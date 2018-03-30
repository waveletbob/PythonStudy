#coding:utf-8
import pickle
import json
d=dict(name='bob',age=20,score=88)
pickle.dumps(d)
with open('dump.txt','wb') as f:
	pickle.dump(d,f)
with open('dump.txt','rb')as f:
	d1=pickle.load(f)
print(type(d1))
d2=json.dumps(d1)
print(json.loads(d2))

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
s=Student('bob', 12, 68)
json.dumps(s,default=student2dict)
json.dumps(s, default=lambda obj: obj.__dict__)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str, object_hook=dict2student)





