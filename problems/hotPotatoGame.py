# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 05:50:46 2018

@author: avinash

Implements Hot Potato Game using a Queue

"""

from queue import Queue

def hotpotato(playerlist, num_of_rounds):
    
    game_q = Queue()
    
    for player in playerlist:
        game_q.enqueue(player)
        
    while game_q.size() > 1:
        for round in range(num_of_rounds):
            game_q.enqueue(game_q.dequeue())
            
        game_q.dequeue()
    
    # winner is the last person remaining    
    return game_q.dequeue() # queue is emptied by the end
    



if __name__ == "__main__":
    
    playerlist = ["Bill","David","Susan","Jane","Kent","Brad"]
    
    rounds = 7
    
    winner = hotpotato(playerlist, rounds)
    
    print(winner)