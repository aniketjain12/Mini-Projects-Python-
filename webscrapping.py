import requests
import bs4
'''
result = requests.get("https://en.wikipedia.org/wiki/International_Cricket_Council")
result.text
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup.select('title')[0].getText())

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text,"lxml")
first_item = soup.select('.vector-toc-text')[1]
print(first_item.text)
for item in soup.select('.vector-toc-text'):
  print(item.text)
'''
res1 = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res1.text, 'lxml')
#soup.select('.image')
computer = soup.select('.image')[0]
#print(computer['src'])
image_link = requests.get(
'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'
)

#image_link.content
f = open('computer_image.jpg', 'wb')  #.jpg should be same as image .jpg
f.write(image_link.content)
f.close()
