# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

from abc import ABC, abstractmethod

__all__ = 'TurnBasedConfig',

class TurnBasedConfig(ABC):
    
    def __init__(self, rows, cols, movetype):
        
        self.Rows = rows
        self.Columns = cols
        self.MoveType = movetype
        
        super().__init__()
    
    @abstractmethod
    def check(self):
        
        pass