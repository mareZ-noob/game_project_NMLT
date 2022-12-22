import pygame
import random
import sys
from pygame.locals import *
from pygame import mixer

# Start
mainClock = pygame.time.Clock()
pygame.init()

# Custom
pygame.display.set_caption('Game Easy')
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font3 = pygame.font.SysFont(None, 32)
font4 = pygame.font.Font('freesansbold.ttf', 40)

background = pygame.image.load("garden.png").convert()
background1 = pygame.image.load("bg.jpg").convert()
background2 = pygame.image.load("spaceshipwindow.jpg").convert()
background3 = pygame.image.load("casino.jpg").convert()

# Back, exit button
back_img = pygame.image.load("hongback.png").convert()
exit_img = pygame.image.load("red.png").convert()
solo_img = pygame.image.load("orange.png").convert()

# Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

DARK_GREEN = (10, 50, 10)
ORANGE = (238, 141, 70)


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if action == True:
            main_menu()

    def exit(self):
        action1 = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action1 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action1

    def solo(self):
        action2 = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action2 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if action2 == True:
            main_game()

    def return_music(self):
        action3 = False
        # mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions, 0 right click, 1 middle click, 2 left click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action3 = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action3


back_button = Button(0, 0, back_img, 0.4)
exit_button = Button(500, 400, exit_img, 1)
solo_button = Button(100, 250, solo_img, 1)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


cur_music = 'LanCuoi.wav'
mixer.init()
mixer.music.load(cur_music)
mixer.music.play(-1)

click = False


def main_menu():
    global click
    running = True
    while running:
        # screen.fill(WHITE)
        screen.blit(background3, (0, 0))
        draw_text('Game Menu', font4, YELLOW, screen, 290, 120)
        mx, my = pygame.mouse.get_pos()
        # Exit Button
        if exit_button.exit():
            pygame.quit()
            sys.exit()
        # Trái, Khoảng cách, Chiều dài, Chiều rộng
        # Play
        # button_1 = pygame.Rect(100, 250, 200, 50)
        # Options
        button_2 = pygame.Rect(500, 250, 200, 50)
        # Settings
        button_3 = pygame.Rect(100, 400, 200, 50)

        # pygame.draw.rect(screen, ORANGE, button_1)
        solo_button.solo()
        draw_text('Solo', font3, BLACK, screen, 180, 265)
        pygame.draw.rect(screen, MAGENTA, button_2)
        draw_text('Options', font3, BLACK, screen, 560, 265)
        pygame.draw.rect(screen, CYAN, button_3)
        draw_text('Settings', font3, BLACK, screen, 155, 415)
        draw_text('Quit', font3, BLACK, screen, 575, 415)


        # if button_1.collidepoint((mx, my)):
        #     if click:
        #         game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                settings()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    global click
    running = True
    while running:
        screen.blit(background3, (0, 0))
        back_button.draw()
        draw_text('Difficulty', font4, YELLOW, screen, 325, 80)
        ox, oy = pygame.mouse.get_pos()

        # Trái, Khoảng cách, Chiều dài, Chiều rộng
        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)

        # x,y
        pygame.draw.rect(screen, BLUE, button_1)
        draw_text('Easy', font3, BLACK, screen, 375, 215)
        pygame.draw.rect(screen, MAGENTA, button_2)
        draw_text('Hard', font3, BLACK, screen, 375, 315)
        pygame.draw.rect(screen, CYAN, button_3)
        draw_text('Supper Hard', font3, BLACK, screen, 335, 415)
        solo_button.solo()
        if button_1.collidepoint((ox, oy)):
            if click:
                pass
        if button_2.collidepoint((ox, oy)):
            if click:
                pass
        if button_3.collidepoint((ox, oy)):
            if click:
                pass

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


