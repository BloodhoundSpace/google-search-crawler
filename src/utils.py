import re

GOOGLE_STATUS_CODE = {
  # 2xx: success
  '200': {
    'code': 200,
    'type': 'success',
    'name': 'success',
    'description': 'Google passes on the content to the indexing pipeline. The indexing systems may index the content, but thats not guaranteed.'
  },
  '201': {
    'code': 201,
    'type': 'success',
    'name': 'created',
    'description': 'Google passes on the content to the indexing pipeline. The indexing systems may index the content, but thats not guaranteed.'
  },
  '202': {
    'code': 202,
    'type': 'success',
    'name': 'accepted',
    'description': 'Googlebot waits for the content for a limited time, then passes on whatever it received to the indexing pipeline. The timeout is user agent dependent, for example Googlebot Smartphone may have a different timeout than Googlebot Image.'
  },
  '204': {
    'code': 204,
    'type': 'success',
    'name': 'no content',
    'description': 'Googlebot signals the indexing pipeline that it received no content. Search Console may show a soft 404 error in the sites Page Indexing report.'
  },
  # 3xx: redirection
  '301': {
    'code': 301,
    'type': 'redirection',
    'name': 'moved permanently',
    'description': 'Googlebot follows the redirect, and the indexing pipeline uses the redirect as a strong signal that the redirect target should be canonical.'
  },
  '302': {
    'code': 302,
    'type': 'redirection',
    'name': 'found',
    'description': 'Googlebot follows the redirect, and the indexing pipeline uses the redirect as a weak signal that the redirect target should be canonical.'
  },
  '303': {
    'code': 303,
    'type': 'redirection',
    'name': 'see other',
    'description': 'Googlebot follows the redirect, and the indexing pipeline uses the redirect as a weak signal that the redirect target should be canonical.'
  },
  '304': {
    'code': 304,
    'type': 'redirection',
    'name': 'not modified',
    'description': 'Googlebot signals the indexing pipeline that the content is the same as last time it was crawled. The indexing pipeline may recalculate signals for the URL, but otherwise the status code has no effect on indexing.'
  },
  '307': {
    'code': 307,
    'type': 'redirection',
    'name': 'temporary redirect',
    'description': 'Equivalent to 302.'
  },
  '308': {
    'code': 308,
    'type': 'redirection',
    'name': 'moved permanently',
    'description': 'Equivalent to 301.'
  },
  # 4xx: client errors
  '400': {
    'code': 400,
    'type': 'client errors',
    'name': 'bad request',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '401': {
    'code': 401,
    'type': 'client errors',
    'name': 'unauthorized',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '403': {
    'code': 403,
    'type': 'client errors',
    'name': 'forbidden',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '404': {
    'code': 404,
    'type': 'client errors',
    'name': 'not found',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '410': {
    'code': 410,
    'type': 'client errors',
    'name': 'gone',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '411': {
    'code': 411,
    'type': 'client errors',
    'name': 'length required',
    'description': 'All 4xx errors, except 429, are treated the same: Googlebot signals the indexing pipeline that the content doesnt exist.'
  },
  '429': {
    'code': 429,
    'type': 'client errors',
    'name': 'too many requests',
    'description': 'Googlebot treats the 429 status code as a signal that the server is overloaded, and its considered a server error.'
  },
  # 5xx: server errors
  '500': {
    'code': 500,
    'type': 'server errors',
    'name': 'internal server error',
    'description': 'Googlebot decreases the crawl rate for the site. The decrease in crawl rate is proportionate to the number of individual URLs that are returning a server error. Googles indexing pipeline removes from the index URLs that persistently return a server error.'
  },
  '502': {
    'code': 411,
    'type': 'server errors',
    'name': 'bad gateway',
    'description': 'Googlebot decreases the crawl rate for the site. The decrease in crawl rate is proportionate to the number of individual URLs that are returning a server error. Googles indexing pipeline removes from the index URLs that persistently return a server error.'
  },
  '503': {
    'code': 503,
    'type': 'server errors',
    'name': 'service unavailable',
    'description': 'Googlebot decreases the crawl rate for the site. The decrease in crawl rate is proportionate to the number of individual URLs that are returning a server error. Googles indexing pipeline removes from the index URLs that persistently return a server error.'
  },
}

def clean_str(str: str):
  try:
    # Remove special charactor (like \t \n)
    str = re.sub(r'[\n\t]', ' ', str)
    
    # Remove extra spaces
    str = re.sub(r'\s+', ' ', str)
    
    # Remove leading and trailing spaces
    str = str.strip()

    return str
  except Exception:
    return str
  
def clean_dict(dict: dict):
  return {
    key: value for key, value in dict.items()
    if value is not None
      and ((not isinstance(value, list) or len(value) > 0)
      and (not isinstance(value, str) or value.strip()))
  }
