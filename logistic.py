#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
#pyplot与pylab的区别在于pylab常用于ipython交互式环境
from scipy.optimize import minimize
from sklearn.preprocessing import PolynomialFeatures
def sigmoid(z):
	return 1/(1+np.exp(-z))
def costFunc(theta,X,y):
	m=y.size
	h=sigmoid(X.dot(theta))
	J =-1.0*(1.0/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))	
	if np.isnan(J[0]):
		return(np.inf)
	return J[0]
def grad(theta,X,y):
	m=y.size
	h=sigmoid(X.dot(theta.reshape(-1,1)))
	grad=(1.0/m)*X.T.dot(h-y)
	return(grad.flatten())
def prediction(theta,X,threshold=0.5):
	p=sigmoid(X.dot(theta.T))>=threshold
	return(p.astype('int'))
def plotData(data, label_x, label_y, label_pos, label_neg, axes=None):
    # 获得正负样本的下标(即哪些是正样本，哪些是负样本)
    neg = data[:,2] == 0
    pos = data[:,2] == 1
    
    if axes == None:
        axes = plt.gca()
    axes.scatter(data[pos][:,0], data[pos][:,1], marker='+', c='k', s=60, linewidth=2, label=label_pos)
    axes.scatter(data[neg][:,0], data[neg][:,1], c='y', s=60, label=label_neg)
    axes.set_xlabel(label_x)
    axes.set_ylabel(label_y)
    axes.legend(frameon= True, fancybox = True)
data=np.loadtxt(u'D:\BaiduNetdiskDownload\ML-examples-master\ML-examples-master\logistic_regression\data1.txt',delimiter=',')
# #print(data[0])
# X=data[:,0:2]
# # print X
# y=data[:,2] 
# # print y

#可以写一个函数集成
# pos=np.where(y==1)
# neg=np.where(y==0)
# plt.scatter(X[pos,0],X[pos,1],marker='o',c='b')
# plt.scatter(X[neg,0],X[neg,1],marker='x',c='r')
# plt.xlabel('Feature1/Exam 1 score')  
# plt.ylabel('Feature2/Exam 2 score')  
# plt.legend(['Fail', 'Pass'])  
# plt.show()  

X = np.c_[np.ones((data.shape[0],1)), data[:,0:2]]
# print X.shape
y = np.c_[data[:,2]]
# print y
init_theta=np.zeros(X.shape[1])
cost=costFunc(init_theta,X,y)
gradient=grad(init_theta,X,y)
# print cost
# print gradient
result=minimize(costFunc,init_theta,args=(X,y),jac=grad,options={'maxiter':400})
print result
print sigmoid(np.array([1,45,85]).dot(result.x.T))

plt.scatter(45, 85, s=60, c='r', marker='v', label='(45, 85)')
plotData(data, 'Exam 1 score', 'Exam 2 score', 'Admitted', 'Not admitted')
x1_min, x1_max = X[:,1].min(), X[:,1].max(),
x2_min, x2_max = X[:,2].min(), X[:,2].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
h =	sigmoid(np.c_[np.ones((xx1.ravel().shape[0],1)), xx1.ravel(), xx2.ravel()].dot(result.x))
h = h.reshape(xx1.shape)
plt.contour(xx1, xx2, h, [0.5], linewidths=1, colors='b')
plt.show()
plt.close()


data2=np.loadtxt(u'D:\BaiduNetdiskDownload\ML-examples-master\ML-examples-master\logistic_regression\data2.txt',delimiter=',')
# X1=data2[:0:2]
y1=np.c_[data2[:,2]]
# plotData(data2,'Microchip Test 1', 'Microchip Test 2', 'y = 1', 'y = 0')
# plt.show()

poly=PolynomialFeatures(6)
X1=poly.fit_transform(data2[:,0:2])
# print X1.shape

def costFuncReg(w,reg,*args):
	m=y1.size
	h=sigmoid(X1.dot(w))
	J=-1.0*(1.0/m)*(np.log(h).T.dot(y1)+np.log(1-h).T.dot(1-y1))+(reg/(2.0*m))*np.sum(np.square(w[1:]))
	if np.isnan(J[0]):
		return(np.inf)
	return J[0]
def gradReg(w,reg,*args):
	m=y1.size
	h=sigmoid(X1.dot(w.reshape(-1,1)))
	gradient=(1.0/m)*X1.T.dot(h-y1)+(reg/m)*np.r_[[[0]],w[1:].reshape(-1,1)]
	return(gradient.flatten())
init_w=np.zeros(X1.shape[1])
# print costFuncReg(init_w,1,X1,y1)
fig,axes=plt.subplots(1,3,sharey=True,figsize=(17,5))
#Lambda=0,1,100
for i,C in enumerate([0.0,1.0,100.0]):
	result2=minimize(costFuncReg,init_w,args=(C,X1,y1),jac=gradReg,options={'maxiter':3000})

	accuracy=100.0*sum(prediction(result2.x,X1)==y1.ravel())/y1.size

	plotData(data2, 'Microchip Test 1', 'Microchip Test 2', 'y = 1', 'y = 0', axes.flatten()[i])

	# 画出决策边界
	x1_min, x1_max = X[:,0].min(), X[:,0].max()
	x2_min, x2_max = X[:,1].min(), X[:,1].max()
	xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
	h = sigmoid(poly.fit_transform(np.c_[xx1.ravel(), xx2.ravel()]).dot(result2.x))
	h = h.reshape(xx1.shape)
	axes.flatten()[i].contour(xx1, xx2, h, [0.5], linewidths=1, colors='g')
	axes.flatten()[i].set_title('Train accuracy {}% with Lambda = {}'.format(np.round(accuracy, decimals=2), C))
plt.show()





