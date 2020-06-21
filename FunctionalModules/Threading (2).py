'''
Created on Dec 5, 2018

@author: Vedha
'''
from threading import Thread
import time
l=input('Enter Limit')
class Thread1(Thread):
    def run(self):
        for i in range(l):
            time.sleep(i)
            print Thread.getName(self),Thread.is_alive(self),i
            
class Thread2(Thread):
    def run(self):
        for i in range(l):
            time.sleep(i)
            print Thread.getName(self),Thread.is_alive(self),i**2
                        
class Thread3(Thread):
    def run(self):
        for i in range(l):
            time.sleep(i)
            print Thread.getName(self),Thread.is_alive(self),i**3
if __name__=="__main__":
    t3=Thread3()
    t2=Thread2()
    t1=Thread1()
    t1.start()
    t2.start()
    t3.start()
    