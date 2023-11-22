# Google Search Crawler

![organic-result](./image/organic-result.png)

## How to run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set parameters

| Parameter | Type | Note |
| --------- | ---- | ---- |
| q | string | Query |
| num | number | Number of results |
| gl | string | Region |
| hl | string | Language |
| location | string | Allows you to see the actual search results by region |
| device | string | `desktop` or `mobile` | 

### 3. Run
```bash
python main.py
```

## Exmaple

### Params

```python
  params = {
    'q': 'orange cat',
    'num': 10,
    'gl': 'uk',
    'hl': 'en',
    'location': 'London',
    'device': 'desktop',
  }
```

### Results

```json
  [
    {
      "position": 1,
      "title": "10 Interesting Facts About Orange Cat Breeds - Rover.com",
      "snippet": "Certain cat breeds are more likely to produce an orange-hued kitty. Some breeds lucky enough to sport an orange coat are the American bobtail, the exotic ...",
      "link": "https://www.rover.com/blog/orange-cat-breeds/",
      "displayed_link": "www.rover.com › blog › orange-cat-breeds"
    },
    {
      "position": 2,
      "title": "Orange Tabby Cats: Everything You Need to Know - A-Z Animals",
      "snippet": "Orange tabby cats everything you need to know is a guide to the cat \"breed\". The Orange tabby isn't a breed, but read to learn more.",
      "link": "https://a-z-animals.com/blog/orange-tabby-cats-everything-you-need-to-know/",
      "displayed_link": "a-z-animals.com › Pet Animals › Cats",
      "rich_snippet": "2 Oct 2023"
    },
    {
      "position": 3,
      "title": "15 Bright and Cheerful Orange Cat Breeds - PureWow",
      "snippet": "15 Bright and Cheerful Orange Cat Breeds · 1. American Curl · 2. American Shorthair · 3. British Shorthair · 4. Cornish Rex · 5. Devon Rex · 6.",
      "link": "https://www.purewow.com/family/orange-cat-breeds",
      "displayed_link": "www.purewow.com › family › orange-cat-breeds",
      "rich_snippet": "20 Sept 2022"
    },
    {
      "position": 4,
      "title": "15 Fascinating Facts About the Orange Tabby Cat (With Pictures)",
      "snippet": "Orange tabbies are known for being friendly and often remind us of Garfield, but there is much more to this cat than meets the eye.",
      "link": "https://www.catster.com/guides/orange-tabby-cat-facts/",
      "displayed_link": "www.catster.com › guides › orange-tabby-cat-facts",
      "rich_snippet": "6 days ago"
    },
    {
      "position": 5,
      "title": "10 Orange Cat Breeds That Have Head-Turning Coats",
      "snippet": "Meowza! Nothing draws your attention like the head-turning coats of these orange cat breeds. These smart, snuggly kitties make perfect pets.",
      "link": "https://www.rd.com/list/orange-cat-breeds/",
      "displayed_link": "www.rd.com › Pets & Animals › Cats",
      "rich_snippet": "20 Jun 2023"
    },
    {
      "position": 6,
      "title": "8 Orange Cat Breeds for Anyone Who Loves a Redhead - Daily Paws",
      "snippet": "8 Orange Cat Breeds for Anyone Who Loves a Redhead · Abyssinian · American Bobtail · Bengal · British Shorthair · Maine Coon · Munchkin.",
      "link": "https://www.dailypaws.com/living-with-pets/pet-compatibility/orange-cat-breeds",
      "displayed_link": "www.dailypaws.com › Living with Pets › Pet Compatibility",
      "rich_snippet": "24 Aug 2020"
    },
    {
      "position": 7,
      "title": "Tabby cat - Wikipedia",
      "snippet": "About 80% of orange tabby cats are male. ... The orange coloring is a gene, found on the X chromosome. Females have XX chromosomes to the male's XY. Thus, both ...",
      "link": "https://en.wikipedia.org/wiki/Tabby_cat",
      "displayed_link": "en.wikipedia.org › wiki › Tabby_cat"
    },
    {
      "position": 8,
      "title": "10 orange tabby cat facts that may surprise you - PetsRadar",
      "snippet": "Discover these 10 facts about orange tabby cats from their warm and loving personalities to their connection with red-headed humans.",
      "link": "https://www.petsradar.com/advice/ten-facts-about-orange-tabby-cats",
      "displayed_link": "www.petsradar.com › advice › ten-facts-about-orange-tabby-cats",
      "rich_snippet": "8 Dec 2022"
    },
    {
      "position": 9,
      "title": "Orange Tabby Cats: Facts, Lifespan & Intelligence",
      "snippet": "This tabby variety is the most unique and can be difficult to identify as a tabby because there are no obvious spots or stripes. Ticked orange ...",
      "link": "https://cats.com/orange-tabby-cats",
      "displayed_link": "cats.com › orange-tabby-cats",
      "rich_snippet": "13 Jun 2023"
    },
    {
      "position": 10,
      "title": "10 orange cat breeds you'll fall in love with | Reader's Digest Australia",
      "snippet": "10 orange cat breeds you'll fall in love with · Gingers for the win! · Bengal · Abyssinian · Maine Coon · Turkish Angora · Egyptian Mau · Devon Rex · Selkirk ...",
      "link": "https://www.readersdigest.com.au/uncategorized/10-orange-cat-breeds-youll-fall-in-love-with",
      "displayed_link": "www.readersdigest.com.au › Articles"
    }
  ]
```
