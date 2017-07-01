#coding:utf-8
# import theano
# from theano import tensor

# # declare two symbolic floating-point scalars
# a = tensor.dscalar()
# b = tensor.dscalar()

# # create a simple expression
# c = a + b

# # convert the expression into a callable object that takes (a,b)
# # values as input and computes a value for c
# f = theano.function([a,b], c)

# # bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
# assert 4.0 == f(1.5, 2.5)

# import numpy as np
# import theano
# import theano.tensor as T
# from theano import function
# from theano.ifelse import ifelse

# w=T.vector('w')
# x=T.vector('x')
# b=T.vector('b')
# # w = theano.shared(np.array([1,1]))
# # b = theano.shared(-1.5)
# z=T.dot(w, x)+b
# a=ifelse(T.lt(z,0), 0,1)
# neuron=function([w,x,b],a)

# inputs = [[0, 0],[0, 1],[1, 0],[1, 1]]
# weights = [1,1]
# bias = -1.5
# for i in range(len(inputs)):
# 	t = inputs[i]
# 	out = neuron(t,weights,bias)
# 	print 'The output for x1=%d | x2=%d is %d' % (t[0],t[1],out)

#单层
# import theano
# import theano.tensor as T
# from theano.ifelse import ifelse
# import numpy as np
# from random import random
# x=T.matrix('x')
# w=theano.shared(np.array([random(),random()]))
# b=theano.shared(1.)
# learning_rate=0.01

# z=T.dot(x,w)+b
# a=1/(1+T.exp(-z))

# a_hat = T.vector('a_hat') #Actual output
# cost = -(a_hat*T.log(a) + (1-a_hat)*T.log(1-a)).sum()
# dw,db = T.grad(cost,[w,b])

# train = theano.function(   
#     inputs = [x,a_hat],
#     outputs = [a,cost],
#     updates = [
#         [w, w-learning_rate*dw],
#         [b, b-learning_rate*db]
#     ]
# )
# inputs = [
#     [0, 0],
#     [0, 1],
#     [1, 0],
#     [1, 1]
# ]
# outputs = [0,0,0,1]
# cost = []
# for iteration in range(30000):
#     pred, cost_iter = train(inputs, outputs)
#     cost.append(cost_iter)
# print 'The outputs of the NN are:'
# for i in range(len(inputs)):
#     print 'The output for x1=%d | x2=%d is %.2f' % (inputs[i][0],inputs[i][1],pred[i])
# print '\nThe flow of cost during model run is as following:'
# import matplotlib.pyplot as plt
# plt.plot(cost)
# plt.show()

#双层
import theano
import theano.tensor as T
from theano.ifelse import ifelse
import numpy as np
from random import random

x=T.matrix('x')
w1=theano.shared(np.array([random(),random()]))
w2=theano.shared(np.array([random(),random()]))
w3=theano.shared(np.array([random(),random()]))
b1=theano.shared(1.)
b2=theano.shared(1.)
learning_rate=0.01

a1=1/(1+T.exp(-T.dot(x, w1)-b1))
a2=1/(1+T.exp(-T.dot(x, w2)-b1))
x2=T.stack([a1,a2],axis=1)
a3=1/(1+T.exp(-T.dot(a1, a2)-b2))


a_hat=T.vector('a_hat')
cost=-(a_hat*T.log(a3)+(1-a_hat)*T.log(1-a3)).sum()
dw1,dw2,dw3,db1,db2=T.grad(cost,[w1,w2,w3,b1,b2])
train=theano.function(
	inputs=[x,a_hat],
	outputs=[a3,a_hat],
	updates=[[w1,w1-learning_rate*dw1],
	[w2,w2-learning_rate*dw2],
	[w3,w3-learning_rate*dw3],
	[b1,b1-learning_rate*b1],
	[b2,b2-learning_rate*b2]
	]
)
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
outputs = [1,0,0,1]
cost = []
for iteration in range(30000):
    pred, cost_iter = train(inputs, outputs)
    cost.append(cost_iter)
print 'The outputs of the NN are:'
for i in range(len(inputs)):
    print 'The output for x1=%d | x2=%d is %.2f' % (inputs[i][0],inputs[i][1],pred[i])
    print '\nThe flow of cost during model run is as following:'
import matplotlib.pyplot as plt
plt.plot(cost)
plt.show()

# x=T.dscalar('x')
# y=T.dscalar('y')
# X=T.dmatrix('X')
# Y=T.dmatrix('Y')

# a=T.vector()
# b=T.vector()
# out=a**2+b**2+2*a*b
# f=function([a,b],out)
# print(f([1,2],[4,5]))

# f=function([x,y],x+y)
# F=function([X,Y],X+Y)
# print(f(2,3))
# print(F([[1,2],[3,4]],[[10,20],[30,40]]))
# print(type(x))
# print(out([0,1,2]))
# print numpy.allclose(f(16.3,12.1), 28.4)

