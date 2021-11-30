# # import numpy as np
# # import matplotlib.pyplot as plt
# # X=np.vstack(([0,0],[0,1],[1,0],[1,1]))
# # t=np.array([0,1,1,0]).reshape(-1,1)
# # alpha=1
# # W1=np.random.rand(2,16)
# # W2=np.random.rand(16,1)
# # def sigmoid(x):
# #   return (1/(1+np.exp(-x)))
# # Loss=[]
# # for i in range(10000):
# #   z=sigmoid(np.dot(X,W1))
# #   y=sigmoid(np.dot(z,W2))
# #   loss=1/4*np.sum((y-t)**2)
# #   grad_W2=2*(np.dot(y.T,(y-t)*y*(1-y)))
# #   grad_W1=2*np.dot(X.T,np.dot((y-t)*y*(1-y),W2.T)*z*(1-z))
# #   W2=W2-alpha*grad_W2
# #   W1=W1-alpha*grad_W1
# #   Loss.append(loss)
# # print(W2)  
# # print(W1)  
# import numpy as np
# import matplotlib.pyplot as plt
# def sigmoid(x):
#   return 1/(1+np.exp(-x))
# def sigmoid_der(x):
#   return sigmoid(x)*(1-sigmoid(x))
# def forward(x,w1,w2,predict=False):
#   a1=np.matmul(x,w1)
#   z1=sigmoid(a1)
#   bias=np.ones((len(z1),1))
#   z1=np.concatenate((bias,z1),axis=1)
#   a2=np.matmul(z1,w2)
#   z2=sigmoid(a2)
#   if predict:
#     return z2
#   return a1,z1,a2,z2

# def backprop(a2,z0,z1,z2,y):
#   delta2=z2-y
#   Delta2=np.matmul(z1.T,delta2)
#   Delta1=(delta2.dot(w2[1:,:].T))*sigmoid_der(a1)
#   return delta2,Delta1,Delta2

# X=np.array([[1,0],[1,1],[0,0],[1,0]])
# y=np.array([[1],[1],[0],[0]])

# w1=np.random.randn(2,5)
# w2=np.random.randn(6,1)

# lr=0.09
# costs=[]
# epochs=15000
# m=len(X)
# for i in range(epochs):
#   a1,z1,a2,z2=forward(X,w1,w2)
#   (delta2,Delta1,Delta2)=backprop(a2,X,z1,z2,y)
#   # print(Delta1)
#   w1-=(lr*(1/m))*Delta1
#   w2-=(lr*(1/m))*Delta2
#   c=np.mean(np.abs(delta2))
#   costs.append(c)
#   if i%1000 ==0:
#     print(f"iteration:{i}.error :{c}")
# print("train comp")    
# z3=forward(X,w1,w2,True)
# print("percentages: ")
# print(z3)
# print("predictions: ")

import numpy as np
X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=np.array([[0,1,1,0]]).T
print("Input")
print(X)
print("\nOutput")
print(Y)
m=X.shape[0] 
n=X.shape[1] 
hidden_s = 4 
l_r = 1 
theta1 = (np.random.random((n + 1, hidden_s)))
theta2 = (np.random.random((hidden_s + 1, 1)))

def sigmoid(z):
    
    return 1/(1+np.exp(-z))

def sigmoid_grad(z):
    
    s=sigmoid(z)
    return s*(1-s)    
def forward_propagate(X,theta1,theta2):
    
    a1=np.c_[np.ones(X.shape[0]),X]
    z1=a1.dot(theta1)
    a2=np.c_[np.ones(X.shape[0]),sigmoid(z1)]
    z3=a2.dot(theta2)
    
    h3=sigmoid(z3)

    return a1,z1,a2,z3,h3    
for i in range(1000):
    a1, z1, a2, z3, hyp = forward_propagate(X, theta1, theta2)
    del_2= Y-hyp
    del_1=del_2.dot(theta2[1:,:].T)

    delta2=del_2
    
    delta1=del_1*sigmoid_grad(z1)

    theta2+=l_r*a2.T.dot(delta2)
    theta1+=l_r*a1.T.dot(delta1)
a1, z1, a2, z3, hyp = forward_propagate(X, theta1, theta2)
print("\nPredicted Output")
print(hyp)