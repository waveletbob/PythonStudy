#encoding=utf-8  
import jieba
import nltk
from jieba import posseg

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('qt4agg')  
#指定默认字体  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'  


textstr=""
def cutstop(text):
	custr=posseg.cut(text)
	result=""
	for word,flag in custr:
		result+=word+"/"+flag+" "
	return result
def cutstring(text):
	cutstr=jieba.cut(text)
	result=" ".join(cutstr)
	return result
with open(u"E:\\迅雷下载\\数据集\\SogouC-UTF8\\UTF8\\test\C000010\\7999.txt",'r')as f:
	textstr=f.read()
	print type(textstr)
cutedtext=cutstop(textstr)
print(type(cutedtext))
# print(type(cutedtext.split()))
strtag=[nltk.tag.str2tuple(word) for word in cutedtext.split()]
for word,tag in strtag:
	print(word+"/"+tag) 
print(type(cutstring(textstr)))
print(cutstring(textstr))
# for word in cutstring(textstr).split():
# 	print word


tokenstr=nltk.word_tokenize(cutstring(textstr))
f1=nltk.FreqDist(tokenstr)
print("出现三次以上")
# for word in f1.hapaxes():
# 	print word
for word in [w for w in set(tokenstr) if len(w)>3]:
	print word 
f2=nltk.FreqDist(len(w) for w in tokenstr)
for w,c in f2.items():
	print w,"=>",c,"||"
print(f2.keys())
f3=nltk.FreqDist(tokenstr)
print(type(f3))
for w,c in f3.items():
	print w,"=>",c
print(f3[u'建筑面积'])
print(f3.N())
print(f3.max())
f3.tabulate()
f3.plot()
f3.plot(5,cumulative=True)



