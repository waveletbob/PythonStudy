#-*- coding=utf-8 -*-
import urllib.request as urllib2
import ssl
from lxml import  etree

url='https://movie.douban.com/top250'
context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)

def fetch_page(url):
	response=urllib2.urlopen(url,context=context)
def parse(url):
	response=fetch_page(url)
	page=response.read()
	html=etree.HTML(page)
	xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
	xpath_title = './/span[@class="title"]'
	xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

	pages = html.xpath(xpath_pages)
	fetch_list = []
	result = []

	for element_movie in html.xpath(xpath_movie):
		result.append(element_movie)

	for p in pages:
		fetch_list.append(url + p.get('href'))

	for url in fetch_list:
		response = fetch_page(url)
		page = response.read()
		html = etree.HTML(page)
		for element_movie in html.xpath(xpath_movie):
			result.append(element_movie)

	for i, movie in enumerate(result, 1):
		title = movie.find(xpath_title).text         
		print(i, title)
def main():
	from time import time
	start=time()
	for i in range(5):
		parse(url)
	end=time()
	print("cost time:{}".format((end-start)/5))

	
if __name__ == '__main__':
	main()