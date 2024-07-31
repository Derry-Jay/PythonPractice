"""
Created on Feb 7, 2019

@author: Vedha
"""
from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def get(self):
        pass
