# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

import random
from pyboard import TurnBasedAgent

__all__ = 'TicTacToeAgent',

class TicTacToeAgent(TurnBasedAgent):
    
    def __init__(self, player, difficulty):
        
        super().__init__(player, difficulty)
        
        if difficulty > 0:
            
            print('Difficulty not yet implemented! Difficulty changed to random.')
            self._Difficulty = 0
    
    def _select_move_easy(self, game_board, valid_moves):
        
        # TODO
        pass
    
    def _select_move_medium(self, game_board, valid_moves):
        
        # TODO
        pass
    
    def _select_move_hard(self, game_board, valid_moves):
        
        # TODO
        pass
    
    def _select_move_extreme(self, game_board, valid_moves):
        
        # TODO
        pass