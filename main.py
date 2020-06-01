import requests
from bs4 import BeautifulSoup

pageGoogle = requests.get('http://www.google.com/ncr')
soup = BeautifulSoup(pageGoogle.content, 'html.parser')

msgGoogle = 'The title of the page www.google.com is ' + soup.title.text

pageWikipedia = requests.get('http://www.wikipedia.com')
soup = BeautifulSoup(pageWikipedia.content, 'html.parser')

msgWikipedia = 'The title of the page www.wikipedia.com is ' + soup.title.text

print ('\n')
print (msgGoogle)
print (msgWikipedia)
print ('\n')