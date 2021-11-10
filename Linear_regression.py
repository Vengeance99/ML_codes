import numpy as np
import pandas as pd
train_d=pd.read_csv("/home/shivanand/Documents/train.csv")
test_d=pd.read_csv("/home/shivanand/Documents/test.csv")
# print(train_d)
x_train=train_d['x']
y_train=train_d['y']
x_test=test_d['x']
y_test=test_d['y']
x_train=np.array([x_train])
y_train=np.array([y_train])
x_test=np.array([x_test])
y_test=np.array([y_test])

# print(x_train)
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)
n=700
alpha=0.0001
a_0=np.zeros((n,1))
a_1=np.zeros((n,1))
ep=0
while(ep<1000):
    y=a_0+a_1*x_train
    errr=y-y_train
    mse=np.sum(errr**2)
    mse_f=mse/n
    a_0=a_0-alpha*2*np.sum(errr)/n
    a_1=a_1-alpha*2*(np.sum(errr)*x_train)/n
    ep+=1
    if (ep%10)==0:
        print(mse)



