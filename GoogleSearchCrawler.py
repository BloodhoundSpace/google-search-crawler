from urllib.parse import quote, unquote, urlparse
import requests
from bs4 import BeautifulSoup
import whois
from logger import logger
from configs import CRAWLER_CONFIGS, IGNORE_SITES

class GoogleSearchCrawler():
  def __init__(self) -> None:
    super().__init__()

    self.search_endpoint = 'https://www.google.com/search'

    self.headers = {
      'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
      'Host': 'www.google.com',
      'Referer': 'https://www.google.com/'
    }

  def _get_search_url(self, query: str, page: int) -> str:
    search_url = f'{self.search_endpoint}?q={quote(query)}&start={page * 10}'

    return search_url

  def _get_source(self, url: str) -> requests.Request:
    return requests.get(url, headers=self.headers)
  
  def _extract_url(self, url: str) -> str:
    start_marker = 'url='
    end_marker = '&ved='

    start_index = url.find(start_marker) + len(start_marker)
    end_index = url.find(end_marker)

    extracted_url = url[start_index:end_index]
    
    return unquote(extracted_url)
  
  def _extract_domain(self, url: str) -> str:
    domain = urlparse(url).netloc

    return domain
  
  def _get_country_from_domain(self, domain: str) -> str:
    try:
      domain_info = whois.whois(domain)
      country = domain_info['country']
      return country
    except Exception as e:
      logger.error('Error', e)
      return ''
    
  def _is_site_ignore(self, domain: str) -> bool:
    removed_www_domain = domain.replace('www.', '', 1)
    return removed_www_domain in IGNORE_SITES

  def search(self, query: str, page = 1):
    search_url = self._get_search_url(query, page)
    res = self._get_source(search_url)

    logger.info(f'👀 {search_url}')

    soup = BeautifulSoup(res.text, 'html.parser')
    result_containers = soup.findAll('div', class_='Gx5Zad fP1Qef xpd EtOod pkphOe')
    
    results = []
    for container in result_containers:
      title = ''
      if (container.find('div', class_='BNeawe vvjwJb AP7Wnd UwRFLe')):
        title = container.find('div', class_='BNeawe vvjwJb AP7Wnd UwRFLe').text
      
      url = container.find('a')['href']
      extracted_url = self._extract_url(url)
      des = ''
      if (container.find('div', class_='BNeawe s3v9rd AP7Wnd')):
        des = container.find('div', class_='BNeawe s3v9rd AP7Wnd').get_text()
      
      if (title and extracted_url):
        domain = self._extract_domain(extracted_url)
        is_site_ignore = self._is_site_ignore(domain)
        if (not is_site_ignore):
          country = '' if not CRAWLER_CONFIGS['is_crawl_country'] \
            else self._get_country_from_domain(domain)
          
          results.append({
            'domain': domain,
            'page': page,
            'url': extracted_url,
            'title': title,
            'description': des,
            'country': country
          })

    return results
  