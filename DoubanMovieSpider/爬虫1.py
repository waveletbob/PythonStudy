import urllib
import urllib2
url="http://www.baidu.com"
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values={'name' : 'WHY',    
		'location' : 'SDU',    
		'language' : 'Python'
}
data=urllib.urlencode(values)
headers={ 'User-Agent' : user_agent }  
request=urllib2.Request(url,data,headers)
# response=urllib2.urlopen(url)
response=urllib2.urlopen(request)
htmlstr=response.read()
print htmlstr