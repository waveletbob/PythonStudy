#!/usr/bin/env python
#coding=utf-8
import asyncio #3.4的协程
import gevent#一个线程进行的协程，切换函数，无切换线程花销无需加锁，当线程多时优势大
import threading
from gevent import monkey;monkey.patch_all()
import urllib2
def getbody(i):
	print("started",i)
	urllib2.urlopen("http://www.baidu.com")
	print("end",i)
tasks=[gevent.spawn(getbody,i)for i in range(3)]
gevent.joinall(tasks)
for i in range(3):
	t=threading.Thread(target=getbody,args=(i,))
t.start()
# import os
# import random
# command='netstat -na'
# result=os.popen(command).read()
# print(result)


'''
实现计算曝光商品在一次曝光列表中的位置，淘宝搜索结果页用户可选择排序类型，
比如按销量从高到低排序，按价格从高到低排序等，
现采集到搜索结果页的日志数据包括如下字段：item_list（商品id列表）,  
item_price_list（商品价格列表，跟商品id一一对应）,
根据item_id和item_price计算商品在一次曝光中出现的位置，
从0开始计数，要求时间复杂度不能为O（N），N为商品列表长度,  
item_price存在多个商品价格相同的情况,
当商品id列表长度跟商品价格列表长度不一致返回-1，这里要注意商品价格并不一定是有序的。
'''



# import numpy as np
# np.set_printoptions(precision=3)
# print(np.random.dirichlet((1,1,1,1,1,1),5))
# print(np.random.dirichlet((6,3,2,2,2,1),5))
# print(np.random.dirichlet((0.2,0.2,0.2,0.2,0.2,0.2),5))

#! /usr/bin/env python
# from os import path
# #from wordcloud import WordCloud
# d=path.dirname(__file__)
# print d
# import pylab as pl




# from matplotlib import pyplot as plt
# import random
# def transformation_1(p):
# 	x=p[0]
# 	y=p[1]
# 	x1=0.85*x+0.04*y
# 	y1=-0.04*x+0.85*y+1.6
# 	return x1,y1
# def transformation_2(p):
# 	x=p[0]
# 	y=p[1]
# 	x1=0.2*x+0.26*y
# 	y1=0.23*x+0.22*y+1.6
# 	return x1,y1
# def transformation_3(p):
# 	x=p[0]
# 	y=p[1]
# 	x1=-0.15*x+0.28*y
# 	y1=0.26*x+0.24*y+0.44
# 	return x1,y1
# def transformation_4(p):
# 	x=p[0]
# 	y=p[1]
# 	x1=0
# 	y1=0.16*y
# 	return x1,y1
# def get_index(probability):
# 	r=random.random()
# 	c_probability=0
# 	sum_probability=[]
# 	for p in probability:
# 		c_probability+=p
# 		sum_probability.append(c_probability)
# 	for item,sp in enumerate(sum_probability):
# 		if r<=sp:
# 			return item
# 	return len(probability)-1 
# def transform(p):
# 	transformations=[transformation_1,transformation_2,transformation_3,transformation_4]
# 	probability=[0.85,0.07,0.07,0.01]
# 	tindex=get_index(probability)
# 	list_t.append(tindex)
# 	t=transformations[tindex]
# 	x,y=t(p)
# 	return x,y
# def draw_fern(n):
# 	x=[0]
# 	y=[0]
# 	x1,y1=0,0
# 	for i in range(n):
# 		x1,y1=transform((x1,y1))
# 		x.append(x1)
# 		y.append(y1)
# 	return x,y
# list_t=[]
# n=10000
# x,y=draw_fern(n)
# plt.plot(x,y,'o')
# plt.title("")
# plt.show()

# import os,sys	
# parameter=sys.argv[1:]
# print parameter
# print os.system('ping www.baidu.com')


