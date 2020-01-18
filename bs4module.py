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