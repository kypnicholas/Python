import requests
import bs4
import lxml

result = requests.get("http://www.example.com")

print(type(result))
# print(result.text)                                   

soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
print(soup.select('title'))                     # by default returns a LIST as there might be multiple elements with the same tags.
print(soup.select('title')[0])                  # return only the first element (with the tags).
print(soup.select('title')[0].getText())        # return only the text.



## Grab ALL elements of a class

'''
soup.select('div')                  All elements with the <div> tag
soup.select('#some_id')             All elements that CONTAIN the id attribute of some_id
soup.select('.notice')              All the HTML elements with the CSS class named notice
soup.select('div span')             Any elements named <span> that are WITHIN an element named <div>
soup.select('div > span')           Any elements named <span> that are directly within an element named <div>, with no other element in between
'''

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,"lxml")

#print(soup.select(".vector-toc-text"))

for item in soup.select(".vector-toc-text"):
    print(item.text)



## GRAB AN IMAGE
import requests
import bs4
import lxml

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('c:/Users/nkypri01/Downloads/my_new_file_name.jpg','wb')
f.write(image_link.content)
f.close()