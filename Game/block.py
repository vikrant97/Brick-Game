import pygame,sys
from random import randrange as rand
from board import *
class Block(Board):
	def __init__(self):
		super(Block,self).__init__()
		self.block_shapes = [
				[[1, 1, 1],
				 [0, 1, 0]],
	
				[[0, 2, 2],
				 [2, 2, 0]],
	
				[[3, 3, 0],
				 [0, 3, 3]],
	
				[[4, 0, 0],
				 [4, 4, 4]],
	
				[[0, 0, 5],
				 [5, 5, 5]],
	
				[[6, 6, 6, 6]],
	
				[[7, 7],
				 [7, 7]]
			]
		
	def move(self, delta_x):
		if not self.gameover and not self.paused:
			new_x = self.block_x + delta_x
			if new_x < 0:
				new_x = 0
			if new_x > cols - len(self.block[0]):
				new_x = cols - len(self.block[0])
			if not self.checkPiecePos(self.board,
			                       self.block,
			                       (new_x, self.block_y)):
				self.block_x = new_x
	def rotate_block(self):
		if not self.gameover and not self.paused:
			new_block=[ [ self.block[y][x] for y in xrange(len(self.block)) ] for x in xrange(len(self.block[0]) - 1, -1, -1) ]
			if not self.checkPiecePos(self.board,new_block,(self.block_x, self.block_y)):
				self.block = new_block


