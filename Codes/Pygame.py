import pygame
import time
pygame.font.init()
pygame.init()

FONT = pygame.font.SysFont("comicsans", 10, False, False)
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

CHAR_SIZE = 96
CHAR_IMAGES = []
CHAR_SHEET = pygame.transform.scale(pygame.image.load("PlayerSpriteSheet1.png"), (2 * CHAR_SIZE, 2 * CHAR_SIZE))
CHAR_STAND = CHAR_SHEET.subsurface((0, 0, CHAR_SIZE, CHAR_SIZE))
CHAR_WALK_1 = CHAR_SHEET.subsurface((CHAR_SIZE, 0, CHAR_SIZE, CHAR_SIZE))
CHAR_WALK_2 = CHAR_SHEET.subsurface((0, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE))
CHAR_IMAGES.append(CHAR_STAND)
CHAR_IMAGES.append(CHAR_WALK_1)
CHAR_IMAGES.append(CHAR_WALK_2)
char_x = 200
char_y = HEIGHT - 2 * CHAR_STAND.get_height()

clock = pygame.time.Clock()


def draw(char_x, char_y, char):
    WIN.blit(BG, (0, 0))
    WIN.blit(char, (char_x, char_y))
    
    pygame.display.update()


def main():
    #Initializing Variables
    char_x = 200
    char_y = HEIGHT - CHAR_SIZE
    run = True
    char = CHAR_SHEET.subsurface((0, 0, CHAR_SIZE, CHAR_SIZE))
    char_image = 0
    char_image_2 = 0
    walk_ani_speed = 5 #Higher is longer

    #Flags
    d_flag = False
    a_flag = False
    walking = False
    walking_steps = 0
    while run:
        clock.tick(30)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            #Flags
            if event.type == pygame.MOUSEBUTTONDOWN:
                d_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    d_flag = True
                    walking = True
                if event.key == pygame.K_a:
                    a_flag = True
                    walking = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    d_flag = False
                    walking = False
                if event.key == pygame.K_a:
                    a_flag = False
                    walking = False
        if d_flag and not a_flag:
            #char_x += 5
            if char_image >= 0:
                char_image -= 1
                for x in range(1, len(CHAR_IMAGES)):
                    if x <= char_image < walk_ani_speed * x:
                        char_image_2 = x - 1
                char = CHAR_IMAGES[ char_image_2 ]
                walking_steps -= 1
            else:
                char_image = walk_ani_speed * len(CHAR_IMAGES) - 2
                char = CHAR_STAND
        
        if a_flag and not d_flag:
            #char_x -= 5
            if char_image >= 0:
                char_image -= 1
                for x in range(1, len(CHAR_IMAGES)):
                    if x <= char_image < walk_ani_speed * x:
                        char_image_2 = x - 1
                char = CHAR_IMAGES[ char_image_2 ]
                walking_steps -= 1
            else:
                char_image = walk_ani_speed * len(CHAR_IMAGES)
                char = CHAR_STAND
        draw(char_x, char_y, char)



if __name__ == "__main__":
    main()