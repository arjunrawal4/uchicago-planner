# Scrapes the uchicago course website 
#
# uncommon-hacks 2/10/2018
# Team Arthur

import bs4
import csv
import urllib.parse
import requests



def get_soup(url):

	re = requests.get(url)
	html = re.text.encode('iso-8859-1')
	soup = bs4.BeautifulSoup(html, 'lxml')

	return soup

def get_absoulte_url(rel):

	return 'http://collegecatalog.uchicago.edu' + rel

def crawl(start):

	soup = get_soup(start)

	links = soup.find_all('a', class_='sitemaplink')

	for link in links:
		url = get_absoulte_url(link.get('href'))
		print(url)


def get_subsequence(tag):

	sub = []

	if tag














