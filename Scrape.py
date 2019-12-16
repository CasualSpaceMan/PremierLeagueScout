import bs4 as BeautifulSoup
import requests
import pandas

def Scrape(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	print(soup.prettify())
Scrape('https://www.premierleague.com/stats/top/clubs/')		

