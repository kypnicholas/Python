import requests
import bs4
import lxml

## GOAL: Get the title of every book that has a 2 star rating and at the end just have a Python list with all their titles. ## 

# Base URL for the catalogue of books we need to loop through. 
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'       # The curly brackets will allow us to specify the page number

res = requests.get(base_url.format('1'))

soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup.select(".product_pod"))                    # it looks like that all the information we need is under this class

products = soup.select(".product_pod")
example = products[0]                           # confirm that we can get athe first book off the list and check the info it contains. 

# print(example)

# Now we are checking if the first book in the catalogue is a 3 star rating
print(example.select('.star-rating.Three'))     # NOTE that if there is a space in a class name we need to replace it with a dot (.)


# But we want only the 2 star ratings 
# THIS IS OUR LOGIC
two_star_titles = []

for n in range(1,5):
    scrape_url = base_url.format(n)         
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:                   # check if the length of the value returned of 2 star rating titles is greater than 0
            two_star_titles.append(book.select('a')[1]['title']) 


print('\n'.join(two_star_titles))           # Print the items of the list with new-line. 

