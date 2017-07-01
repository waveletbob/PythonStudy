# import numpy as np
# from pylab import *
# X=np.linspace(-np.pi,np.pi,256,endpoint=True)
# cos,sin=np.cos(X),np.sin(X)
# plot(X,cos)
# plot(X,sin)
# show()

import numpy as np
from matplotlib import pyplot as plt
# print(np.__version__)
# np.show_config()

# X=np.array([1,2,3,4,5,6])
# np.save('outfile',X,allow_pickle=True)
# np.savetxt('out.txt',X)
# Y=np.load('outfile.npy')
# y=np.loadtxt('out.txt')
# print("%s|||%s"%(Y,y))

#x=np.arange(1,11)
#y=x*2+5
# x=np.arange(0,3*np.pi,0.1)
# y_sin=np.sin(x)
# y_cos=np.cos(x)
# plt.subplot(2,1,1)
# plt.title("Test")
# plt.xlabel("x")
# plt.ylabel("y_sin")
# plt.plot(x,y_sin,'b--x',label="sin")
# plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)  
# plt.subplot(2,1,2)
# plt.title("Test")
# plt.xlabel("x")
# plt.ylabel("y_cos")
# plt.plot(x,y_cos,'b--x',label="sin")
# plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)  
# plt.show()

# x = [5,8,10]
# y = [12,16,6]
# x2 = [6,9,11]
# y2 = [6,15,7]
# plt.bar(x, y, align = 'center')
# plt.bar(x2, y2, color = 'g', align = 'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()

# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# np.histogram(a,bins = [0,20,40,60,80,100])
# hist,bins = np.histogram(a,bins = [0,20,40,60,80,100])
# print hist
# print bins
# plt.hist(a, bins = [0,20,40,60,80,100])
# plt.title("histogram")
# plt.show()

# a=np.array([[1,2],[3,4]])
# b=np.array([[11,12],[13,14]])
# print(np.dot(a,b))
# print(np.vdot(a,b))
# print(np.inner(a,b))
# print(np.matmul(a,b))
# print(np.linalg.det(a))
# print(np.linalg.solve(a,b))
# print(np.linalg.inv(a))

# import numpy.matlib 
# print np.matlib.empty((2,2))
# print np.matlib.zeros((2,2))
# print np.matlib.ones((2,2))
# print np.matlib.eye(n=3,M=4,k=0,dtype=float)
# print np.matlib.identity(5,dtype=float)
# print np.matlib.rand(3,3)

# a=np.arange(6)
# b=a
# print(id(a))
# print(id(b))
# c=a.view()
# print(id(c))
# print(b is a)
# print(c is a)
# a1=np.array([[10,10],[2,3],[4,5]])
# s=a1[:,:2]
# print s
# b1=a1.copy()
# print (b1 is a1)

# a=np.array([1,256,8755])
# print(map(hex,a))
# print(a.byteswap(True))
# print(map(hex,a))

# a=np.array([[3,7],[9,1]])
# print(np.sort(a,axis=1,kind='heapsort'))
# dt=np.dtype([('name', 'S10'),('age', int)])
# b=np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27
# )], dtype = dt)
# print(np.sort(b,order='name'))
# x=np.array([3,1,2])
# y=np.argsort(x)
# print(x[y])
# for i in y:
# 	print x[i]
# nm = ('raju','anil','ravi','amar')
# dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
# ind = np.lexsort((dv,nm))
# print(ind)
# print [nm[i] + ", " + dv[i] for i in ind]

# a = np.array([[30,40,70],[80,20,10],[50,90,60]])
# print np.argmax(a)
# print a.flatten()
# print np.argmax(a, axis = 0)
# print np.argmax(a, axis = 1)
# print np.argmin(a)
# print a.flatten()[np.argmin(a)]
# print np.nonzero(a)
# print(np.where(a>80))
# print(a[np.where(a>80)])
# condition=np.mod(x,2)==0
# print np.extract(condition,[0,1,2,3,4,5,6])


# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.amin(a))
# print(np.amax(a,axis=0))
# print(np.ptp(a,axis=0))
# print(np.percentile(a,50,axis=0))
# print(np.median(a,axis=0))
# print(np.mean(a,axis=0))
# print(np.average(a))
# wts=np.array([[4,3,2],[3,4,5],[5,2,3]])
# print(np.average(a,weights=wts))
# print(np.average(a,weights=wts,returned=True))
# #std=sqrt(mean((x-x.mean())**2))
# print(np.std(a))
# print(np.var(a))

