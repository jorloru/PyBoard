# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

__all__ = 'TurnBasedMove',

class TurnBasedMove():
    
    def __init__(self, row, col, value):
        
        self.Row    = row
        self.Column = col
        self.Value  = value