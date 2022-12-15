import pygame
#initalizeing pygame
pygame.init()
#creating the screen
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Judgemental Typing")
#icon for gui window
icon = pygame.image.load('venta.jpg')
pygame.display.set_icon(icon)
pygame.display.update()

#basic colour codings
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#adding text to the gui window
font = pygame.font.Font("freesansbold.ttf",32)
text = font.render("Judemental Typing", True , green )
textRect= text.get_rect()
textRect.center = (400, 50)

running = True
# keep game running till running is true
while running:
	screen.fill((0,0,0))
	screen.blit(text, textRect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()

