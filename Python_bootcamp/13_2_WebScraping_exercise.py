import requests
import bs4
import lxml 


res = requests.get('http://quotes.toscrape.com/')

soup = bs4.BeautifulSoup(res.text,"lxml")

## TASK - Select the authors from the first page

# Print a clean list of authors
authors = set()                             # create a set to avoid duplicates. (sets only allow unique values)
for name in soup.select(".author"):
    authors.add(name.text)

print('\n'.join(authors))

# TASK - Create a list of all the quotes on the first page.

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print('\n'.join(quotes))


# TASK - Extract the top ten tags from the homepage 

tags = []
for tag in soup.select(".tag-item"):
    tags.append(tag.text)

print('\n'.join(tags))



# TASK - loop through all the pages and get all the unique authors on the website.

url = 'http://quotes.toscrape.com/page/'
authors = set()

for page in range(1,10):

    # Concatenate to get new page URL = http://quotes.toscrape.com/page/2
    page_url = url+str(page)

    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')

    for name in soup.select(".author"):
        authors.add(name.text)

print('\n'.join(authors))