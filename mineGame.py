#mineGame.py

from random import *
from tkinter import StringVar

class MinesGame:
	"""
	MinesGame Class - Basic Framework of MinesGame
	"""
	
	def __init__(self, master, diff):
		"""
		MinesGame Constructor. Takes no arguments
		"""
		self.master = master
		self.setSize(diff)
		

	def __str__(self):
		"""
		Pretty prints a 2D array of X's and Spaces
		"""
		string = ""
		for i in self.board:
			for j in i:
				if(j.isMine):
					string += "x"
				else:
					if(j.surroundedBy == 0):
						string += " "
					else:
						string += str(j.surroundedBy)
			string += "\n"
		return string


	def setSize(self, difficulty):
		"""
		MinesGame.setSize(self, difficulty)
			Takes difficulty as a string: Easy | Intermediate | Expert | Custom(To be written)
		"""
		self.difficulty = StringVar(self.master)
		self.difficulty.set(difficulty)
		print(self.difficulty.get())
		if(self.difficulty.get() == "Easy"):
			self.rows = 8
			self.cols = 8
			self.numMines = 10
		elif(self.difficulty.get() == "Intermediate"):
			self.rows = 16
			self.cols = 16
			self.numMines = 40
		elif(self.difficulty.get() == "Expert"):
			self.rows = 16
			self.cols = 30
			self.numMines = 99
		else:
			pass
		
		self.initBoard()

	def initBoard(self):
		"""

		"""
		self.board = []
		print(self.difficulty.get())
		#Board of empty squares
		for i in range(0, self.rows, 1):
			l = []
			for j in range(0, self.cols, 1):
				l.append(Square(self.board, False))
			self.board.append(l)
		
		#Populate board with some mines
		count = 0
		while( count < self.numMines ):
			i = randrange(0, self.rows, 1) 
			j = randrange(0, self.cols, 1)
			if(self.board[i][j].isMine is not True):
				count += 1
			self.board[i][j].isMine = True

		#Find out how many mines surround the squares
		for i in range(0, self.rows, 1):
			for j in range(0, self.cols, 1):
				if(self.board[i][j].isMine == False):
					
					#If Square is on top row
					if(i==0):
						if(j==0):
							n = self.board[0][1].isMine + self.board[1][0].isMine + self.board[1][1].isMine
						elif(j==(self.cols-1)):
							n = self.board[0][self.cols-2].isMine + self.board[1][self.cols-2].isMine + self.board[1][self.cols-1].isMine
						else:
							n = self.board[0][j-1].isMine + self.board[1][j].isMine + self.board[0][j+1].isMine + self.board[1][j-1].isMine + self.board[1][j+1].isMine
						self.board[i][j].surroundedBy = n

					#If Square on Bottom row
					elif(i==(self.rows-1)):
						if(j==0):
							n = self.board[self.rows-1][1].isMine + self.board[self.rows-2][0].isMine + self.board[self.rows-2][1].isMine
						elif(j==(self.cols-1)):
							n = self.board[self.rows-1][self.cols-2].isMine + self.board[self.rows-2][self.cols-2].isMine + self.board[self.rows-2][self.cols-1].isMine
						else:
							n = self.board[self.rows-1][j-1].isMine + self.board[self.rows-2][j].isMine + self.board[self.rows-1][j+1].isMine + self.board[self.rows-2][j-1].isMine + self.board[self.rows-2][j+1].isMine
						self.board[i][j].surroundedBy = n

					#If Square is in a middle row
					else:
						if(j==0):
							n = self.board[i-1][j].isMine + self.board[i+1][j].isMine + self.board[i][j+1].isMine + self.board[i-1][j+1].isMine + self.board[i+1][j+1].isMine
						elif(j==(self.cols-1)):
							n = self.board[i-1][j].isMine + self.board[i+1][j].isMine + self.board[i][j-1].isMine + self.board[i-1][j-1].isMine + self.board[i+1][j-1].isMine
						else:
							n = self.board[i-1][j].isMine + self.board[i+1][j].isMine + self.board[i][j-1].isMine + self.board[i-1][j-1].isMine + self.board[i+1][j-1].isMine + self.board[i][j+1].isMine + self.board[i-1][j+1].isMine + self.board[i+1][j+1].isMine
						self.board[i][j].surroundedBy = n

	def checkWin(self):
		for i in range(0, self.rows, 1):
			for j in range(0, self.cols, 1):
				if(self.board[i][j].isMine == False and self.board[i][j].isClicked == False):
					return False
		return True

class Square:
	"""

	"""
	def __init__(self, board, isMine):
		"""

		"""
		self.board = board
		self.isMine = isMine
		self.isClicked = False
		self.surroundedBy = 0




#Test, please ignore
if __name__ == "__main__":
	game = MinesGame()
	print(game)


