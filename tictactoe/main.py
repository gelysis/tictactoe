'''
Created on 25.10.2020

@author: andreas
'''
import sys
import time
import pygame
from pygame.locals import *
from tictactoe.gameboard import GameBoard

if __name__ == '__main__':
    print("Spiele tic tac toe\n")
    board = GameBoard()

    maxMoves = board.getMaxMoves()
    move = 1
    player = 1
    winningPlayer = 0

    while winningPlayer == 0 and move <= maxMoves:
        board.display()

        print(f"\nRUNDE {move}")
        print(f"Spieler {player} is am Zug: ")
        x = int(input("Welche Spalte? "))
        y = int(input("Welche Zeile? "))
        validMove = board.addInput(player, x, y)

        if validMove:
            move += 1
            winningPlayer = board.checkVictory()

            if winningPlayer == 0:
                print("\nDas Rennen ist noch offen\n")
                player = 3 - player
            else:
                print("\nSpieler " + str(player) + " hat gewonnen.\n")
        else:
            print("\nUngültiger Zug.\n")
