import random


class SnakeAndLadder:
    def __init__(self):
        '''
        Initializing Snake, Ladder and Player positions on the board
        '''
        self.SnakeFromPos = [99, 90, 73]
        self.SnakeToPos = [6, 65, 3]

        self.LadderFromPos = [7, 21, 31]
        self.LadderToPos = [27, 91, 56]

        self.Player1_pos = 0
        self.Player2_pos = 0
        self.turn = 0

    def chessStatus(self):
        '''
        To Show the Snake and Ladder positions on the board
        '''
        print("Snake Positions")
        for i in range(3):
            print(str(self.SnakeFromPos[i]) + '->' + str(self.SnakeToPos[i]))

        print("\nLadder Positions")
        for i in range(3):
            print(str(self.LadderFromPos[i]) + '->' + str(self.LadderToPos[i]))

    def isLadder(self):
        '''
        To Check if the player wins a ladder or not
        '''
        if (self.turn % 2 == 0):
            if self.Player1_pos in self.LadderFromPos:
                print("Congrats Player 1, You got the Ladder.")
                self.Player1_pos = self.LadderToPos[self.LadderFromPos.index(
                    self.Player1_pos)]
                print(" Now Player 1 is at : "+str(self.Player1_pos))

        else:
            if self.Player2_pos in self.LadderFromPos:
                print("Congrats Player 2, You got the Ladder.")
                self.Player2_pos = self.LadderToPos[self.LadderFromPos.index(
                    self.Player2_pos)]
                print(" Now Player 2 is at : "+str(self.Player2_pos))

    def isSnake(self):
        '''
        To determine if a player is bitten by a snake
        '''
        if (self.turn % 2 == 0):
            if self.Player1_pos in self.SnakeFromPos:
                print("Sorry Player 1, Snake bit you.")
                self.Player1_pos = self.SnakeToPos[self.SnakeFromPos.index(
                    self.Player1_pos)]
                print(" Now Player 1 is at : "+str(self.Player1_pos))
        else:
            if self.Player2_pos in self.SnakeFromPos:
                print("Sorry Player 2, Snake bit you.")
                self.Player2_pos = self.SnakeToPos[self.SnakeFromPos.index(
                    self.Player2_pos)]
                print(" Now Player 2 is at : ", self.Player2_pos)

    def isAttacked(self):
        '''
        To determine if a player attacks the other player
        '''
        if(self.Player1_pos == self.Player2_pos):
            if(self.turn % 2 == 0):
                print("Player 1 attacked Player 2 and now Player 2 is back to 0")
                self.Player2_pos = 0
            else:
                print("Player 2 attacked Player 1 and now Player 1 is back to 0")
                self.Player1_pos = 0

    def start(self):
        '''
        To Start the game
        '''
        while(self.Player1_pos < 100 and self.Player2_pos < 100):
            if((self.turn % 2) == 0):
                print(
                    "\n\nPlayer 1 : Roll the dice by pressing Enter or Press e to exit the game")
                a = input("Rolling  ")
                if(a == 'exit' or a == 'e'):
                    print("Game Exited")
                    break
                val = random.choice([1, 2, 3, 4, 5, 6])
                if(self.Player1_pos+val > 100):
                    print("Player 1 got : ", val)
                    print("Invalid Move! Cannot go beyond 100, you need a ",
                          100-self.Player1_pos, " to win")
                    print("Player 1 is still at : ", self.Player1_pos)
                else:
                    print("Player 1 got : ", val)
                    self.Player1_pos = self.Player1_pos+val
                    print("Player 1 is at :", self.Player1_pos)
                    self.isLadder()
                    self.isSnake()
                    self.isAttacked()
            else:
                print(
                    "\n\nPlayer 1 : Roll the dice by pressing Enter or Press e to exit the game")
                a = input("Rolling  ")
                if(a == 'exit' or a == 'e'):
                    print("Game Exited")
                    break
                val = random.choice([1, 2, 3, 4, 5, 6])
                if(self.Player2_pos+val > 100):
                    print("Player 2 got : ", val)
                    print("Invalid Move! Cannot go beyond 100, you need a ",
                          100-self.Player2_pos, " to win")
                    print("Player 2 is still at : ", self.Player2_pos)
                else:
                    print("Player 2 got : ", val)
                    self.Player2_pos = self.Player2_pos+val
                    print("Player 2 is at :", self.Player2_pos)
                    self.isLadder()
                    self.isSnake()
                    self.isAttacked()
            self.turn = self.turn+1
        if(self.Player1_pos >= 100):
            print("Congratulations! Player 1 is the winner")
        elif(self.Player2_pos >= 100):
            print("Congratulations! Player 2 is the winner")


# Creating an instance of the game
obj = SnakeAndLadder()
# Showing the status of the snake and ladder positions
obj.chessStatus()
# Starting the game
obj.start()

'''
Rules of the Game:
1. A player can get bitten by a snake
2. A player can win a ladder
3. A player can attack other player by snatching its position
4. A player must reach exactly at 100th position in order to win the game
5. If a player reaches beyond 100th position then the last turn of the player
   will be considered Invalid
6. Player who reaches 100th position first wins the game
'''
