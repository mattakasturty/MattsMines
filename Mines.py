from tkinter import *
from random import *
from mineGame import *
import sys


class Square(Button):
	def __init__(self, master, row, col, *args,**kwargs):
		Button.__init__(self, master=master, *args, **kwargs)

		self.row = row
		self.col = col

		self.config(height = 1, width = 1)

		self.bind("<ButtonRelease-3>", self.rightClick)

	def click(self):
		space = self.master.master.game.board[self.row][self.col]
		if(space.isClicked == False):
			space.isClicked = True
			if(space.isMine):
				self.config(text = "x", bg="red")
				print("You blew yourself up at space " + str(self.row) + " " + str(self.col))
				sys.exit()
			else:
				if(space.surroundedBy >= 0):
					self.config(text = str(space.surroundedBy), relief=SUNKEN)
		if(self.master.master.game.checkWin()):
			print("You Won!")
			sys.exit()

	def rightClick(self, event):
		if(self['text'] == " "):
			self["text"] = "$"
			return 
		if(self['text'] == "$"):
			self["text"] = " "




class MineGame(Canvas):
	def __init__(self, master, *args,**kwargs):
		Canvas.__init__(self, master=master, *args, **kwargs)
		
		self.game = MinesGame()

		self.menuFrame = Frame(self)
		self.menuFrame.pack(side = TOP)

		difficulty = Button(master = self.menuFrame, text = "Difficulty")
		difficulty.grid(row = 0, column = 0)


		self.buttonFrame = Frame(self)
		self.buttonFrame.pack(side = BOTTOM)

		for i in range(0, self.game.rows, 1):
			for j in range(0, self.game.cols, 1):
				s = Square(master = self.buttonFrame, text = " ", row = i, col = j)
				s.config(command = s.click)
				s.grid(row = i, column = j)





if __name__ == "__main__":
	window = Tk()
	board = MineGame(master = window)
	board.pack()
	window.mainloop()