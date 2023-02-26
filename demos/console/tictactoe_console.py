# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26

@author: jorloru
"""

import sys
import os
sys.path.append(os.path.join('..','..'))

from pyboard import TicTacToe, TicTacToeConfig, TicTacToeAgent, SetValueMove

if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!\n')
    print('In this console version you (Player 1) can try a demo where you play against the computer (Player 2).\n')
    print("You can input the position (i,j) as a string 'i j' where both indices can go from 0 to 2\n")
    input("Hit Enter to start!")
    
    while True:
        
        firstPlayer = input("\nSelect which player is going to move first (1: you, 2: computer): ")
        
        if firstPlayer in ('1','2'):
            
            firstPlayer = int(firstPlayer)
            break
        
        else:
            
            print('\nInvalid player! Enter just the number 1, or 2.\n')
    
    game = TicTacToe(TicTacToeConfig(firstPlayer))
    
    while True:
        
        difficulty = input("\nSelect the computer's difficulty (0: random, 1: easy, 2: medium, 3: hard, 4: extreme): ")
        
        if difficulty in ('0','1','2','3','4'):
            
            difficulty = int(difficulty)
            break
        
        else:
            
            print('\nInvalid difficulty! Enter just the number 0, 1, 2, 3 or 4.\n')
            
    player2 = TicTacToeAgent(2, difficulty)
    
    while not game.Status.Finished:
        
        print('\n---------------------------\n')
        print("Player " + str(game.Status.PlayerTurn) + "'s turn!\n")
        print(game.Board)
        
        if game.Status.PlayerTurn == 1:
        
            validmove = False
            while not validmove:
                
                move = input('\nSelect your move! : ').split()
                
                if not (len(move) == 2):
                    
                    print("\nInvalid move! Couldn't distinguish 2 positions from input.")
                    
                elif not move[0].isnumeric() or not move[1].isnumeric():
                    
                    print("\nInvalid move! Non-numeric input.")
                    
                else:
                    
                    if not game.update_tile(SetValueMove(int(move[0]), int(move[1]), game.Status.PlayerTurn)):
                        
                        print("\nInvalid move! Valid positions range from '0 0' to '2 2' and are not already occupied.")
                        
                    else:
                        
                        validmove = True
                        
        else:
            
            input('\nHit Enter to resolve turn!')
            player2.play_turn(game)
            
    print('\n---------------------------\n')  
    print(game.Board)
    
    if game.Status.Winner == 0:
        print('\nDraw!')
    else:
        print(' '.join(['\nPlayer',str(game.Status.PlayerTurn%2 + 1),'won!']))