def options():
    running = True
    while running:
        screen.blit(background3, (0, 0))
        back_button.draw()
        draw_text('Options', font4, YELLOW, screen, 330, 80)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def settings():
    global click
    running = True
    while running:
        screen.blit(background3, (0, 0))
        draw_text('Settings', font4, YELLOW, screen, 325, 70)
        draw_text('Choose your music: ', font3, YELLOW, screen, 290, 150)
        px, py = pygame.mouse.get_pos()

        # back_button.draw()
        back_button.draw()

        # Button Trái, Khoảng cách, Chiều dài, Chiều rộng
        button_1 = pygame.Rect(80, 200, 200, 50)
        button_2 = pygame.Rect(80, 300, 200, 50)
        button_3 = pygame.Rect(80, 400, 200, 50)
        button_4 = pygame.Rect(300, 200, 200, 50)
        button_5 = pygame.Rect(300, 300, 200, 50)
        button_6 = pygame.Rect(300, 400, 200, 50)
        button_7 = pygame.Rect(520, 200, 200, 50)
        button_8 = pygame.Rect(520, 300, 200, 50)
        button_9 = pygame.Rect(520, 400, 200, 50)

        pygame.draw.rect(screen, BLUE, button_1)
        draw_text('Lan Cuoi', font3, BLACK, screen, 135, 215)
        pygame.draw.rect(screen, MAGENTA, button_2)
        draw_text('Among Us', font3, BLACK, screen, 125, 315)
        pygame.draw.rect(screen, CYAN, button_3)
        draw_text('MNKM', font3, BLACK, screen, 145, 415)
        pygame.draw.rect(screen, RED, button_4)
        draw_text('Em Trang Tri', font3, BLACK, screen, 330, 215)
        pygame.draw.rect(screen, GREEN, button_5)
        draw_text('Renai Circulation', font3, BLACK, screen, 305, 315)
        pygame.draw.rect(screen, MAGENTA, button_6)
        draw_text('Pink Panther', font3, BLACK, screen, 330, 415)
        pygame.draw.rect(screen, BLUE, button_7)
        draw_text('Doraemon', font3, BLACK, screen, 565, 215)
        pygame.draw.rect(screen, MAGENTA, button_8)
        draw_text('Always With Me', font3, BLACK, screen, 540, 315)
        pygame.draw.rect(screen, CYAN, button_9)
        draw_text('Merry Go Ground', font3, BLACK, screen, 530, 415)

        if button_1.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('LanCuoi.wav')
                mixer.music.play(-1)
        if button_2.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('AmongUsThemeSong.wav')
                mixer.music.play(-1)
        if button_3.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('motngaykhongmua.wav')
                mixer.music.play(-1)
        if button_4.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('emtrangtri.wav')
                mixer.music.play(-1)
        if button_5.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('RenaiCirculation.wav')
                mixer.music.play(-1)
        if button_6.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('PinkPanther.wav')
                mixer.music.play(-1)
        if button_7.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('Doraemon.wav')
                mixer.music.play(-1)
        if button_8.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('AlwaysWithMe.wav')
                mixer.music.play(-1)
        if button_9.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('MerryGoRoundofLifeHowl_sMovingCastle.wav')
                mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def main_game():
    BURGER_BEGIN_SPEED = 6
    ACCELERATION = .1
    DOG_DEFAULT_SPEED = 8
    DOG_BOOST_SPEED = 20
    DOG_BEGIN_BOOST_LEVEL = 100
    DOG_LIVES = 4
    boost_level = DOG_BEGIN_BOOST_LEVEL
    point = 0
    lives = DOG_LIVES
    dog_speed = DOG_DEFAULT_SPEED

    # Load Music
    bark_sound = pygame.mixer.Sound("bark_sound.wav")
    miss_sound = pygame.mixer.Sound("miss.mp3")
    boost_sound = pygame.mixer.Sound("boost_sound.wav")
    game_over_sound = pygame.mixer.Sound("gameover.wav")
    pygame.mixer.music.load('AmongUsThemeSong.wav')
    pygame.mixer.music.set_volume(.4)


    # Load DOG
    right_dog = pygame.image.load("right_dog.png")
    left_dog = pygame.image.load("left_dog.png")
    dog = right_dog
    dog_rect = dog.get_rect()
    dog_rect.centerx = WINDOW_WIDTH/2
    dog_rect.bottom = WINDOW_HEIGHT
    meat = pygame.image.load("meat.png")
    meat_rect = meat.get_rect()

    # Load Text
    font = pygame.font.Font('font.ttf', 32)
    font2 = pygame.font.Font('font.ttf', 46)

    point_text = font.render(f'Point:  {point}', True, GREEN,BLACK)
    point_text_rect = point_text.get_rect()
    point_text_rect.topleft = (132, 32)

    live_text = font.render(f'Lives:  {lives}',True, GREEN, BLACK)
    live_text_rect = live_text.get_rect()
    live_text_rect.topright = (668, 32)

    game_over_text = font2.render("GAME OVER, PRESS ENTER TO CONTINUE!", True, ORANGE, GREEN)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

    boost_text = font.render(f'BOOST ENERGY:  {boost_level}', True, ORANGE,BLACK)
    boost_text_rect = boost_text.get_rect()
    boost_text_rect.centerx = WINDOW_WIDTH // 2
    boost_text_rect.y = 32


    # BEGIN GAME
    pygame.mixer.music.play(-1)
    boost_level = DOG_BEGIN_BOOST_LEVEL
    point = 0
    lives = DOG_LIVES
    dog_speed = DOG_DEFAULT_SPEED
    dog_rect.centerx = WINDOW_WIDTH/2
    dog_rect.bottom = WINDOW_HEIGHT
    meat_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
    burger_speed = BURGER_BEGIN_SPEED

    # MAIN GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control the Dog
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dog_rect.left > 0:
            dog_rect.x -= dog_speed
            dog = left_dog

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dog_rect.right < WINDOW_WIDTH:
            dog_rect.x += dog_speed
            dog = right_dog

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and dog_rect.top > 100:
            dog_rect.y -= dog_speed

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dog_rect.bottom < WINDOW_HEIGHT:
            dog_rect.y += dog_speed

        if keys[pygame.K_SPACE] and boost_level > 0:
            boost_level -= 1
            if dog_speed != DOG_BOOST_SPEED:
                boost_sound.play()
            dog_speed = DOG_BOOST_SPEED

        else:
            dog_speed = DOG_DEFAULT_SPEED
            boost_sound.stop()

        # Move the Meat
        meat_rect.y += burger_speed

        # Check Meat
        if meat_rect.colliderect(dog_rect):
            point += 1
            burger_speed += ACCELERATION
            boost_level += 50
            meat_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
            bark_sound.play()
        if meat_rect.y > WINDOW_HEIGHT:
            miss_sound.play()
            lives -= 1
            meat_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)

        # Refresh the SCREEN
        screen.blit(background2, (0, 0))
        back_button.draw()

        # Load Text ReRender
        point_text = font.render(f'Point:  {point}', True, GREEN,BLACK)
        boost_text = font.render(f'BOOST ENERGY:  {boost_level}', True, ORANGE,BLACK)
        live_text = font.render(f'Lives:  {lives}',True, GREEN, BLACK)
        screen.blit(boost_text, boost_text_rect)
        screen.blit(point_text, point_text_rect)
        screen.blit(live_text, live_text_rect)
        pygame.draw.line(screen, DARK_GREEN ,(0, 97), (WINDOW_WIDTH, 97),3)

        #Check lose
        if lives == 0:
            pause = True
            game_over_sound.play()
            while pause:
                screen.blit(game_over_text, game_over_text_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pause = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pause = False
                            game_over_sound.stop()
                            pygame.mixer.music.play(-1)
                            boost_level = DOG_BEGIN_BOOST_LEVEL
                            point = 0
                            lives = DOG_LIVES
                            dog_speed = DOG_DEFAULT_SPEED
                            dog_rect.centerx = WINDOW_WIDTH / 2
                            dog_rect.bottom = WINDOW_HEIGHT
                            meat_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
                            burger_speed = BURGER_BEGIN_SPEED

        #Load the dog
        screen.blit(dog, dog_rect)
        screen.blit(meat, meat_rect)

        #UPDATE DISPLAY AND SET CLOCK
        pygame.display.update()
        mainClock.tick(60)

    pygame.quit()



main_menu()
pygame.quit()

