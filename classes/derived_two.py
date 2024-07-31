"""
Created on Dec 18, 2018

    @author: Vedha
"""
from classes.base import Base


class DerivedTwo(Base):
    def get(self):
        print("Hi")
