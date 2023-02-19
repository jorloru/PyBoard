# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

from abc import ABC, abstractmethod
import numpy as np
from pyboard import TurnBasedStatus, SetValueMove, MovePieceMove

__all__ = 'TurnBasedBoard',

class TurnBasedBoard(ABC):
    
    def __init__(self, config):
        
        self.Config = config
        self.Board  = np.zeros((config.Rows, config.Columns), int)
        self.Status = TurnBasedStatus()
        
        super().__init__()
        
    def update_tile(self, move):
        
        if self.Config.MoveType == SetValueMove:
        
            if type(move) != SetValueMove:
                
                raise TypeError(' '.join(['Method update_tile(move) of class',type(self),'expected argument of type TurnBasedMove, but got',str(type(move))]))
            
            else:
                
                if self._check_valid_move(move):
                    
                    self.Board[move.Row,move.Column] = move.Value
                    self.Status.LastPlayedMove = move
                    self._update_status()
                    return True
                
                else:
                    
                    return False
                
        elif self.Config.MoveType == MovePieceMove:
        
            if type(move) != MovePieceMove:
                
                raise TypeError(' '.join(['Method update_tile(move) of class',type(self),'expected argument of type TurnBasedMove, but got',str(type(move))]))
            
            else:
                
                if self._check_valid_move(move):
                    
                    self.Board[move.RowTarget,move.ColumnTarget] = self.Board[move.RowOrigin,move.ColumnOrigin]
                    self.Board[move.RowOrigin,move.ColumnOrigin] = 0
                    self.Status.LastPlayedMove = move
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
    def get_valid_moves(self, player):
        
        pass

    @abstractmethod
    def _check_valid_move(self, move):
        
        pass