# #基于标签推荐
# from math import sqrt
# import random
# def cosinSimilarity(item_tags,i,j):
# 	ret=0
# 	for b,wib in item_tags[i].items():
# 		if b in item_tags[j]:
# 			ret+=wib*item_tags[j][b]
# 	ni=0
# 	nj=0
# 	for b,w in item_tags[i].items():
# 		ni+=w*w
# 	for b,w in item_tags[j].items():
# 		nj+=w*w
# 	if ret==0:
# 		return 0
# 	return ret/sqrt(ni*nj)
# def diversity(item_tags,recommend_items):
# 	ret=0
# 	n=0
# 	for i in recommend_list.keys():
# 		for j in recommend_items.keys():
# 			if i==j:
# 				continue
# 			ret+=cosinSimilarity(item_tags,i,j)
# 			n+=1
# 	return ret/(n*1.0)
# def addValueToMat(theMat,key,value,incr):    
#     if key not in theMat: #如果key没出先在theMat中    
#         theMat[key]=dict();    
#         theMat[key][value]=incr;    
#     else:    
#         if value not in theMat[key]:    
#             theMat[key][value]=incr;    
#         else:    
#             theMat[key][value]+=incr;#若有值，则递增   
# def init():
# 	with open(u'E:\\迅雷下载\\数据集\\delicious\\delicious.dat','r') as f:
# 		line=f.readline()
# 		while line:
# 			terms=line.split('\t')
# 			user=terms[0]
# 			item=terms[1]
# 			tag=terms[2]
# 			if random.random()>0.1:
# 				addValueToMat(user_tags,user,tag,1)
# 				addValueToMat(tag_items,tag,item,1)
# 				addValueToMat(user_items,user,item,1)
# 				line=f.readline()
# 			else:
# 				addValueToMat(user_items_test,user,item,1)
# def Recommend(usr):  
#     recommend_list = dict();    
#     tagged_item = user_items[usr];#得到该用户所有推荐过的物品    
#     for tag_,wut in user_tags[usr].items():#用户打过的标签及次数    
#         for item_,wit in tag_items[tag_].items():#物品被打过的标签及被打过的次数    
#             if item_ not in tagged_item:#已经推荐过的不再推荐    
#                 if item_ not in recommend_list:    
#                     recommend_list[item_]=wut*wit;#根据公式    
#                 else:    
#                     recommend_list[item_]+=wut*wit;    
#     return sorted(recommend_list.iteritems(), key=lambda a:a[1],reverse=True)  
# #给用户u推荐整个系统里最热门的标签
# def RecommendPopularTags(user,item,tags,N):
# 	return sorted(tags.items(),key=itemgetter(1),reversed=True)[0:N]
# #给用户u推荐物品i上最热门的标签
# def RecommendItemPopularTags(user,item,user_tags,N):
# 	return sorted(item_tags[item].items(), key=itemgetter(1), reverse=True)[0:N]
# #给用户u推荐他自己经常使用的标签
# def RecommendUserPopularTags(user,item, user_tags, N):
# 	return sorted(user_tags[user].items(), key=itemgetter(1), reverse=True)[0:N]
# #前面两种的融合
# def RecommendHybridPopularTags(user,item, user_tags, item_tags, alpha, N):
# 	max_user_tag_weight = max(user_tags[user].values())
# 	for tag, weight in user_tags[user].items():
# 		ret[tag] = (1-alpha) * weight / max_user_tag_weight  
# 		max_item_tag_weight = max(item_tags[item].values())  
# 	for tag, weight in item_tags[item].items():
# 		if tag not in ret:
# 			ret[tag] = alpha * weight / max_item_tag_weight  
# 		else:  
# 			ret[tag] += alpha * weight / max_item_tag_weight  
# 	return sorted(ret[user].items(), key=itemgetter(1), reverse=True)[0:N]
# user_tags=dict()
# tag_items=dict()
# user_items=dict()
# user_items_test=dict()	
# init()
# print user_tags
# recommend_list=Recommend('48411')
# for recommend in recommend_list[:10]:
# 	print recommend

#quicksort
# def quicksort(arr):
# 	if(len(arr)<=1):
# 		return arr
# 	pivot=arr[len(arr)/2]
# 	left=[x for x in arr if x<pivot]
# 	middle=[x for x in arr if x==pivot]
# 	right=[x for x in arr if x>pivot]
# 	return quicksort(left)+middle+quicksort(right)
# print quicksort([3,6,8,9,5,4,1,2])

#int boolean strings

#socket
# import socket
# import threading
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('localhost',5550))
# sock.listen(5)
# print('Server', socket.gethostbyname('localhost'), 'listening ...') 

# mydict = dict()  
# mylist = list()
# def tellOthers(exceptNum, whatToSay):  
# 	for c in mylist:  
# 		if c.fileno() != exceptNum :  
# 			try:  
# 				c.send(whatToSay.encode())  
# 			except:
# 				pass
# def subThreadIn(connection,connNum):
# 	nickname=connection.recv(1024).decode()
# 	mydict[connection.fileno()]=nickname
# 	mylist.append(connection)
#  	pass 
# while True:
# 	connection,addr=sock.accept()
# 	print("Accepted a new connection,",connection.getsockname(),connection.fileno())
# 	try:
# 		buf=connection.recv(1024).decode()
# 		if buf=='1':
# 			connection.send(b'welcome to server')
# 			mythread=threading.Thread(target=subThreadIn,args=(connection,connection.fileno()))
# 			mythread.setDaemon(True)
# 			mythread.start()
# 		else:
# 			connection.send(b'please go out')
# 			connection.close()
# 	except Exception as e:
# 		pass