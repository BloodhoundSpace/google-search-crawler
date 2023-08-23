from GoogleSearchCrawler import GoogleSearchCrawler
from ExcelWriter import ExcelWriter
from logger import logger

SEARCH_INPUT = 'Why orange cats are weird'

START_PAGE = 1
END_PAGE = 2

RESULTS = []

if __name__ == '__main__':
  logger.info(f'🤖 Keyword: {SEARCH_INPUT}')
  # Step 1: Crawl Data from Google Search
  crawler = GoogleSearchCrawler()
  while(START_PAGE <= END_PAGE):
    result = crawler.search(SEARCH_INPUT, START_PAGE)
    RESULTS.extend(result)
    START_PAGE += 1

  # Step 2: Save results data to Excel with filename = search string
  filename = SEARCH_INPUT.lower().replace(' ', '-')
  excel_writer = ExcelWriter(filename)
  excel_writer.save_to_excel(RESULTS)

  logger.info('🎉 Done')
  