import pygame
import random
import sys
from pygame.locals import *
from pygame import mixer

# Start
mainClock = pygame.time.Clock()
pygame.init()

# Custom
pygame.display.set_caption('Catching Fruits')
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font3 = pygame.font.SysFont(None, 32)
font4 = pygame.font.Font('./fonts/freesansbold.ttf', 40)

# Load background
background = pygame.image.load("./images/spacegame.jpg").convert()
background1 = pygame.image.load("./images/forrest.png").convert()
background2 = pygame.image.load("./images/triet.png").convert()
background3 = pygame.image.load("./images/casino.jpg").convert()
background4 = pygame.image.load("./images/spirited.jpg").convert()
cur_bg = background2

# Back, exit button
back_img = pygame.image.load("./images/hongback.png").convert()
exit_img = pygame.image.load("./images/red.png").convert()
solo_img = pygame.image.load("./images/orange.png").convert()
music_back_img = pygame.image.load("./images/red.png").convert()
choose_bg_img = pygame.image.load("./images/spirited.jpg").convert()
choose_bg_img2 = pygame.image.load("./images/forrest.png").convert()
choose_bg_img3 = pygame.image.load("./images/spacegame.jpg").convert()

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
SKY = (0,191,255)

SEA = (84,255,159)
SALMON = (250,128,114)

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
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if action:
            main_menu(cur_music)

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
        if action2 == True:
            main_game(cur_music, cur_bg)

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


# Load button
back_button = Button(0, 0, back_img, 0.4)
exit_button = Button(320, 545, exit_img, 0.8)
solo_button = Button(100, 250, solo_img, 1)
music_back_button = Button(0, 0, back_img, 0.4)
choose_bg_button = Button(100, 300, choose_bg_img, 0.2)
choose_bg_button2 = Button(300, 300, choose_bg_img2, 0.2)
choose_bg_button3 = Button(500, 300, choose_bg_img3, 0.2)


# Current music
cur_music = './sounds/AlwaysWithMe.wav'


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu(cur_music):
    global click
    running = True
    pygame.mixer.init()
    pygame.mixer.music.load(cur_music)
    pygame.mixer.music.play(-1)
    while running:
        # Custom
        screen.blit(background3, (0, 0))
        draw_text('Game Menu', font4, YELLOW, screen, 290, 120)
        mx, my = pygame.mouse.get_pos()

        # Exit Button
        if exit_button.exit():
            pygame.quit()
            sys.exit()

        # Button
        button_1 = pygame.Rect(500, 250, 200, 50)
        button_2 = pygame.Rect(100, 400, 200, 50)
        button_3 = pygame.Rect(500, 400, 200, 50)
        solo_button.solo()

        # Text
        draw_text('Play', font3, BLACK, screen, 180, 265)
        pygame.draw.rect(screen, SEA, button_1)
        draw_text('Background', font3, BLACK, screen, 540, 265)
        pygame.draw.rect(screen, CYAN, button_2)
        draw_text('Setting', font3, BLACK, screen, 165, 415)
        pygame.draw.rect(screen, SALMON, button_3)
        draw_text('High Score', font3, BLACK, screen, 545, 415)
        draw_text('Quit', font3, BLACK, screen, 380, 555)

        # Choose
        if button_1.collidepoint((mx, my)):
            if click:
                options()
        if button_2.collidepoint((mx, my)):
            if click:
                settings()
        if button_3.collidepoint((mx, my)):
            if click:
                show_high_score_from_file("./data/highscore.txt")

        # Exit
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


def options():
    global click
    running = True
    while running:
        # Background
        screen.blit(background3, (0, 0))

        # Back Button
        if music_back_button.return_music():
            return main_menu(cur_music)
        draw_text('Background', font4, YELLOW, screen, 290, 120)

        # Select background
        if choose_bg_button.choose_background():
            cur_bg = background4
            return main_game(cur_music, cur_bg)
        if choose_bg_button2.choose_background():
            cur_bg = background1
            return main_game(cur_music, cur_bg)
        if choose_bg_button3.choose_background():
            cur_bg = background
            return main_game(cur_music, cur_bg)

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


