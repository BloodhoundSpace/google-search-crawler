import json
from src.GoogleSearchResults import GoogleSearchResults

params = {
  'q': 'orange cat',
  'num': 10,
  'gl': 'uk',
  'hl': 'en',
  'location': 'London',
  'device': 'desktop',
}

if __name__ == '__main__':
  print(f'🤖 Query: {params.get("q")}')
  
  google_search = GoogleSearchResults()
  results = google_search.search(params)

  print('🔥 Organic Results:')
  print(json.dumps(results, indent=2, ensure_ascii=False))
  