# a=np.arange(9,dtype=np.float_).reshape(3,3)
# b=np.array([10,10,10])
# print((np.add(a,b).tolist(),np.subtract(a,b).tolist(),np.multiply(a,b).tolist(),np.divide(a,b).tolist()))
# print(np.reciprocal(a))
# print(np.power(a,b))
# print(np.mod(a,2))
# c=np.array([-5.6j,0.2j,11.,1+1j])
# print(np.real(c))
# print(np.imag(c))
# print(np.conj(c))
# print(np.angle(c))

# a = np.array([0,30,45,60,90])
# print np.sin(a*np.pi/180)
# print np.cos(a*np.pi/180)
# print np.tan(a*np.pi/180)
# # inv = np.arcsin(sin)
# # inv = np.arccos(cos)
# # inv = np.arctan(tan)
# # print np.degrees(inv)
# print np.around(a, decimals = 1)
# print np.floor(a)
# print np.ceil(a)

# print np.char.add(['hello'],[' xyz'])
# print np.char.add(['hello', 'hi'],[' abc', ' xyz'])
# print np.char.multiply('Hello ',3)
# print np.char.center('hello', 20,fillchar = '*')
# print np.char.capitalize('hello world')
# print np.char.title('hello how are you?')
# print np.char.lower(['HELLO','WORLD'])
# print np.char.lower('HELLO')
# print np.char.upper('hello')
# print np.char.upper(['hello','world'])
# print np.char.split ('hello how are you?')
# print np.char.split ('TutorialsPoint,Hyderabad,Telangana', sep =
# ',')
# print np.char.splitlines('hello\nhow are you?')
# print np.char.splitlines('hello\rhow are you?')
# print np.char.strip('ashok arora','a')
# print np.char.strip(['arora','admin','java'],'a')
# print np.char.join(':','dmy')
# print np.char.join([':','-'],['dmy','ymd'])
# print np.char.replace ('He is a good boy', 'is', 'was')
# a = np.char.encode('hello', 'cp500')
# print a
# print np.char.decode(a,'cp500')

# a,b = 13,17
# print bin(a), bin(b)
# print np.bitwise_and(13, 17)
# print np.bitwise_or(13, 17)
# print np.invert(np.array([13], dtype = np.uint8))
# print np.binary_repr(13, width = 8)
# print np.binary_repr(242, width = 8)
# print np.left_shift(10,2)
# print np.binary_repr(10, width = 8)
# print np.binary_repr(40, width = 8)
# print np.right_shift(40,2)

# a = np.arange(8)
# b = a.reshape(4,2)
# print a.flat[5]
# print a.flatten(order = 'F')
# print a.ravel(order = 'F')
# print np.transpose(a)
# print a.T
# a = np.arange(8).reshape(2,2,2)
# print np.rollaxis(a,1,0)
# print np.swapaxes(a, 2, 0)


#修改维度
#1、broadcast 产生模仿广播的对象 ;2、broadcast_to 将数组广播到新形状;
#3、expand_dims 扩展数组的形状;4、squeeze 从数组的形状中删除单维条目
#数组的链接
# 1. concatenate 沿着现存的轴连接数据序列
# 2. stack 沿着新轴连接数组序列
# 3. hstack 水平堆叠序列中的数组（列方向）
# 4. vstack 竖直堆叠序列中的数组（行方向）

#数组分割
# 1. split 将一个数组分割为多个子数组
# 2. hsplit 将一个数组水平分割为多个子数组（按列）
# 3. vsplit 将一个数组竖直分割为多个子数组（按行）

#添加/删除元素
# 1. resize 返回指定形状的新数组
# 2. append 将值添加到数组末尾
# 3. insert 沿指定轴将值插入到指定下标之前
# 4. delete 返回删掉某个轴的子数组的新数组
# 5. unique 寻找数组内的唯一元素

#数组上的迭代numpy.nditer

#数组创建
empty zeros ones
#现有数组
asarray frombuffer fromiter 
#数值范围
arange linspace logspace

#切片 索引
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]]
print y
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 1
0, 11]])
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print y
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 1
0, 11]])
z = x[1:4,1:3]
y = x[1:4,[1,2]]
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 1
0, 11]])
print x[x > 5]
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print a[~np.isnan(a)]
a = np.array([1, 2+6j, 5, 3.5+5j])
print a[np.iscomplex(a)]

#广播
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print c

