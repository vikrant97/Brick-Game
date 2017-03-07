import pygame,sys
from random import randrange as rand

colors = [
(0,   0,   0  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) 
]

white=(248,248,255)
black=(0,0,0)
red=(255,0,0)
violet=(238,130,238)
pale=(175,238,238)
pink=(255,182,193)
gray=(211,211,211)
rows=34
cols=32
cell_size=12

class Board(object):
	def __init__(self):
		super(Board,self).__init__()
		self.height=cell_size*rows
		self.width=cell_size*(cols+8)
		self.rlim = cell_size*cols
		self.bground_grid = [[ 8 if x%2==y%2 else 0 for x in xrange(cols)] for y in xrange(rows)]
	
	def create_fig(self, fig, init_coordinates):
		off_x, off_y  = init_coordinates
		for y, row in enumerate(fig):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(self.screen,colors[val],
						pygame.Rect((off_x+x) *cell_size,(off_y+y) *cell_size, cell_size,cell_size),0)	
	
	def checkPiecePos(self,board, fig, offset):
		off_x, off_y = offset
		for cy, row in enumerate(fig):
			for cx, cell in enumerate(row):
				try:
					if cell and board[ cy + off_y ][ cx + off_x ]:
						return True
				except IndexError:
					return True
		return False
	def join_pieces(self,mat1, mat2, mat2_off):
		off_x, off_y = mat2_off
		for cy, row in enumerate(mat2):
			for cx, val in enumerate(row):
				mat1[cy+off_y-1	][cx+off_x] += val
		return mat1

	def new_board(self):
		board = [ [ 0 for x in xrange(cols) ]
			for y in xrange(rows) ]
		board += [[ 1 for x in xrange(cols)]]
		return board
	
	def disp_msg(self,msg, coordinates):
		x,y = coordinates
		for line in msg.splitlines():
			self.screen.blit(
				pygame.font.Font(
			pygame.font.get_default_font(), 12).render(
					line,
					False,
					black,
					white),
				(x,y))
			y+=14
