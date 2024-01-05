import requests
import bs4

result = requests.get("https://www.freepik.com/premium-vector/team-business-people-preparing-about-environmental-protection-nature-conservation_26055515.htm")

soup = bs4.BeautifulSoup(result.text,"lxml")

link_image = requests.get("https://img.freepik.com/premium-vector/team-business-people-preparing-about-environmental-protection-nature-conservation_101179-1893.jpg")

f =open('ppt.jpg','wb')
f.write(link_image.content)
f.close()
