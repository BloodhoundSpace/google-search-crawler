from pprint import pprint
from GoogleSearchCrawler import GoogleSearchCrawler

START_PAGE = 1
END_PAGE = 10

SEARCH_INPUT = 'Why orange cats are weird'

if __name__ == '__main__':
  while(START_PAGE <= END_PAGE):
    Crawler = GoogleSearchCrawler()
    results = Crawler.search(SEARCH_INPUT, START_PAGE)
    pprint(results)

    START_PAGE += 1
