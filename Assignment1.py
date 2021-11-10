import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Reading .xlsx file as a DataFrame
df=pd.read_excel('/home/shivanand/Downloads/Activity_1_Data.xlsx') 
print(df)

#plotting initial data from .xlsx file

df.plot.scatter(x = 'x', y = 'y',facecolors='black', s = 50)
plt.scatter(0, 0, color="black")
plt.show()

#finding new position of base statio such that max customers are covered

tempx=[i for i in df['x']]
tempy=[j for j in df['y']]
def newpos(tempx,tempy):
    newx=sum(tempx)/len(tempx)
    newy=sum(tempy)/len(tempy)
    return newx,newy
newx,newy=newpos(tempx,tempy)    

#plotting new base station   
df.plot.scatter(x = 'x', y = 'y',facecolors='black', s = 50)
plt.scatter(newx, newy, color="black")
plt.show()

#getting data of retained and transfered customers
def calculate(df):
    import math
    retx=[]
    rety=[]
    transx=[]
    transy=[]
    retidx=[]
    transidx=[]
    for idx,(i,j) in enumerate(zip(df['x'],df['y'])):
    # print(i,j,newx)
        if (math.sqrt(pow((i-newx),2)+pow((j-newy),2)) <=2):
            retidx.append(idx+1)
            retx.append(i)
            rety.append(j)
        else:
            transidx.append(idx+1)
            transx.append(i)
            transy.append(j)  
    print(transidx)
    print(len(retx),len(rety))    
    print(len(transx),len(transy))
    return (retidx,retx,rety,transidx,transx,transy)
(retidx,retx,rety,transidx,transx,transy)=calculate(df)     

#creating separate dataframes for retained and transfered customers
retcus={'idx':retidx,'x':retx,'y':rety}
trans={'idx':transidx,'x':transx,'y':transy}
nretdf=pd.DataFrame(retcus)
transdf=pd.DataFrame(trans)

#writing to .xlsx file for retained customers
writer =pd.ExcelWriter('/home/shivanand/Documents/ML_codes/Activity1-Retain.xlsx',engine='xlsxwriter')
nretdf.to_excel(writer,sheet_name='Activity1-Retain.xlsx',index=False)
writer.save()

#writing to .xlsx file for transfered customers
twriter =pd.ExcelWriter('/home/shivanand/Documents/ML_codes/Activity1-Transfer.xlsx',engine='xlsxwriter')
transdf.to_excel(twriter,sheet_name='Activity1-Transfer.xlsx',index=False)
twriter.save()