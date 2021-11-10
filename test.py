import numpy as np

import pandas as pd
train_d=pd.read_csv("/home/shivanand/Documents/train.csv")
test_d=pd.read_csv("/home/shivanand/Documents/test.csv")

x_train = train_d['x']
y_train = train_d['y']
x_test = train_d['x']
y_test = train_d['y']

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)
# print(y_train)
x_train1 = x_train.reshape(-1,1)
# print(x_train1)
y_train1=y_train.reshape(-1,1)
x_test1 = x_test.reshape(-1,1)
n=700
alpha=0.0001
a_0=np.zeros((n,1),dtype='i')
a_1=np.zeros((n,1),dtype='i')
# print(a_1)
ep=0
while(ep<100):
    print(a_1)
    # break
    # print()
    y=(a_1[0]*x_train1)
    # print(y)
    errr=abs(y-y_train)
    x=errr**2
    # print(x)
    mse=np.sum(x)
    # print(mse)
    mse_f=mse/n
    # a_0=a_0-alpha*2*np.sum(errr)/n
    a_1=a_1-alpha*2*(np.sum(errr)*x_train)/n
    ep+=1
    # if (ep%10)==0:
    # print(a_1)

# print(a_1)