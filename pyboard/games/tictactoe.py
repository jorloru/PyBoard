# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

import numpy as np
from pyboard import SetValueMove, TicTacToeConfig, TurnBasedBoard

__all__ = 'TicTacToe',
    
class TicTacToe(TurnBasedBoard):
    
    def __init__(self, config):
        
        super().__init__(config)
        
        if not isinstance(config,TicTacToeConfig):
            
            raise TypeError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'config' to be",
                                      str(TicTacToeConfig),
                                      "but got",
                                      str(type(config))]))
        
        self.Status.PlayerTurn = config.FirstPlayer
        
    def _update_status(self):
        
        if self.Status.Turn >= 5:
            
            if np.all(self.Board.diagonal() == 1) or np.all(np.fliplr(self.Board).diagonal() == 1):
                
                self.Status.Finished = True
                self.Status.Winner = self.Status.PlayerTurn
                
            else:
                
                for i in range(3):
                
                    if np.all(self.Board[i] == self.Status.PlayerTurn) or np.all(self.Board[:,i] == self.Status.PlayerTurn):
                    
                        self.Status.Finished = True
                        self.Status.Winner = self.Status.PlayerTurn
        
        self.Status.Turn += 1
        self.Status.PlayerTurn = self.Status.PlayerTurn%2 + 1
        
        if self.Status.Turn == 10:
            
            self.Status.Finished = True
    
    def _initialize_game(self):
        
        pass
        
    def get_valid_moves(self, player):
        
        if type(player) != int:
            
            raise TypeError(' '.join(["Method get_valid_moves of",
                                      str(type(self)),
                                      "expected argument 'player' to be",
                                      str(int),
                                      "but got",
                                      str(type(player))]))
            
        elif player not in (1,2):
            
            raise ValueError(' '.join(["Method get_valid_moves of",
                                      str(type(self)),
                                      "expected argument 'player' to be one of",
                                      str([1,2]),
                                      "but got",
                                      str(player)]))
        
        valid_moves = []
        
        if player == self.Status.PlayerTurn:
        
            for i in range(self.Config.Rows):
                for j in range(self.Config.Columns):
                
                    if self.Board[i,j] == 0:
                    
                        valid_moves.append(SetValueMove(i, j, self.Status.PlayerTurn))
                    
        return valid_moves

    def _check_valid_move(self, move):
        
        if (type(move.Row) != int) or (type(move.Column) != int) or (type(move.Value) != int):
            
            return False
        
        elif (move.Row < 0) or (move.Column < 0) or (move.Row > len(self.Board)) or (move.Column > len(self.Board[0])):
            
            return False
        
        elif self.Status.Finished or (self.Board[move.Row,move.Column] != 0) or (move.Value != self.Status.PlayerTurn):
            
            return False
        
        else:
            
            return True