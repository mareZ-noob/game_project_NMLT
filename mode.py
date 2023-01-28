import pygame
import random
import sys
from pygame.locals import *
from pygame import mixer
from single import single_player as single
from duo import two_players as duo

# Start
mainClock = pygame.time.Clock()
pygame.init()

# Custom
pygame.display.set_caption('Catching Fruits')
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font3 = pygame.font.SysFont('None', 32)
font4 = pygame.font.Font('./fonts/freesansbold.ttf', 40)
back_img = pygame.image.load("./images/hongback.png").convert()
background3 = pygame.image.load("./images/casino.jpg").convert()
solo_img = pygame.image.load("./images/orange.png").convert()
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
SKY = (0, 191, 255)
SEA = (84, 255, 159)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Class button
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def back(self):
        action = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if action:
            pass

    def exit(self):
        action1 = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action1 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action1

    def solo(self):
        action2 = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action2 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if action2:
            pass

    def return_music(self):
        action3 = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action3 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action3

    def choose_background(self):
        action4 = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action4 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action4

    def choose(self):
        action5 = False

        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action5 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action5


single_button = Button(300, 250, solo_img, 1)
duo_button = Button(300, 400, solo_img, 1)
back_button = Button(0, 0, back_img, 0.4)


def single_duo():
    running = True
    while running:
        # Custom
        screen.blit(background3, (0, 0))
        draw_text('Mode', font4, YELLOW, screen, 355, 70)

        if single_button.choose():
            return single()
        draw_text('Single', font3, BLACK, screen, 370, 265)

        if duo_button.choose():
            return duo()
        draw_text('Duo', font3, BLACK, screen, 380, 415)

        # Quit
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


single_duo()
