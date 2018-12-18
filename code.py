import numpy as np
import matplotlib.pyplot as plt
length = int(input("Enter the length of the signal(Recomended above 200): "))
iterations = int(input("Enter the number of iterations:(Recomended above 200): "))

A = .5
l0 = []
l = []
l1 = []
l2 = []
c1 = 0
c2 = 0
for i in range(1,length+1):
    for j in range(0,i):
        c1 = c1 + np.random.normal(A, 1, None) 
        c2 = c2 + np.random.normal(0, 1, None)
    l1.append(float(c1)/i)
    l2.append(float(c2)/i)
    l.append(i)
    l0.append(A/2)
    c1 = 0
    c2 = 0
plt.figure(0)
plt.plot(l,l1,'r--')
plt.plot(l,l2,'g--')
plt.plot(l,l0,'b--')
plt.xlabel('Number of Samples,N',fontsize=12)
plt.ylabel('Sample mean',fontsize=12)
plt.grid(True)
plt.axis([0,length,-1,1.5])
plt.text(float(length)/3,.75,'signal plus noise', color = 'red',fontsize=12,fontweight = 'bold')
plt.text(float(length)/3,-.35,'only noise',color = 'green',fontsize=12,fontweight = 'bold')
plt.title('Sample mean Vs Number of samples',fontweight = 'bold', fontsize = 14)

total = 0
acc = 0
l3 = []
l4 = []

s = 0
for i in range(1,length):
    for j in range(0,iterations):
        for k in range(0,i):
            s = s + np.random.normal(A, 1, None) 
        if float(s)/i>A/2:
            total = total + 1
        s = 0
    acc = (float(total)/iterations)*100
  
    
    l3.append(acc)
    l4.append(i)
    acc = 0
    total = 0

plt.figure(1)
plt.plot(l4,l3,'r')
plt.xlabel('Number of samples',fontsize=12)
plt.ylabel('Accuracy(in %)')
plt.title('Accuracy Vs Number of samples',fontweight = 'bold', fontsize = 14)
plt.grid(True)
plt.axis([0,length,min(l3),105])
plt.text(length/3,80,'No. of iterations: '+str(iterations),color = 'red',fontsize=12,fontweight = 'bold')
plt.show()    
    
        

