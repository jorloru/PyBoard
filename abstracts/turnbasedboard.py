# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

from abc import ABC, abstractmethod
import numpy as np

__all__ = 'TurnBasedBoard', 'TurnBasedStatus',

class TurnBasedStatus():
    
    def __init__(self):
        
        self.Finished = False
        self.Winner = 0
        self.Turn = 1
        self.PlayerTurn = 1

class TurnBasedBoard(ABC):
    
    def __init__(self, config):
        
        self.Config = config
        self.Board  = np.zeros((config.Rows, config.Columns), int)
        self.Status = TurnBasedStatus()
        
        super().__init__()
        
    def update_tile(self, row, col, value):
        
        if self._check_valid_move(row, col, value):
            
            self.Board[row,col] = value
            self._update_status()
            return True
        
        else:
            
            return False
        
    @abstractmethod
    def _update_status(self):
        
        pass
    
    @abstractmethod
    def _initialize_game(self):
        
        pass

    @abstractmethod
    def _check_valid_move(self, row, col, value):
        
        pass