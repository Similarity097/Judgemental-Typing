import pygame
import os
import sys
import pygame.freetype
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

class typing:

	def __init__(self):
		self.w=1200
		self.h=720
		self.reset=True
		self.active=False
		self.input_text=''
		self.word=''
		self.total_time=0
		self.accuracy='0%'
		self.results= "Time:0 Accuracy:0 % Wpm:0"
		self.wpm=0
		self.end=False
		self.white = (255, 255, 255)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 128)
		self.space="\n"

		self.bg = pygame.image.load('bg5.jpg')
		self.bg = pygame.transform.scale(self.bg, (1200, 720))
		self.bg2 = pygame.image.load('bg5.jpg')
		self.bg2 = pygame.transform.scale(self.bg2, (1200, 720))

		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.set_caption("Judgemental Typing")
		icon = pygame.image.load('venta.jpg')
		pygame.display.set_icon(icon)
		pygame.display.update()

	def text_display(self,screen,msg,x,y,fsize,color):
		font = pygame.font.Font("freesansbold.ttf", fsize)
		text = font.render(msg , True , color)
		text_rect = text.get_rect(center=(x, y))
		screen.blit(text, text_rect)
		pygame.display.update()

	def get_sentence(self):
		return
		#add code for importing lines
	
	def result(self):
		return
		#add print statements and codes for result

	def getlinenormal(self):
		self.word="SAMPLE TEXT"
		

	def timeshow(self):
		font=pygame.freetype.SysFont(None,34)
		font.origin=True
		ticks=pygame.time.get_ticks()
		mills=int(ticks%1000)
		seconds=int(ticks/1000%60)
		minutes=int(ticks/60000%24)
		out='{minutes:02d}:{seconds:02d}:{mills}'.format(minutes=minutes, mills=mills, seconds=seconds)
		font.render_to(self.screen, (100, 200), out, pygame.Color('white'))

	def run(self):
		
		self.resetg()
		self.running = True
		while (self.running):
			clock = pygame.time.Clock()
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					x,y = pygame.mouse.get_pos()
					if (x >= 50 and x <= 200 and y >= 250 and y <= 350):
						self.active=True
						self.getlinenormal()
						self.resetg2()
						self.run2()
						break
					elif (x >= 50 and x <= 200 and y >= 350 and y <= 450):
						self.active=True
						self.getlinenormal()
						self.resetg2()
						self.run2()
						break
					elif (x >= 50 and x <= 200 and y >= 450 and y <= 550):
						self.active=True
						self.getlinenormal()
						self.resetg2()
						self.run2()
						break
				clock.tick(60)
			pygame.display.update()

	def run2(self):
		self.running = True
		while (self.running):
			clock = pygame.time.Clock()

			self.screen.fill((0,0,0), (50, 350, 1100, 50))
			self.screen.fill((0,0,0), (100, 165, 160, 40))
			pygame.draw.rect(self.screen, (159,43,104), (50, 350, 1100, 50), 3)

			#input font commands
			font = pygame.font.Font("freesansbold.ttf", 30)
			txt_surface = font.render(self.input_text, True, self.white)
			self.screen.blit(txt_surface, (60, 360))
			self.timeshow()
			#self.timeshow()
			# end of input commands

			#self.text_display(self.screen, self.input_text, 100, 275, 30, self.white)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					x,y = pygame.mouse.get_pos()
					if (x >= 100 and x <= 1000 and y >= 250 and y <= 600):
						self.active=True
						self.input_text=''
						self.time_start=time.time()
				elif event.type == pygame.KEYDOWN:
					if self.active and not self.end:
						if event.key == pygame.K_RETURN:
							self.input_text=self.input_text+self.space
							self.input_text+=event.unicode
							self.end = False
						elif event.key == pygame.K_BACKSPACE:
							self.input_text=self.input_text[:-1]
						else:
							try:
								self.input_text+=event.unicode
							except:
								pass
			clock.tick(60)
	def resetg(self):
		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.update()
		self.reset=False
		self.end = False
		self.input_text = ''
		self.word = ''
		
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg, (0, 0))
		self.text_display(self.screen,"Judgemental Typing",600,80,40,self.white)
		self.text_display(self.screen,"Select Difficulty",190,200,40,self.white)

		#pygame.draw.rect(self.screen, (255, 192, 25), (10, 250, 200, 100), 5)
		self.text_display(self.screen,"1. Easy",100,300,40,self.white)
		self.text_display(self.screen,"2. Medium",130,400,40,self.white)
		self.text_display(self.screen,"3. Hard",104,500,40,self.white)

		pygame.display.update()

	def resetg2(self):
		self.screen=pygame.display.set_mode((self.w,self.h))
		
		pygame.display.update()
		self.reset=False
		self.end = False
		self.input_text = ''
		self.time_start = 0
		self.total_time = 0
		self.wpm = 0

		self.screen.fill((0,0,0))
		self.screen.blit(self.bg2, (0, 0))
		self.text_display(self.screen,"Judgemental Typing",600,80,40,self.white)

		self.text_display(self.screen, self.word, 600,250,35, self.white )
		
		pygame.display.update()

execute=typing()
execute.run()