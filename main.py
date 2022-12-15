import pygame
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

class typing:

	def __init__(self):
		self.w=800
		self.h=600
		self.reset=True
		self.active=False
		self.input_Text=''
		self.word=''
		self.total_time=0
		self.accuracy='0%'
		self.results= "Time:0 Accuracy:0 % Wpm:0"
		self.wpm=0
		self.end=False
		self.white = (255, 255, 255)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 128)

		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.set_caption("Judgemental Typing")
		icon = pygame.image.load('venta.jpg')
		pygame.display.set_icon(icon)
		pygame.display.update()

	def text_display(self,screen,msg,y,fsize,color):
		font = pygame.font.Font("freesansbold.ttf", fsize)
		text = font.render(msg , True , color)
		text_rect = text.get_rect(center=(self.w/2, y))
		screen.blit(text, text_rect)
		pygame.display.update()

	def get_sentence(self):
		return
		#add code for importing lines
	
	def result(self):
		return
		#add print statements and codes for result

	def run(self):
		
		self.resetg()
		self.running = True
		while (self.running):
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()

			pygame.display.update()

	def resetg(self):
		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.update()
		self.reset=False
		self.end = False
		self.input_text = ''
		self.word = ''
		self.time_start = 0
		self.total_time = 0
		self.wpm = 0

		self.screen.fill((0,0,0))
		execute.text_display(self.screen,"Judgemental Typing",60,40,self.green)
		

execute=typing()
execute.run()
