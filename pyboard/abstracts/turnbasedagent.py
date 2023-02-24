# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

from abc import ABC, abstractmethod
import random

__all__ = 'TurnBasedAgent',

class TurnBasedAgent(ABC):
    
    def __init__(self, player=1, difficulty=0):
        
        self._Player = player
        self._Difficulty = difficulty
        
        super().__init__()
    
    def _select_move(self, game_board):
        
        valid_moves = game_board.get_valid_moves(self._Player)
        
        if self._Difficulty == 0:
            
            return self._select_move_random(valid_moves)
        
        elif self._Difficulty == 1:
            
            return self._select_move_easy(game_board, valid_moves)
        
        elif self._Difficulty == 2:
            
            return self._select_move_medium(game_board, valid_moves)
        
        elif self._Difficulty == 3:
            
            return self._select_move_hard(game_board, valid_moves)
        
        else:
            
            return self._select_move_extreme(game_board, valid_moves)
        
    def get_player(self):
        
        return self._Player
    
    def get_difficulty(self):
        
        return self._Difficulty
    
    def _select_move_random(self, valid_moves):
        
        return random.choice(valid_moves)
    
    @abstractmethod
    def _select_move_easy(self, game_board, valid_moves):
        
        return random.choice(valid_moves)
    
    @abstractmethod
    def _select_move_medium(self, game_board, valid_moves):
        
        pass
    
    @abstractmethod
    def _select_move_hard(self, game_board, valid_moves):
        
        pass
    
    @abstractmethod
    def _select_move_extreme(self, game_board, valid_moves):
        
        pass
        
    def play_turn(self, game_board):
        
        return game_board.update_tile(self._select_move(game_board))