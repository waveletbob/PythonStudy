#coding:utf-8
#https://movie.douban.com/top250?start=50&filter
import socket
import ssl
import time
import requests
def get(url):
	r=requests.get(url,headers={'User-Agent': 'Mozilla/4.0'})
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	return r.text

	# host='movie.douban.com'
	# path=url[24:]
	# print('path',path)
#http
	# s=socket.socket()
	# port=80
	#https
	# s=ssl.wrap_socket(socket.socket())
	# port=443
	# s.connect((host,port))
	# # request='GET{}HTTP/1.1\r\nhost:{}\r\n\r\n'.format(path,host)
	# request='''
	# Accept:text/event-stream
	# Accept-Encoding:gzip, deflate, sdch, br
	# Accept-Language:zh-CN,zh;q=0.8
	# Cache-Control:no-cache
	# Connection:keep-alive
	# Host:push.douban.com:4397
	# Origin:https://movie.douban.com
	# Referer:https://movie.douban.com/top250?start=25&filter=
	# User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36
	# '''


	# print(request)
	# print('request',request)
	# s.send(request.encode('utf-8'))
	# response=b''
	# while True:
	# 	size=1024
	# 	r=s.recv(size)
	# 	response+=r
	# 	if len(r)<size:
	# 		break
	# response=response.decode('utf-8')
	# print('response',response)
	return response
def htmls_from_douban():
	html=[]
	url='https://movie.douban.com/top250?start={}&filter='
	for index in range(0,250,25):
		u=url.format(index)
		print('url:',u)
		r=get(u)
		time.sleep(2)
		html.append(r)
	return html
def findall_in_html(html,startpart,endpart):
	all_strings=[]
	start=html.find(startpart)+len(startpart)
	end=html.find(endpart,start)
	string=html[start:end]
	print(string)
	while html.find('</html>')>start>html.find('<html'):
		all_strings.append(string)
		start=html.find(startpart)+len(startpart)
		end=html.find(endpart,start)
		string=html[start:end]
		print(string)
	return all_strings
def movie_name(html):
	name=findall_in_html(html,'<span class="title">', '</span>')
	for i in name:
		if 'nbsp' in i:
			name.remove(i)
	return name
def movie_score(html):
	score=findall_in_html(html,'<span class="rating_num" property="v:average">', '</span>')
	return score
def movie_inq(html):
	inq=findall_in_html(html, '<span class="inq">', '</span>')
	return inq
def number_comment(html):
	temp=findall_in_html(html, '<div class="star">', '</div>')
	num=[]
	for item in temp:
		start=item.find('<span>'+len('<span>'))
		end=item.find('人评价</span>',start)
		n=item[start:end]
		num.append(n)
	return num
def movie_info(htmls):
	movie=[]
	score=[]
	inq=[]
	number=[]
	for h in htmls:
		#extend参数只接受列表，将其中元素添加到自己的后面
		movie.extend(movie_name(h))
		score.extend(movie_score(h))
		inq.extend(movie_inq(h))
		number.extend(number_comment(h))
	data=zip(movie,score,inq,number)
	return data
data=movie_info(htmls_from_douban())
for i in data:
	print(i)
