import pygame
from pygame.locals import *
import os
import sys
import pygame.freetype
import time
import random
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
		self.time_start= 0
		self.total_time=0
		self.accuracy='0%'
		self.results= "Time:0 Accuracy:0% Wpm:0"
		self.wpm=0
		self.end=False
		self.white = (255, 255, 255)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 128)

		self.bg = pygame.image.load('bg5.jpg')
		self.bg = pygame.transform.scale(self.bg, (1200, 720))
		self.bg2 = pygame.image.load('bg5.jpg')
		self.bg2 = pygame.transform.scale(self.bg2, (1200, 720))

		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.set_caption("Judgemental Typing")
		icon = pygame.image.load('venta.jpg')
		pygame.display.set_icon(icon)

	def text_display(self,screen,msg,x,y,fsize,color):
		font = pygame.font.Font("freesansbold.ttf", fsize)
		text = font.render(msg , 1 , color)
		text_rect = text.get_rect(center=(x, y))
		screen.blit(text, text_rect)
		pygame.display.update()

	def random_line(self,name):
		lines = open(name).read().splitlines()
		return random.choice(lines)
		
	def result(self):
		if not self.end:
			self.total_time = time.time() - self.time_start

			count=0
			for i,c in enumerate(self.word):
				try:
					if self.input_text[i]==c:
						count+=1
				except:
					pass
			self.accuracy = count/len(self.word)*100

			self.wpm = len(self.input_text)*60/(5*self.total_time)
			self.end =True
			self.results='Time:'+str(round(self.total_time)) + " secs   Accuracy:" + str(round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

			self.text_display(self.screen,"Reset",600,600,30,self.white)
			pygame.display.update()

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
						self.word = self.random_line('EZ.txt')
						self.resetg2()
						self.run2()
						break
					elif (x >= 50 and x <= 200 and y >= 350 and y <= 450):
						self.active=True
						self.word = self.random_line('MID.txt')
						self.resetg2()
						self.run2()
						break
					elif (x >= 50 and x <= 200 and y >= 450 and y <= 550):
						self.active=True
						self.word = self.random_line('SWEAT.txt')
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
			pygame.draw.rect(self.screen, (159,43,104), (50, 350, 1100, 50), 3)
			
			self.text_display(self.screen,self.input_text,600,375,30,self.white)
			#font = pygame.font.Font("freesansbold.ttf", 30)
			#txt_surface = font.render(self.input_text, True, self.white)
			#self.screen.blit(txt_surface, (60, 360))

			pygame.display.update()
			for event in pygame.event.get():
				if event.type == QUIT:
					self.running = False
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONUP:
					x,y = pygame.mouse.get_pos()
					if (x >= 50 and x <= 1100 and y >= 350 and y <= 400):
						self.active=True
						self.type=False
						self.input_text= ''
						self.text_display(self.screen,self.input_text,600,375,30,self.white)
						self.time_start=time.time()
					if (x >= 550 and x <= 650 and y >= 600 and y <= 670):
						self.run()
						x, y= pygame.mouse.get_pos()
				elif (event.type == pygame.KEYDOWN):
					if self.active and not self.end and not self.type:
						if event.key == pygame.K_RETURN:
							self.result()
							self.text_display(self.screen,self.results,600,500,28,self.white)
							self.end=True
						elif event.key == pygame.K_BACKSPACE:
							self.input_text=self.input_text[:-1]
						else:
							try:
								self.input_text += event.unicode
							except:
								pass
			pygame.display.update()
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

		self.text_display(self.screen,"1. Easy",100,300,40,self.white)
		self.text_display(self.screen,"2. Medium",130,400,40,self.white)
		self.text_display(self.screen,"3. Hard",104,500,40,self.white)

		pygame.display.update()

	def resetg2(self):
		self.screen=pygame.display.set_mode((self.w,self.h))
		
		pygame.display.update()
		self.reset=False
		self.end = False
		self.type= True
		self.input_text = ''
		self.time_start = 0
		self.total_time = 0
		self.wpm = 0

		self.screen.fill((0,0,0))
		self.screen.blit(self.bg2, (0, 0))
		self.text_display(self.screen,"Judgemental Typing",600,80,40,self.white)
		pygame.draw.rect(self.screen, (159,43,104), (50, 350, 1100, 50), 3)
		self.text_display(self.screen, self.word, 600,250,35, self.white )
		
		pygame.display.update()

typing().run()