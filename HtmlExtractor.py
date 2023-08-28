import re
import requests
from bs4 import BeautifulSoup
from logger import logger

class HtmlExtractor():
  def __init__(self, url: str) -> None:
    super().__init__()

    self.url = url
    self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

  def _get_soup(self):
    try:
      res = requests.get(self.url, timeout=5)
      soup = BeautifulSoup(res.text, 'html.parser')
      return soup
    except Exception as e:
      logger.error('Error', e)
      return ''

  # Ref: https://stackoverflow.com/a/24618186
  def _extract_text_from_soup(self) -> str:
    soup = self._get_soup()
    if (not soup):
      return ''
    
    # kill all script and style elements
    for script in soup(['script', 'style']):
      script.extract() # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text
  
  def get_email(self) -> str:
    html_text = self._extract_text_from_soup()
    
    email_addresses = re.findall(self.email_pattern, html_text)
    # Remove duplicated email
    email_addresses = list(set(email_addresses))

    if (len(email_addresses) == 0):
      return ''
    
    return email_addresses
  