# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 2023

@author: jorloru
"""

__all__ = 'TurnBasedStatus',

class TurnBasedStatus():
    
    def __init__(self):
        
        self.Finished = False
        self.Winner = 0
        self.Turn = 1
        self.PlayerTurn = 1