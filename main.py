from GoogleSearchCrawler import GoogleSearchCrawler
from ExcelWriter import ExcelWriter
from logger import logger
from configs import CRAWLER_CONFIGS

if __name__ == '__main__':
  search_input = CRAWLER_CONFIGS['search_input']
  start_page = CRAWLER_CONFIGS['start_page']
  end_page = CRAWLER_CONFIGS['end_page']
  
  results = []
  is_result_empty = False
  
  logger.info(f'🤖 Keyword: {search_input}')
  # Step 1: Crawl Data from Google Search
  crawler = GoogleSearchCrawler()
  while(
    start_page <= end_page
    and not is_result_empty
  ):
    result = crawler.search(search_input, start_page)
    if (not result):
      is_result_empty = True
    else:
      results.extend(result)
      start_page += 1

  # Step 2: Save results data to Excel with filename = search string
  filename = search_input.lower().replace(' ', '-')
  if (not results):
    logger.info('🚬 No results found')
  else:
    excel_writer = ExcelWriter(filename)
    excel_writer.save_to_excel(results)

    logger.info('🎉 Done')
  