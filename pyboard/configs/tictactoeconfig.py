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
        
        super().__init__(rows=3, cols=3, movetype=SetValueMove)
        self.FirstPlayer = firstPlayer
        
    def check(self):
        
        if self.FirstPlayer in (1,2):
            
            return True
        
        else:
            
            return False