def settings():
    global click, cur_music
    running = True
    while running:
        # Background
        screen.blit(background3, (0, 0))
        draw_text('Setting', font4, YELLOW, screen, 335, 70)
        draw_text('Choose your music: ', font3, YELLOW, screen, 290, 150)
        px, py = pygame.mouse.get_pos()

        # Button
        button_1 = pygame.Rect(80, 200, 200, 50)
        button_2 = pygame.Rect(80, 300, 200, 50)
        button_3 = pygame.Rect(80, 400, 200, 50)
        button_4 = pygame.Rect(300, 200, 200, 50)
        button_5 = pygame.Rect(300, 300, 200, 50)
        button_6 = pygame.Rect(300, 400, 200, 50)
        button_7 = pygame.Rect(520, 200, 200, 50)
        button_8 = pygame.Rect(520, 300, 200, 50)
        button_9 = pygame.Rect(520, 400, 200, 50)

        # Text & Music
        pygame.draw.rect(screen, CYAN, button_1)
        draw_text('HCTS', font3, BLACK, screen, 150, 215)
        pygame.draw.rect(screen, (238, 220, 130), button_2)
        draw_text('Among Us', font3, BLACK, screen, 125, 315)
        pygame.draw.rect(screen, (255, 182, 193), button_3)
        draw_text('Don Xuan', font3, BLACK, screen, 130, 415)
        pygame.draw.rect(screen, (127, 255, 212), button_4)
        draw_text('In My Life', font3, BLACK, screen, 350, 215)
        pygame.draw.rect(screen, (238, 154, 73), button_5)
        draw_text('Renai Circulation', font3, BLACK, screen, 305, 315)
        pygame.draw.rect(screen, (240, 128, 128), button_6)
        draw_text('Lan Cuoi', font3, BLACK, screen, 355, 415)
        pygame.draw.rect(screen, (193, 255, 193), button_7)
        draw_text('Doraemon', font3, BLACK, screen, 565, 215)
        pygame.draw.rect(screen, (255, 128, 0), button_8)
        draw_text('Always With Me', font3, BLACK, screen, 540, 315)
        pygame.draw.rect(screen, (255, 106, 106 ), button_9)
        draw_text('Merry Go Ground', font3, BLACK, screen, 530, 415)

        # Choose
        if button_1.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/HCTS.wav')
                mixer.music.play(-1)
                cur_music = './sounds/HCTS.wav'
        if button_2.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/AmongUsThemeSong.wav')
                mixer.music.play(-1)
                cur_music = './sounds/AmongUsThemeSong.wav'
        if button_3.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/DonXuan.wav')
                mixer.music.play(-1)
                cur_music = './sounds/DonXuan.wav'
        if button_4.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/InMyLife_Beat.wav')
                mixer.music.play(-1)
                cur_music = './sounds/InMyLife_Beat.wav'
        if button_5.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/RenaiCirculation.wav')
                mixer.music.play(-1)
                cur_music = './sounds/RenaiCirculation.wav'
        if button_6.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/LanCuoi.wav')
                mixer.music.play(-1)
                cur_music = './sounds/LanCuoi.wav'
        if button_7.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/Doraemon.wav')
                cur_music = './sounds/Doraemon.wav'
                mixer.music.play(-1)
        if button_8.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/AlwaysWithMe.wav')
                mixer.music.play(-1)
                cur_music = './sounds/AlwaysWithMe.wav'
        if button_9.collidepoint((px, py)):
            if click:
                mixer.init()
                mixer.music.load('./sounds/MerryGoRoundofLifeHowl_sMovingCastle.wav')
                mixer.music.play(-1)
                cur_music = './sounds/MerryGoRoundofLifeHowl_sMovingCastle.wav'

        # Back button
        if music_back_button.return_music():
            return main_menu(cur_music)

        # Quit
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


