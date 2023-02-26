# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

__all__ = 'SetValueMove', 'MovePieceMove'

class SetValueMove():
    
    def __init__(self, row, col, value):
        
        if type(row) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'row' to be",
                                      str(int),
                                      "but got",
                                      str(type(row))]))
        
        if type(col) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'col' to be",
                                      str(int),
                                      "but got",
                                      str(type(col))]))
        
        if type(value) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'value' to be",
                                      str(int),
                                      "but got",
                                      str(type(value))]))
        
        self.Row    = row
        self.Column = col
        self.Value  = value
        
class MovePieceMove():
    
    def __init__(self, row_origin, col_origin, row_target, col_target):
        
        if type(row_origin) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'row_origin' to be",
                                      str(int),
                                      "but got",
                                      str(type(row_origin))]))
        
        if type(col_origin) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'col_origin' to be",
                                      str(int),
                                      "but got",
                                      str(type(col_origin))]))
        
        if type(row_target) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'row_target' to be",
                                      str(int),
                                      "but got",
                                      str(type(row_target))]))
        
        if type(col_target) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'col_target' to be",
                                      str(int),
                                      "but got",
                                      str(type(col_target))]))
        
        self.RowOrigin    = row_origin
        self.ColumnOrigin = col_origin
        self.RowTarget    = row_target
        self.ColTarget    = col_target