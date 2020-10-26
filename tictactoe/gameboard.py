'''
Created on 25.10.2020

@author: andreas
'''


class GameBoard(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.gameboard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.yMax = (len(self.gameboard))
        self.xMax = len(self.gameboard[0])

        if self.xMax != self.yMax:
            self.gameboard = [[]]
            print("Das Spielbrett muss quadratisch sein.")

    def getMaxMoves(self):
        return self.xMax * self.yMax

    def display(self):
        print(" " + "  ".join([str(column + 1) for column in range(self.xMax)]))
        for rowIndex, row in enumerate(self.gameboard):
            print(rowIndex + 1, row)

    def checkVictory(self):

        def checkEqual(check):
            return check[0] != 0 and check.count(check[0]) == len(check)

        victory = False
        for row in self.gameboard:
            victory = checkEqual(row) or victory
            player = row[0]

        columnIndex = 0
        while not victory and columnIndex < self.xMax:
            check = []
            for row in self.gameboard:
                check.append(row[columnIndex])

            victory = checkEqual(check) or victory
            player = check[0]
            columnIndex += 1

        if not victory:
            checkDown = []
            checkUp = []
            for row in self.gameboard:
                columnIndex -= 1
                checkDown.append(row[self.xMax - 1 - columnIndex])
                checkUp.append(row[columnIndex])

            if checkEqual(checkDown):
                victory = True
                player = checkDown[0]
            elif checkEqual(checkUp):
                victory = True
                player = checkUp[0]

        if not victory:
            player = 0

        return player

    def addInput(self, player, x, y):
        valid = False
        if self.gameboard[y - 1][x - 1] == 0:
            try:
                self.gameboard[y - 1][x - 1] = player
                valid = True

            except IndexError:
                print("Die eingegebenen Werte sind falsch.")

            except Exception as e:
                print(str(e))

        return valid
