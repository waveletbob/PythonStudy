#coding:utf-8
with open('path','wrb') as f:
	print(f.read())
	print(f.read(1024))
	print(f.readlines())
	print(f.readline())