# Read from file
def best():
    with open("./data/highscore.txt", "r") as f:
        return f.read()

def show_high_score_from_file(filename):
    global click
    running = True
    while running:
        # Background
        screen.blit(background3, (0, 0))

        # Set the initial high score to 0
        high_score = 0

        # Try to open the high score file and read the high score from it
        try:
            with open(filename, "r") as f:
                high_score = int(f.read())
        except FileNotFoundError:
            high_score = 0
        except ValueError:
            high_score = 0
        draw_text('High Score' + ': ' + str(high_score), font4, YELLOW, screen, 250, 300)

        # Back button
        if music_back_button.return_music():
            return main_menu(cur_music)

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


def main_game(cur_music, cur_bg):
    FALL_BEGIN_SPEED = 6
    ACCELERATION = .1
    BOWL_DEFAULT_SPEED = 8
    BOWL_BOOST_SPEED = 20
    BOWL_BEGIN_BOOST_LEVEL = 100
    BOWL_LIVES = 100
    boost_level = BOWL_BEGIN_BOOST_LEVEL
    point = 0
    lives = BOWL_LIVES
    bowl_speed = BOWL_DEFAULT_SPEED

    try:
        high_score = int(best())
    except:
        high_score = 0

    # Load music
    bark_sound = pygame.mixer.Sound("./sounds/achieve_complete.wav")
    bark_sound.set_volume(0.4)
    miss_sound = pygame.mixer.Sound("./sounds/siu.wav")
    boost_sound = pygame.mixer.Sound("./sounds/quickswhooshingnoise.wav")
    game_over_sound = pygame.mixer.Sound("./sounds/gameover.wav")
    game_win_sound = pygame.mixer.Sound("./sounds/goodresult.wav")
    pygame.mixer.music.load(cur_music)

    # Load bowl
    right_bowl = pygame.image.load("./images/bowl.png")
    left_bowl = pygame.image.load("./images/bowl.png")
    bowl = right_bowl
    bowl_rect = bowl.get_rect()
    bowl_rect.centerx = WINDOW_WIDTH / 2
    bowl_rect.bottom = WINDOW_HEIGHT

    # Create a list of file paths for the images
    image_paths = ['./images/apple.png', './images/banana.png', './images/carrot.png',
                   './images/coconut.png', './images/luffy.png', './images/kaido.png',
                   './images/lemon.png', './images/trai_dao.png', './images/strawberry.png',
                   './images/trai_cam.png', './images/watermelon.png']

    # Load the images and store them in a list
    images = []
    for path in image_paths:
        image = pygame.image.load(path)
        images.append(image)

    # Choose a random image
    random_image = random.choice(images)

    # fruit = pygame.image.load("./images/apple.png")
    random_image_rect = random_image.get_rect()
    fruit = random_image
    fruit_rect = fruit.get_rect()

    # Load Text
    font = pygame.font.Font('./fonts/font.ttf', 32)
    font2 = pygame.font.Font('./fonts/font.ttf', 46)

    point_text = font.render(f'Point:  {point}', True, GREEN, BLACK)
    point_text_rect = point_text.get_rect()
    point_text_rect.topleft = (132, 32)

    live_text = font.render(f'Lives:  {lives}', True, GREEN, BLACK)
    live_text_rect = live_text.get_rect()
    live_text_rect.topright = (668, 32)

    game_over_text = font2.render("GAME OVER, PRESS ENTER TO CONTINUE!", True, ORANGE, GREEN)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)

    game_win_text = font2.render("YOU WIN, PRESS F TO PlAY AGAIN!", True, ORANGE, GREEN)
    game_win_text_rect = game_win_text.get_rect()
    game_win_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)

    boost_text = font.render(f'BOOST ENERGY:  {boost_level}', True, ORANGE, BLACK)
    boost_text_rect = boost_text.get_rect()
    boost_text_rect.centerx = WINDOW_WIDTH // 2
    boost_text_rect.y = 32

    # Begin game
    pygame.mixer.music.play(1) # -1 -> delete 425 -> 427, 531 -> 554.
    boost_level = BOWL_BEGIN_BOOST_LEVEL
    point = 0
    lives = BOWL_LIVES
    bowl_speed = BOWL_DEFAULT_SPEED
    bowl_rect.centerx = WINDOW_WIDTH / 2
    bowl_rect.bottom = WINDOW_HEIGHT
    fruit_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
    fall_speed = FALL_BEGIN_SPEED

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control the bowl
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and bowl_rect.left > 0:
            bowl_rect.x -= bowl_speed
            bowl = left_bowl

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and bowl_rect.right < WINDOW_WIDTH:
            bowl_rect.x += bowl_speed
            bowl = right_bowl

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and bowl_rect.top > 100:
            bowl_rect.y -= bowl_speed

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and bowl_rect.bottom < WINDOW_HEIGHT:
            bowl_rect.y += bowl_speed

        if keys[pygame.K_SPACE] and boost_level > 0:
            boost_level -= 1
            if bowl_speed != BOWL_BOOST_SPEED:
                boost_sound.play()
            bowl_speed = BOWL_BOOST_SPEED

        else:
            bowl_speed = BOWL_DEFAULT_SPEED
            boost_sound.stop()

        # Move the fruit
        fruit_rect.y += fall_speed

        # Check fruit
        if fruit_rect.colliderect(bowl_rect):
            point += 1
            fall_speed += ACCELERATION
            boost_level += 50
            fruit_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
            bark_sound.play()
        if fruit_rect.y > WINDOW_HEIGHT:
            miss_sound.play()
            lives -= 1
            fruit_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)

        # Refresh the screen
        screen.blit(cur_bg, (0, 0))
        back_button.back()

        # Load text rerender
        point_text = font.render(f'Point:  {point}', True, GREEN, BLACK)
        boost_text = font.render(f'BOOST ENERGY:  {boost_level}', True, ORANGE, BLACK)
        live_text = font.render(f'Lives:  {lives}', True, GREEN, BLACK)
        screen.blit(boost_text, boost_text_rect)
        screen.blit(point_text, point_text_rect)
        screen.blit(live_text, live_text_rect)
        pygame.draw.line(screen, DARK_GREEN, (0, 97), (WINDOW_WIDTH, 97), 3)

        # Check highscore
        if (high_score < point):
            high_score = point
        with open("./data/highscore.txt", "w") as f:
            f.write(str(high_score))

        # Check lose
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
                            boost_level = BOWL_BEGIN_BOOST_LEVEL
                            point = 0
                            lives = BOWL_LIVES
                            bowl_speed = BOWL_DEFAULT_SPEED
                            bowl_rect.centerx = WINDOW_WIDTH / 2
                            bowl_rect.bottom = WINDOW_HEIGHT
                            fruit_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
                            fall_speed = FALL_BEGIN_SPEED

        # Check win
        if not pygame.mixer.music.get_busy():
            stop = True
            game_win_sound.play()
            while stop:
                screen.blit(game_win_text, game_win_text_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        stop = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                            stop = False
                            game_win_sound.stop()
                            pygame.mixer.music.play(-1)
                            boost_level = BOWL_BEGIN_BOOST_LEVEL
                            point = 0
                            lives = BOWL_LIVES
                            bowl_speed = BOWL_DEFAULT_SPEED
                            bowl_rect.centerx = WINDOW_WIDTH / 2
                            bowl_rect.bottom = WINDOW_HEIGHT
                            fruit_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
                            fall_speed = FALL_BEGIN_SPEED

        # Load the bowl
        screen.blit(bowl, bowl_rect)
        screen.blit(fruit, fruit_rect)

        # Update display and set clock
        pygame.display.update()
        mainClock.tick(60)

    pygame.quit()


main_menu(cur_music)
pygame.quit()
