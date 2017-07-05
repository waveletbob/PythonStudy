#coding=utf-8
import requests
import time
import json
from bs4 import BeautifulSoup
url="http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={page}&pagebar=0&pl_name=Pl_Official_MyProfileFeed__21&id=1005052428186595&script_uri=/u/2428186595&feed_type=0&pre_page={page}&domain_op=100505&__rnd=1490150266412"
cookies={"Cookie":"SINAGLOBAL=5920432319171.193.1486952382149; UM_distinctid=15ab7def7aa0-068901557cbdc8-64191279-15f900-15ab7def7ab262; login_sid_t=0ce0a1875ebfa185ffc420b2aac2eba2; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; YF-V5-G0=f7add382196ce7818cd5832b5a20aaf5; _s_tentry=www.hao123.com; UOR=baike.baidu.com,widget.weibo.com,www.hao123.com; Apache=9670189290251.395.1490146525934; ULV=1490146525939:19:10:1:9670189290251.395.1490146525934:1489720787780; YF-Page-G0=e1a5a1aae05361d646241e28c550f987; WBtopGlobal_register_version=ddc090d739748ab2; SCF=AodssSaS_d2q59NV8C3-VWq9yVYa9my45rAzI4g8KZZt-PigJ7lYvook0YuF-KNgZIcFjkgsgcfP66yDyIfLt98.; SUB=_2A2511ZEBDeRxGeVK6FsV9CrFyjyIHXVWooXJrDV8PUNbmtBeLWjVkW-UodDjAWJer3QsVO1x92DNSnwV5Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5mNYLQ82XAGNeB9yzU_smL5JpX5K2hUgL.FoeXe0.XShB4eK52dJLoI7DNqP9LdsHXqJvb; SUHB=0Yhhntb9gvYKOH; ALF=1490754517; SSOLoginState=1490149713; un=410015031@qq.com"}
#for i in range(8):
url=url.format(page=11)
r=requests.get(url,cookies=cookies)
Data=json.loads(r.text)
#print(type(Data))
htmlstr=Data['data']
bsobj=BeautifulSoup(htmlstr,"html.parser")
titles=bsobj.find_all('div',{'class':"WB_text W_f14"})
		#print(type(titles))
f=open(u"xx的微博.txt",'a')
for title in titles:
	f.write(title.get_text().encode("utf8"))
f.write('----------------------page1------------------\n')
f.close()
	
	