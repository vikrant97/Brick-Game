import pygame,sys
from random import randrange as rand
from block import *

class GamePlay(Block):
	def __init__(self):
		pygame.init()
		self.score=0
		self.highScore=0
		super(GamePlay,self).__init__()
		self.next_block = self.block_shapes[rand(len(self.block_shapes))]
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption('Tetris')
		self.initializeGame()
	def initializeGame(self):
		self.board = self.new_board()
		self.new_block()
		self.score = 0
		self.lines = 0
		self.level=1
		pygame.time.set_timer(pygame.USEREVENT+1, 1000)

	def new_block(self):
		self.block = self.next_block[:]
		self.next_block = self.block_shapes[rand(len(self.block_shapes))]
		self.block_x = int(cols / 2 - len(self.block[0])/2)
		self.block_y = 0
		if self.checkPiecePos(self.board,
		                   self.block,
		                   (self.block_x, self.block_y)):
			self.gameover = True
	def resumeGame(self):
		if self.gameover:
			self.initializeGame()
			self.gameover = False
	def drop(self, manual):
		if not self.gameover and not self.paused:
			self.block_y += 1
			if self.checkPiecePos(self.board,self.block,(self.block_x, self.block_y)):
				self.updateScore(1)
				self.board = self.join_pieces(self.board,self.block,(self.block_x, self.block_y))
				self.new_block()
				#self.cleared_rows = 0
				self.checkRowFull()
				#self.add_cl_lines(cleared_rows)
				return True
		return False
	def updateScore(self,val):
		if val==1:
			self.score+=10
		if val==2:
			self.score+=100
		if self.level*100<self.score:
			self.level+=1
		if self.score>self.highScore:
			self.highScore=self.score
	def checkRowFull(self):
		while True:
			for i, row in enumerate(self.board[:-1]):
				if 0 not in row:
					self.board = self.deleteRow(self.board, i)
					#self.cleared_rows += 1
					break
			else:
				break
 	def deleteRow(self,board, row):
		self.updateScore(2)
		del board[row]
		return [[0 for i in xrange(cols)]] + board
	def drop_fast(self):
		if not self.gameover and not self.paused:
			while(not self.drop(True)):
				pass
	def quit(self):
		pygame.quit()
		print "Game Over!"
		print "Your score is: %d" % self.score
		print "You reached level number: %d" % self.level
		sys.exit()
	
	def pygame_run(self):
		key_actions = {
			'ESCAPE':	self.quit,
			'a':		lambda:self.move(-1),
			'd':	lambda:self.move(+1),
			'DOWN':		lambda:self.drop(True),
			's':		self.rotate_block,
			'SPACE':	self.drop_fast,
			'c': 		self.resumeGame
		}

		self.gameover = False
		self.paused = False
		gameExit=False
		while not gameExit:
			self.screen.fill(pale)
			if self.gameover:
				self.quit()
			else:
				pygame.draw.rect(self.screen,gray,pygame.Rect(cols*cell_size,0,cell_size*(cols+6),rows*cell_size),0)
				self.create_fig(self.board, (0,0))
				self.create_fig(self.block,(self.block_x, self.block_y))
				self.disp_msg("Score: %d\n\nLevel: %d\n" % (self.score,self.level),
						(self.rlim+cell_size, cell_size*5))
				pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.USEREVENT+1:
					self.drop(False)
				elif event.type == pygame.QUIT:
					gameExit=True
					#self.quit()
				elif event.type == pygame.KEYDOWN:
					for key in key_actions:
						if event.key == eval("pygame.K_"
						+key):
							key_actions[key]()
		
x=GamePlay()
x.pygame_run()
