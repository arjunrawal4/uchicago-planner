# Scrapes the Uchicago Course Website 
#
# Uncommon Hacks: 2/10/2018
# Team: Arthur

import bs4
import csv
import urllib.parse
import requests
import re


def get_soup(url):
	'''
	Given a url(str), returns a BeautifulSoup object.
	'''
	re = requests.get(url)
	html = re.text.encode()
	soup = bs4.BeautifulSoup(html, 'lxml')

	return soup


def get_absolute_url(rel):
	'''
	Given a relative url(str), returns the absolute url(str).
	'''
	return 'http://collegecatalog.uchicago.edu' + rel


def crawl(start):
	'''
	Crawls the course catalog and returns a dictionary of data
	pretaining to the courses. 
	'''
	soup = get_soup(start)

	links = soup.find_all('a', class_='sitemaplink')
	data = {}

	for link in links:
		
		url = get_absolute_url(link.get('href'))
		soup1 = get_soup(url)

		tags = soup1.find_all('div', class_='courseblock main')

		
		for tag in tags:
			get_the_stuff(tag, data)


	return data

		
def get_the_stuff(tag, d):
	'''
	Given a tag, returns the 
	'''
	sub = find_sequence(tag)

	if not sub:
		sub.append(tag)

	print(len(sub))

	for course in sub:

		reg = '([A-Z]{4})\\xa0([0-9]{5})\.  (.+).'
		title = course.find('p', class_="courseblocktitle").text
		dept, num, tit = re.findall(reg, title)[0]
		print(dept,num,tit)
		ident = dept + ' ' + num
		d[ident] = {'dept':dept, 'num':num, 'title':tit}
		desctag = tag.find('p', class_="courseblockdesc")
		if desctag:
			d[ident]['desc'] = desctag.text
		else:
			d[ident]['desc'] = None


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

