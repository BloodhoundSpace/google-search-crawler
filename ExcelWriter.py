import pandas as pd
from logger import logger

class ExcelWriter():
  def __init__(self, filename: str) -> None:
    self.filename = filename + '.xlsx'
    self.sheet_name = 'Sheet1'
    self.engine = 'xlsxwriter'
    self.desired_column_order = ['domain', 'page', 'url', 'title', 'description']

  def save_to_excel(self, data) -> None:
    logger.info(f'🔧 Save to file {self.filename}')
    
    # Get Dataframe
    df = pd.DataFrame(data)
    df = df[self.desired_column_order]

    # Specify the Excel writer
    writer = pd.ExcelWriter(self.filename, engine=self.engine)

    # Write the DataFrame to Excel
    df.to_excel(writer, sheet_name=self.sheet_name, index=False)

    # Get the xlsxwriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets[self.sheet_name]

    # Set Columns Width
    self._set_columns_width(worksheet, df)

    # Add Clickable for Link (domain, url)
    self._add_clickable(workbook, worksheet, data, df)

    # Close the Excel file
    writer.close()

  def _set_columns_width(self, worksheet, df) -> None:
    # Define and set column width
    column_widths = {
      'domain': 22,
      'page': 4,
      'url': 45,
      'title': 45,
      'description': 60
    }
    
    for column_name, max_width in column_widths.items():
      col_index = df.columns.get_loc(column_name)
      worksheet.set_column(col_index, col_index, max_width)

  def _add_clickable(self, workbook, worksheet, data, df) -> None:
    # Define a cell format for the URLs
    url_format = workbook.add_format({'color': 'blue'})

    # Add clickable URLs using write_url()
    for row_num, row_data in enumerate(data, start=1):
      url = row_data['url']
      domain = row_data['domain']
      worksheet.write_url(
        row_num, df.columns.get_loc('url'),
        url, string=url,
        cell_format=url_format
      )
      worksheet.write_url(
        row_num, df.columns.get_loc('domain'),
        'http://' + domain, string=domain,
        cell_format=url_format
      )
