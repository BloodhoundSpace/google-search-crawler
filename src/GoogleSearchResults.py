import requests
import uule_grabber
from parsel import Selector
from urllib.parse import quote, unquote
from src.utils import clean_str, clean_dict, GOOGLE_STATUS_CODE

class GoogleSearchResults():
  def __init__(self) -> None:
    self.search_endpoint = 'https://www.google.com/search'
    self.headers = {
      'Host': 'www.google.com',
      'Referer': 'https://www.google.com/',
      'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    }
  
  def search(self, params: dict) -> list[dict]:
    search_url = self._get_search_url(params)
    print(f'👀 {search_url}')
    
    res = self._get_source(search_url)
    if res.status_code != 200:
      raise Exception(GOOGLE_STATUS_CODE[str(res.status_code)])
    
    selector = self._get_selector(res.text)
    
    results = self._extract_organic_results(selector)

    return results
  
  def _get_source(self, url: str) -> requests.Response:
    return requests.get(url, headers=self.headers)
  
  def _get_selector(self, text: str) -> Selector:
    return Selector(text=text)

  def _get_search_url(self, params: dict) -> str:
    if params.get('q') is None:
      raise 'Missing query parameter'
    
    query = quote(params.get('q'))
    num = params.get('num') or 10
    gl = params.get('gl') # Region
    hl = params.get('hl') # Language
    location = params.get('location')
    
    search_url = f'{self.search_endpoint}?q={query}&num={num}'

    if gl is not None:
      search_url += f'&gl={gl}'
    if hl is not None:
      search_url += f'&hl={hl}'
    if location is not None:
      uule = self._generate_ggs_uule(location)
      search_url += f'&uule={uule}'

    return search_url
  
  def _generate_ggs_uule(self, location: str) -> str:
    return uule_grabber.uule(location)
  
  def _extract_url(self, url: str) -> str:
    start_marker = 'url='
    end_marker = '&ved='

    start_index = url.find(start_marker) + len(start_marker)
    end_index = url.find(end_marker)

    extracted_url = url[start_index:end_index]
    
    return unquote(extracted_url)
  
  def _extract_single_element(self, element, xpath, is_get_all=False):
    try:
      e = element.xpath(xpath)
      if e is not None:
        if is_get_all:
          return e.getall()
        else:
          return e.get()
      else:
        return ''
    except Exception:
      return ''
  
  def _extract_organic_results(self, selector: Selector) -> list[dict] | None:
    xpath = {
      'elements': '//div[contains(@class, "Gx5Zad fP1Qef xpd EtOod pkphOe") and not(ancestor::div[contains(@class, "uEierd")])]',
      'component': {
        'title': './/div[@class="BNeawe vvjwJb AP7Wnd UwRFLe"]/text()',
        'snippet': './/div[@class="BNeawe s3v9rd AP7Wnd"]/text()',
        'link': './/div[@class="egMi0 kCrYT"]/a/@href',
        'displayed_link': './/div[@class="BNeawe UPmit AP7Wnd lRVwie"]/text()',
        'rich_snippet': './/div[@class="BNeawe s3v9rd AP7Wnd"]//span[@class="r0bn4c rQMQod"]//text()',
        'sitelinks': {
          'inline': {
            'elements': './/div[@class="BNeawe s3v9rd AP7Wnd"]/span[@class="BNeawe"]',
            'component': {
              'title': './/span[@class="XLloXe AP7Wnd"]/text()',
              'link': './/a/@href',
            }
          }
        }
      }
    }

    try:
      organic_results = []
      xpath_elements = xpath['elements']
      xpath_component = xpath['component']

      elements = selector.xpath(xpath_elements)
      for index, e in enumerate(elements, start=1):
        title = self._extract_single_element(e, xpath_component['title'])
        snippet = self._extract_single_element(e, xpath_component['snippet'], is_get_all=True)
        link = self._extract_single_element(e, xpath_component['link'])
        displayed_link = self._extract_single_element(e, xpath_component['displayed_link'])
        rich_snippet = self._extract_single_element(e, xpath_component['rich_snippet'], is_get_all=True)

        # Extract sitelinks
        inline_sitelinks = []
        inline_sitelink_elements = e.xpath(
          xpath_component['sitelinks']['inline']['elements']
        )
        for inline_e in inline_sitelink_elements:
          inline_title = self._extract_single_element(
            inline_e,
            xpath_component['sitelinks']['inline']['component']['title']
          )
          inline_link = self._extract_single_element(
            inline_e,
            xpath_component['sitelinks']['inline']['component']['link']
          )
          inline_sitelinks.append({
            'title': inline_title,
            'link': self._extract_url(inline_link)
          })

        organic_obj = {
          'position': index,
          'title': clean_str(title),
          'snippet': clean_str(''.join(snippet)),
          'link': self._extract_url(link),
          'displayed_link': displayed_link,
          'rich_snippet': ' '.join(rich_snippet).replace(' · ', '').strip(),
          'sitelinks': inline_sitelinks
        }

        organic_results.append(clean_dict(organic_obj))
      
      return organic_results
    except Exception:
      return None
  