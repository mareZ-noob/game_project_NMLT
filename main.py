import pygame, random

pygame.init()

#Set display sureface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#FPS AND Clock
clock = pygame.time.Clock()
FPS = 60
background3 = pygame.image.load("casino.jpg").convert()
#Define Colors
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
GREEN      = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
ORANGE     = (238, 141, 70)

#Game Value
def choi():
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

    #Load Music
    bark_sound = pygame.mixer.Sound("bark_sound.wav")
    miss_sound = pygame.mixer.Sound("miss.mp3")
    boost_sound = pygame.mixer.Sound("boost_sound.wav")
    game_over_sound = pygame.mixer.Sound("gameover.wav")
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(.4)


    #Load DOG
    right_dog = pygame.image.load("right_dog.png")
    left_dog = pygame.image.load("left_dog.png")
    dog = right_dog
    dog_rect = dog.get_rect()
    dog_rect.centerx = WINDOW_WIDTH/2
    dog_rect.bottom = WINDOW_HEIGHT
    meat = pygame.image.load("meat.png")
    meat_rect = meat.get_rect()

    #Load Text
    font = pygame.font.Font('font.ttf', 32)
    font2 = pygame.font.Font('font.ttf', 46)

    point_text = font.render(f'Point:  {point}', True, GREEN,BLACK)
    point_text_rect = point_text.get_rect()
    point_text_rect.topleft = (32, 32)

    live_text = font.render(f'Lives:  {lives}',True, GREEN, BLACK)
    live_text_rect = live_text.get_rect()
    live_text_rect.topright = (WINDOW_WIDTH - 32, 32)

    game_over_text = font2.render("GAME OVER, PRESS ENTER TO CONTINUE!", True, ORANGE, GREEN)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

    boost_text = font.render(f'BOOST ENERGY:  {boost_level}', True, ORANGE,BLACK)
    boost_text_rect = boost_text.get_rect()
    boost_text_rect.centerx = WINDOW_WIDTH // 2
    boost_text_rect.y = 32


    #BEGIN GAME
    pygame.mixer.music.play(-1)
    boost_level = DOG_BEGIN_BOOST_LEVEL
    point = 0
    lives = DOG_LIVES
    dog_speed = DOG_DEFAULT_SPEED
    dog_rect.centerx = WINDOW_WIDTH/2
    dog_rect.bottom = WINDOW_HEIGHT
    meat_rect.bottomleft = (random.randint(0, WINDOW_WIDTH - 72), 100)
    burger_speed = BURGER_BEGIN_SPEED

    #MAIN GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Control the Dog
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

        #Move the Meat
        meat_rect.y += burger_speed

        #Check Meat
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

        #Refresh the SCREEN
        screen.blit(background3, (0, 0))

        #Load Text ReRender
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
        clock.tick(FPS)

    pygame.quit()


choi()