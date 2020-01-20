import requests, bs4
# get request to download main page
res = requests.get('https://nostarch.com')
res.raise_for_status()
# pass request text to bs4 and store object in noStarchSoup
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems)) #elems is a list of Tag objects.
#<class 'list'>
len(elems)

type(elems[0])
#<class 'bs4.element.Tag'>
print(str(elems[0])) # The Tag object as a string.
#'<span id="author">Al Sweigart</span>'
print(elems[0].getText())
#'Al Sweigart'
print(elems[0].attrs)

pElems = exampleSoup.select('p')
str(pElems[0])
#'<p>Download my <strong>Python</strong> book from <a href="https://
#inventwithpython.com">my website</a>.</p>'
pElems[0].getText()
#'Download my Python book from my website.'
str(pElems[1])
#'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
#'Learn Python the easy way!'
str(pElems[2])
#'<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()
#'By Al Sweigart'

# get() method for Tag objects makes it simple to access attribute values from element
import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
#'<span id="author">Al Sweigart</span>'
spanElem.get('id')
#'author'
spanElem.get('some_nonexistent_addr') == None
#True
spanElem.attrs
#{'id': 'author'}