from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs').text
	
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

for article in soup.find_all('td', class_='overview-top'):
	Movietitle = article.a.text
	print(Movietitle)