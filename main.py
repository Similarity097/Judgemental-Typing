import pygame
#initalizeing pygame
pygame.init()
#creating the screen
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Judgemental Typing")
#icon for gui window
icon = pygame.image.load('venta.jpg')
pygame.display.set_icon(icon)
screen.fill((0,0,0))
pygame.display.update()

running = True
# keep game running till running is true
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

