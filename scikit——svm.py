#coding=utf-8
from sklearn.svm import SVC
from sklearn.svm import NuSVC
from sklearn.svm import LinearSVC
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt
# X=np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
# y=np.array([1,1,2,2])

# clf=SVC()
# clf1=NuSVC()
# print(clf.fit(X,y))
# print(clf1.fit(X,y))
# print(clf.predict([[-0.8,-1]]))
# print(clf1.predict([[-0.8,-1]]))
# clf = LinearSVC()
# clf.fit(X, y) 
# print(clf.fit(X,y))
# print(clf.predict([[-0.8, -1]]))

 # X=[[0],[1],[2],[3]] 
 # Y = [0,1,2,3] 
 # clf = SVC(decision_function_shape='ovo') 
 # #ovo为一对一 
 # clf.fit(X,Y) 
 # print clf.fit(X,Y) 
 # dec = clf.decision_function([[1]]) 
 # #返回的是样本距离超平面的距离 
 # print dec clf.decision_function_shape = "ovr" 
 # dec =clf.decision_function([1]) 
 # #返回的是样本距离超平面的距离 
 # print dec 
 # #预测 
 # print clf.predict([1])

#多类别分类：直接法  间接法（一对多，一对一，层次SVM，其他）
#SVC NuSVC采样一对一
 
# X=[[0],[1],[2],[3]]
# Y = [0,1,2,3]
# clf = SVC(decision_function_shape='ovo') #ovo为一对一
# clf.fit(X,Y)
# print "SVC:",clf.fit(X,Y)
# dec = clf.decision_function([[1]])    #返回的是样本距离超平面的距离
# print "SVC:",dec
# clf.decision_function_shape = "ovr"
# dec =clf.decision_function([1]) #返回的是样本距离超平面的距离
# print "SVC:",dec
# #预测
# print "预测：",clf.predict([1])
# lin_clf = LinearSVC()
# lin_clf.fit(X, Y) 
# dec = lin_clf.decision_function([[1]])
# print dec.shape[1]

#数据不平衡问题
from sklearn.linear_model import SGDClassifier
#we create 40 separable points
rng = np.random.RandomState(0)
n_samples_1 = 1000
n_samples_2 = 100
X = np.r_[1.5 * rng.randn(n_samples_1, 2),0.5 * rng.randn(n_samples_2, 2) + [2, 2]]
y = [0] * (n_samples_1) + [1] * (n_samples_2)
# print X
# print y
# fit the model and get the separating hyperplane
clf =SVC(kernel='linear', C=1.0)
clf.fit(X, y)
w = clf.coef_[0]
print w
a = -w[0] / w[1]      #a可以理解为斜率
xx = np.linspace(-5, 5)
yy = a * xx - clf.intercept_[0] / w[1]    #二维坐标下的直线方程
# get the separating hyperplane using weighted classes
wclf =SVC(kernel='linear', class_weight={1: 10})
wclf.fit(X, y)
ww = wclf.coef_[0]
wa = -ww[0] / ww[1]
wyy = wa * xx - wclf.intercept_[0] / ww[1]   #带权重的直线
# plot separating hyperplanes and samples
h0 = plt.plot(xx, yy, 'k-', label='no weights')
h1 = plt.plot(xx, wyy, 'k--', label='with weights')
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.legend()
plt.axis('tight')
plt.show()
# #支持向量回归
# X = [[0, 0], [2, 2]]
# y = [0.5, 2.5]
# clf=SVR()
# print clf.fit(X, y)
# print clf.predict([[1, 1]])
# #小例子#
# #数据准备
# X = np.sort(5 * np.random.rand(40, 1), axis=0)  #产生40组数据，每组一个数据，axis=0决定按列排列，=1表示行排列
# y = np.sin(X).ravel()   #np.sin()输出的是列，和X对应，ravel表示转换成行
# # Add noise to targets
# y[::5] += 3 * (0.5 - np.random.rand(8))
# # Fit regression model
# svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
# svr_lin = SVR(kernel='linear', C=1e3)
# svr_poly = SVR(kernel='poly', C=1e3, degree=2)
# y_rbf = svr_rbf.fit(X, y).predict(X)
# y_lin = svr_lin.fit(X, y).predict(X)
# y_poly = svr_poly.fit(X, y).predict(X)
# # look at the results
# lw = 2
# plt.scatter(X, y, color='darkorange', label='data')
# plt.hold('on')
# plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
# plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
# plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
# plt.xlabel('data')
# plt.ylabel('target')
# plt.title('Support Vector Regression')
# plt.legend()
# plt.show()
