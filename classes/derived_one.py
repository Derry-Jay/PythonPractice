"""
Created on Dec 19, 2018

@author: Vedha
"""
from classes.base import Base


class DerivedOne(Base):
    def get(self):
        print("Hello")
