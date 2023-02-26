# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

import random
from pyboard import TurnBasedAgent, SetValueMove, TicTacToe

__all__ = 'TicTacToeAgent',

class TicTacToeAgent(TurnBasedAgent):
    
    def __init__(self, player, difficulty):
        
        super().__init__(player, difficulty)
        
        if player not in (1,2):
            
            raise ValueError(' '.join(["Method __init__ of",
                                      str(type(self)),
                                      "expected argument 'player' to be one of",
                                      str([1,2]),
                                      "but was",
                                      str(player)]))
        
        if difficulty == 4:
            
            print('Difficulty not yet implemented! Difficulty changed to hard.')
            self._Difficulty = 3
            
    def _get_winning_moves(self, game_board, valid_moves, player):    
        
        moves = []
        board = game_board.Board
        
        for move in valid_moves:
            
            i, j = move.Row, move.Column
            
            # Auxiliaries for packing cases
            i_indexes = [x for x in range(3) if x!=i]
            if j == 2: i_indexes.reverse()
            
            j_indexes = [x for x in range(3) if x!=j]
            if i == 2: j_indexes.reverse()
            
            # Check verticals
            if board[i,j_indexes[0]] == player and board[i,j_indexes[1]] == player:
                
                moves.append(move)
            
            # Check horizantals
            if board[i_indexes[0],j] == player and board[i_indexes[1],j] == player:
                
                moves.append(move)
            
            # Check diagonals in extremes
            if i in (0,2) and j in (0,2):
                
                if board[i_indexes[0],j_indexes[0]] == player and board[i_indexes[1],j_indexes[1]] == player:
                    
                    moves.append(move)
                    
            # Check diagonals in center
            if i == 1 and j == 1:
                
                if (board[0,0] == player and board[2,2] == player) or (board[2,0] == player and board[0,2] == player):
                    
                    moves.append(move)
                        
        return moves
    
    def _select_move_easy(self, game_board, valid_moves):
        
        winning_moves = self._get_winning_moves(game_board, valid_moves, self._Player)
        
        if len(winning_moves) != 0:
            
            return random.choice(winning_moves)
        
        else:
            
            return random.choice(valid_moves)
    
    def _select_move_medium(self, game_board, valid_moves):
        
        if game_board.Board[1,1] == 0:
            
            return SetValueMove(1, 1, self._Player)
        
        else:
            
            return self._select_move_easy(game_board, valid_moves)
    
    def _select_move_hard(self, game_board, valid_moves):
        
        if game_board.Board[1,1] == 0:
            
            return SetValueMove(1, 1, self._Player)
        
        else:
        
            winning_moves = self._get_winning_moves(game_board, valid_moves, self._Player)
            
            if len(winning_moves) != 0:
                
                return random.choice(winning_moves)
            
            else:
                
                losing_moves = self._get_winning_moves(game_board, valid_moves, self._Player%2+1)
                
                if len(losing_moves) != 0:
                    
                    return random.choice(losing_moves)
                
                else:
                    
                    return random.choice(valid_moves)
    
    def _select_move_extreme(self, game_board, valid_moves):
        
        # TODO
        pass
    
    def _check_board_type(self, game_board):
        
        if not isinstance(game_board, TicTacToe):
            
            raise TypeError(' '.join(["Method play_turn of",
                                      str(type(self)),
                                      "expected argument 'game_board' to be",
                                      str(TicTacToe),
                                      "but got",
                                      str(type(game_board))]))
        
        