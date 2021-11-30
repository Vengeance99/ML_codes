import numpy as np
x=np.array([[1,2,3]])
y=np.transpose([[4,5,6]])   
c=299792458

def main(mob_add):
    mob_add(x,y,c)
@main
def mob_add(x,y,c):
    # x=np.array([[1,2,3]])
    # y=np.transpose([[4,5,6]])
    # c=299792458
    a=np.matmul((1+2*c*(x.dot(y))+c*((np.linalg.norm(y))**2)),x)
    b=(1-c*(np.linalg.norm(y))**2)*y
    d=1+(2*c*x.dot(y))+(((c**2)*(np.linalg.norm(x))**2)*(np.linalg.norm(y))**2)
    mbstemp=np.add(a,b)
    x_mbsa_y=np.divide(mbstemp,d)
    print(x_mbsa_y)

