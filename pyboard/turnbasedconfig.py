# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..'))

from abc import ABC, abstractmethod
from pyboard import SetValueMove, MovePieceMove

__all__ = 'TurnBasedConfig',

class TurnBasedConfig(ABC):
    
    def __init__(self, rows, cols, movetype):
        
        if type(rows) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'rows' to be",
                                      str(int),
                                      "but got",
                                      str(type(rows))]))
        
        if type(cols) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'cols' to be",
                                      str(int),
                                      "but got",
                                      str(type(cols))]))
            
        if movetype not in (SetValueMove, MovePieceMove):
            
            raise ValueError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'movetype' to be one of",
                                      str([SetValueMove, MovePieceMove]),
                                      "but got",
                                      str(movetype)]))
        
        self.Rows = rows
        self.Columns = cols
        self.MoveType = movetype
        
        super().__init__()