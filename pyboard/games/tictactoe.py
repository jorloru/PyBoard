# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

import numpy as np
from pyboard import TurnBasedStatus, TurnBasedMove, TicTacToeConfig, TurnBasedBoard

__all__ = 'TicTacToe',
    
class TicTacToe(TurnBasedBoard):
    
    def __init__(self, config):
        
        super().__init__(config)
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
        
        self.Board  = np.zeros((self.config.Rows, self.config.Columns), int)
        self.Status = TurnBasedStatus()
        self.Status.PlayerTurn = self.config.firstPlayer
        
    def get_valid_moves(self):
        
        valid_moves = []
        
        for i in range(self.Config.Rows):
            
            for j in range(self.Config.Columns):
                
                if self.Board[i,j] == 0:
                    
                    valid_moves.append(TurnBasedMove(i, j, self.Status.PlayerTurn))
                    
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

if __name__ == "__main__":
    
    game = TicTacToe(TicTacToeConfig())
    
    print('Welcome to Tic Tac Toe!\n')
    print('In this console version you can try a demo where you play against yourself.\n')
    print("You can input the position (i,j) as a string 'i j' where both indices can go from 0 to 2\n")
    input("Hit Enter to start!")
    
    while not game.Status.Finished:
        
        print('\n---------------------------\n')
        print(' '.join(['Player',str(game.Status.PlayerTurn),'turn\n']))
        print(game.Board)
                
        validmove = False
        while not validmove:
            
            move = input('\nSelect your move! : ').split()
            
            if not (len(move) == 2):
                
                print("\nInvalid move! Couldn't distinguish 2 positions from input.")
                
            elif not move[0].isnumeric() or not move[1].isnumeric():
                
                print("\nInvalid move! Non-numeric input.")
                
            else:
                
                if not game.update_tile(TurnBasedMove(int(move[0]), int(move[1]), game.Status.PlayerTurn)):
                    
                    print("\nInvalid move! Valid positions range from '0 0' to '2 2' and are not already occupied.")
                    
                else:
                    
                    validmove = True
            
    print('\n---------------------------\n')  
    print(game.Board)
    
    if game.Status.Winner == 0:
        print('\nDraw!')
    else:
        print(' '.join(['\nPlayer',str(game.Status.PlayerTurn%2 + 1),'won!']))
    
