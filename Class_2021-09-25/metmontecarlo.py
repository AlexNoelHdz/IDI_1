import numpy as np

N=100000

x=np.random.random((N,2))
y=sum(np.sum(x**2,1)<=1)
mi_pi=y/N*4

gano=0
for _ in range(N):
    tiro=sum(np.random.randint(1,7,2))
    if tiro in [7,11]:
        gano+=1
    elif not tiro in [2,3,12]:
        tiro2=-1
        while not tiro2 in [7,tiro]:
            tiro2=sum(np.random.randint(1,7,2))
        if tiro2==tiro:
            gano+=1
            
            
I=(4-1)*np.mean(np.random.uniform(1,4,N)**2)




    

