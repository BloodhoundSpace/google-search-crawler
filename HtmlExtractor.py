import re

class HtmlExtractor():
  def __init__(self) -> None:
    pass

  # Ref: https://stackoverflow.com/a/24618186
  def extract_text(self, soup) -> str:
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
  
  def get_email(self, text: str) -> str:
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email_addresses = re.findall(email_pattern, text)
    # Remove duplicated email
    email_addresses = list(set(email_addresses))

    return email_addresses
  