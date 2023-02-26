# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

from pyboard import TurnBasedConfig, SetValueMove

__all__ = 'TicTacToeConfig',

class TicTacToeConfig(TurnBasedConfig):
    
    def __init__(self, firstPlayer=1):
        
        if type(firstPlayer) != int:
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'firstPlayer' to be",
                                      str(int),
                                      "but got",
                                      str(type(firstPlayer))]))
            
        elif firstPlayer not in (1,2):
            
            raise ValueError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'firstPlayer' to be one of",
                                      str([1,2]),
                                      "but got",
                                      str(firstPlayer)]))
        
        super().__init__(rows=3, cols=3, movetype=SetValueMove)
        self.FirstPlayer = firstPlayer