'''
Created on Nov 30, 2018
@author: Vedha
'''
def isArms(b):
    s=f=d=0
    a=b
    while(a!=0):
        d=a%10
        s+=pow(d,3)
        a/=10
    if(s==b):
        f=1
    return f
l=int(input('Enter Limit:'))
for j in range(1,l+1):
    if(isArms(j)):
        print (j)