
#products = soup.select('.product_pod')
#example = products[0]
# 'star rating Three' in str(example)
#[] == example.select('.star rating.Two') #dot to fill space in class
#example('a')[1]['title']
# We can check if someting is 2 stars (string call in, example.select(rating))
#example.seexample('a')[1]['title'] to grab the book title
import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

#res = requests.get(base_url.format(1))
#soup = bs4.BeautifulSoup(res.text,'lxml')

two_star_titles = []

for n in range(1,51):

  scrape_url = base_url.format(n)
  res = requests.get(scrape_url)

  soup = bs4.BeautifulSoup(res.text,'lxml')
  books = soup.select('.product_pod')

  for book in books:

    #if 'star-rating Two in str(book)':
    if len(book.select('.star-rating.Two')) != 0:
      book_title = book.select('a')[1]['title']
      two_star_titles.append(book_title)

print(list(two_star_titles))