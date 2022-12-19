import pygame
from pygame.locals import *
import os
import time
import random

# import os is used to change defaukt import directory from python to the current file's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initalizing the pygame module
pygame.init()


class typing:

    def __init__(self):
        # creating basic variables which will be used throughout the code
        self.w = 1200
        self.h = 720
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        self.stop = False

        self.white = (255, 255, 255)

        # command to import background from directory and rescale to gui window dimensions
        self.bg = pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(self.bg, (1200, 720))

        pygame.font.get_fonts()
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Judgemental Typing")
        icon = pygame.image.load('venta.jpg')
        pygame.display.set_icon(icon)

    def text_display(self, screen, msg, x, y, fsize, color):
        # creating text command
        font = pygame.font.SysFont("georgia", fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def random_line(self, name):
        # function to import random line from the selected text file
        # read() is to read the file and bring its contents
        # splitlines is to split the lines at \n from the.txt file and assign them to a list
        filename = open(name).read()
        lines = filename.splitlines()
        line = random.choice(lines)
        return line

    def result(self):
        # function to print the final result of the code
        if not self.stop:

            self.total_time = time.time() - self.time_start
            count = 0

            # i iterates through the index values while c iterated through the individual letters of the word
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass

            self.accuracy = count/len(self.word)*100
            self.wpm = len(self.input_text)/(5*self.total_time)
            self.stop = True
            self.results = 'Time: '+str(round(self.total_time)) + " secs  |  Accuracy: " + str(
                round(self.accuracy)) + "%" + '  |  Wpm: ' + str(round(self.wpm))

            pygame.draw.rect(self.screen, (191, 58, 238),
                             (515, 565, 170, 80), 3)
            self.text_display(self.screen, "Reset", 600, 600, 50, self.white)
            self.text_display(self.screen, "Rating ", 100, 650, 30, self.white)

            # conditions for rating according to the wpm count
            if self.wpm >= 0 and self.wpm <= 20:
                self.text_display(self.screen, "1", 170, 645, 60, self.white)

            elif self.wpm > 20 and self.wpm <= 40:
                self.text_display(self.screen, "2", 170, 645, 60, self.white)

            elif self.wpm > 40 and self.wpm <= 60:
                self.text_display(self.screen, "3", 170, 645, 60, self.white)

            elif self.wpm > 60 and self.wpm < 80:
                self.text_display(self.screen, "4", 170, 645, 60, self.white)

            elif self.wpm >= 80:
                self.text_display(self.screen, "5", 170, 645, 60, self.white)

                pygame.display.update()

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
                    x, y = pygame.mouse.get_pos()

                    if (x >= 50 and x <= 200 and y >= 250 and y <= 350):
                        self.active = False
                        self.word = self.random_line('EASY.txt')
                        self.resetg2()
                        self.run2()
                        break

                    elif (x >= 50 and x <= 200 and y >= 350 and y <= 450):
                        self.active = False
                        self.word = self.random_line('MEDIUM.txt')
                        self.resetg2()
                        self.run2()
                        break

                    elif (x >= 50 and x <= 200 and y >= 450 and y <= 550):
                        self.active = False
                        self.word = self.random_line('HARD.txt')
                        self.resetg2()
                        self.run2()
                        break

                clock.tick(60)

            pygame.display.update()

    def run2(self):
        self.running = True

        while (self.running):

            clock = pygame.time.Clock()

            self.screen.fill((0, 0, 0), (50, 350, 1100, 50))
            pygame.draw.rect(self.screen, (191, 58, 238),
                             (50, 350, 1100, 50), 3)
            self.text_display(self.screen, self.input_text,
                              600, 372.5, 35, self.white)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == QUIT:
                    self.running = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if (x >= 50 and x <= 1100 and y >= 350 and y <= 400):
                        self.active = True
                        self.input_text = ''
                        self.text_display(
                            self.screen, self.input_text, 600, 375, 30, self.white)
                        self.time_start = time.time()

                    if (x >= 515 and x <= 685 and y >= 565 and y <= 645):
                        self.run()
                        x, y = pygame.mouse.get_pos()

                elif (event.type == pygame.KEYDOWN):

                    if self.active and not self.stop:

                        if event.key == pygame.K_RETURN:
                            self.result()
                            self.text_display(
                                self.screen, self.results, 600, 500, 30, self.white)
                            self.stop = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]

                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    def resetg(self):

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.update()

        self.input_text = ''
        self.word = ''

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        self.text_display(self.screen, "Judgemental Typing",
                          600, 80, 50, self.white)
        self.text_display(self.screen, "Select Difficulty",
                          190, 200, 45, self.white)
        self.text_display(self.screen, "1. Easy", 100, 300, 40, self.white)
        self.text_display(self.screen, "2. Medium", 130, 400, 40, self.white)
        self.text_display(self.screen, "3. Hard", 104, 500, 40, self.white)

        pygame.display.update()

    def resetg2(self):

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.update()

        self.stop = False
        self.active = False
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        self.text_display(self.screen, "Judgemental Typing",
                          600, 80, 50, self.white)
        self.text_display(self.screen, self.word, 600, 250, 35, self.white)

        pygame.display.update()


# initializing and starting the pygame gui window
typing().run()
