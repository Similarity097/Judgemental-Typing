import pygame
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

class typing:

	def __init__(self):
		self.w=1200
		self.h=720
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
					if (x >= 90 and x <= 300 and y >= 250 and y <= 350):
						self.active=True
						self.getlinenormal()
						self.resetg2()

			pygame.display.update()

	def resetg(self):
		self.screen=pygame.display.set_mode((self.w,self.h))
		pygame.display.update()
		self.reset=False
		self.end = False
		self.input_text = ''
		self.word = ''
		
		self.screen.fill((0,0,0))
		self.text_display(self.screen,"Judgemental Typing",600,60,40,self.green)
		self.text_display(self.screen,"Select Difficulty",190,200,40,self.green)

		pygame.draw.rect(self.screen, (255, 192, 25), (10, 250, 200, 100), 5)
		self.text_display(self.screen,"1. Easy",100,300,40,self.green)
		
		self.text_display(self.screen,"2. Medium",130,400,40,self.green)
		self.text_display(self.screen,"3. Hard",104,500,40,self.green)

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
		self.text_display(self.screen,"Judgemental Typing",400,60,40,self.green)

		# draw the rectangle for input box
		self.screen.fill((50, 0, 0), (50, 250, 650, 50))
		pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 5)
		self.text_display(self.screen, self.word, 200,270,25, self.green )
		pygame.display.update()

		


execute=typing()
execute.run()
