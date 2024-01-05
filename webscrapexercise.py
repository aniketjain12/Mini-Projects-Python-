import requests
import bs4
'''
res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup('res.text','lxml')
soup.select('.author')
authors = set()
for name in soup.select('.author'):
  authors.add(name.text)

quotes = []
for quote in soup.select('.text'):
  quote.append(quotes.text)

#for item in soup.select('.tag-item'):
  #print(item.text)
'''

url = 'http://quotes.toscrape.com/page/'
authors = set()
for page in range(1,10):
  page_url = url+str(page)

  res=requests.get(page_url)
  soup = bs4.BeautifulSoup(res.text,'lxml')
  
  for name in soup.select('.author'):
    authors.add(name.text)
print(authors)    