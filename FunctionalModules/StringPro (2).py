'''
Created on Nov 29, 2018

@author: Vedha
'''
class Pro:
    def getdet(self):
        a="derrick"
        b="rajasekar"
        print a.center(1);
        print a.find('e')
        print a.index('i')
        print a.__add__(b)
        print a.join("ra")
        print a.isspace()
        #print a.ljust(24,'e')
        print a.rjust(24,'d')
        print a.__sizeof__()
        print b.__sizeof__()
        print a.__ne__("raja")
        print b.__mul__(4)
        x=12
        y=13
        print x.__mod__(y)
        
        
if __name__=="__main__":
    ob=Pro()
    ob.getdet()
