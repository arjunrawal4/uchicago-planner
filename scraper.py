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
	html = re.text.encode()
	soup = bs4.BeautifulSoup(html, 'lxml')

	return soup

def get_absoulte_url(rel):

	return 'http://collegecatalog.uchicago.edu' + rel

def crawl(start):

	soup = get_soup(start)

	links = soup.find_all('a', class_='sitemaplink')

	for link in links:
		url = get_absoulte_url(link.get('href'))
		
		soup1 = get_soup(url)

		tags = soup.find_all('div', class_='courseblock main')





def is_whitespace(tag):
	'''
	Does the tag represent whitespace?
	'''
	return isinstance(tag, bs4.element.NavigableString) and (tag.strip() == "")


def find_sequence(tag):
	'''
	If tag is the header for a sequence, then
	find the tags for the courses in the sequence.
	'''
	rv = []
	sib_tag = tag.next_sibling
	while is_subsequence(sib_tag) or is_whitespace(tag):
	    if not is_whitespace(tag):
	        rv.append(sib_tag)
	    sib_tag = sib_tag.next_sibling
	return rv

	

def is_subsequence(tag):
    '''
    Does the tag represent a subsequence?
    '''
    return isinstance(tag, bs4.element.Tag) and 'class' in tag.attrs \
        and tag['class'] == ['courseblock', 'subsequence']

















