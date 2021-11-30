import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[2,4,6,8,10,12,14]

plt.scatter(x,y)
plt.show()

n=len(y)
costapp=[]
def hypo(theta1,x):
    hyp=theta1*x
    return hyp

def cost(theta1,y,x):
    cost=(pow((hypo(theta1,x)-y),2))/(2*n)
    costapp.append(cost)
    # print((hypo(theta1,x),cost))
    return cost

def gradient(theta1,x,y):
    gradient=(1/n) * cost(theta1,y,x)*x
    return gradient
def costcalc(theta,x,y,n):
    cost=0
    for i in range(n):
        cost+=(pow((hypo(theta,x[i])-y[i]),2))
    return cost/(2*n)    

weights=[]    
theta1=5
# print(theta1)
sumgrad=0  
nsumgrad=1
# ntheta=0
learning_rate=0.01
iters=0
while (abs(nsumgrad-sumgrad)>0.1):
# for z in range(19):
    iters+=1
    # print("ll")
    nsumgrad=sumgrad
    i=0
    for i in range(len(x)):
        sumgrad+=gradient(theta1,x[i],y[i])
        
    if(abs(nsumgrad-sumgrad)<0.9):
        theta1=theta1
        break
    # print(sumgrad)  
    else:  
        theta1=theta1-(learning_rate*sumgrad)
    weights.append(theta1)    
    print(theta1)
    
    # ntheta1=theta1
# print(iters)
fcost=[]
# print(theta1)
# print(weights)
# print(costapp)
for i in range(len(weights)):
    temp=costcalc(weights[i],x,y,len(x))
    # print(temp)
    fcost.append(temp)
# print(fcost)
# plt.scatter(cost,)
plt.scatter(np.arange(1,len(weights)+1),fcost)
plt.show()
plt.scatter(weights,fcost)
plt.show()

#final Fit
# plt.scatter(x,y)
# plt.show()
y_pred=[]
for j in range(len(x)):
    y_pred.append(theta1*x[j])
# print(y_pred)  
plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()  

# plt.plot(x,())