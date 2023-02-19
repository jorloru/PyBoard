# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

__all__ = 'SetValueMove', 'MovePieceMove'

class SetValueMove():
    
    def __init__(self, row, col, value):
        
        self.Row    = row
        self.Column = col
        self.Value  = value
        
class MovePieceMove():
    
    def __init__(self, row_origin, col_origin, row_target, col_target):
        
        self.RowOrigin    = row_origin
        self.ColumnOrigin = col_origin
        self.RowTarget    = row_target
        self.ColTarget    = col_target