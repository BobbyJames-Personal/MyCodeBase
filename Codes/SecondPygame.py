import pygame
import random
import time
import math
pygame.font.init()
pygame.init()
 
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Moving Game")

FONT = pygame.font.SysFont("comicsans", 30)
IMAGE = pygame.image.load("CharacterPoses\CharacterSpriteSheet4.png")
BG = pygame.transform.scale((pygame.image.load("bg.jpeg")), (WIDTH, HEIGHT))


def draw(char_x, char_y, draw_sprite, rotation_fix_x, rotation_fix_y):
    WIN.blit(BG, (0, 0))
    WIN.blit(draw_sprite, (char_x - rotation_fix_x, char_y - rotation_fix_y))
    WIN.blit(FONT.render("Max Speed Reached", 1, "white"), (500, 100))
    
    pygame.display.update()

#Character sprites
CHAR_DRAWN = IMAGE.subsurface((0, 0, 192, 192))
CHAR_SWING = IMAGE.subsurface((192, 0, 192, 192))
CHAR_REST_2 = IMAGE.subsurface((0, 192, 192, 192))
CHAR_REST_1 = IMAGE.subsurface((192, 192, 192, 192))
CHAR_SLASH = IMAGE.subsurface((0, 384, 192, 192))

CHARACTER_SPRITES = [CHAR_DRAWN, CHAR_SWING, CHAR_REST_2, CHAR_REST_1, CHAR_SLASH]



def main():
    #Initializes the variables
    current_sprite = CHAR_REST_1
    draw_sprite = current_sprite
    sword_drawn = False
    direction = "right"
    run = True
    clock = pygame.time.Clock()
    draw_sprite = CHAR_REST_1
    char_x, char_y = 250, 150
    w_flag = False 
    s_flag = False 
    a_flag = False 
    d_flag = False 
    rclick_flag = False 
    speed = 10
    rotation_fix_x = current_sprite.get_width() / 3
    rotation_fix_y = current_sprite.get_height() / 3
    target_y = 0
    target_x = 0
    while run:
        deltatime = clock.tick(30)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            if event.type == pygame.QUIT:
                run = False
                break
        #Testing
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    draw_sprite = CHARACTER_SPRITES[2]
        #Turns on movement flags
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_q]:
                    if sword_drawn == True:
                        sword_drawn = False
                        current_sprite = CHAR_REST_1
                        draw_sprite = pygame.transform.rotate(current_sprite, direction)
                    else: 
                        sword_drawn = True
                        current_sprite = CHAR_DRAWN
                        draw_sprite = pygame.transform.rotate(current_sprite, direction)
                if keys[pygame.K_w]:
                    w_flag = True
                if keys[pygame.K_s]:
                    s_flag = True
                if keys[pygame.K_a]:
                    a_flag = True
                if keys[pygame.K_d]:
                    d_flag = True
        #Turns off movement flags    
            elif event.type == pygame.KEYUP:
                if not keys[pygame.K_w]:
                    w_flag = False
                if not keys[pygame.K_s]:
                    s_flag = False
                if not keys[pygame.K_a]:
                    a_flag = False
                if not keys[pygame.K_d]:
                    d_flag = False
        #Sprite flags
        
        if d_flag == True:
            if sword_drawn == True:
                current_sprite = CHAR_DRAWN
                draw_sprite = pygame.transform.rotate(current_sprite, -90)
                direction = -90
            else:
                current_sprite = CHAR_REST_1
                draw_sprite = pygame.transform.rotate(current_sprite, -90)
                direction = -90
        if a_flag == True:  
            if sword_drawn == True:
                current_sprite = CHAR_DRAWN
                draw_sprite = pygame.transform.rotate(current_sprite, 90)
                direction = 90
            else:
                current_sprite = CHAR_REST_1
                draw_sprite = pygame.transform.rotate(current_sprite, 90)
                direction = 90
        if w_flag == True:
            if sword_drawn == True:
                current_sprite = CHAR_DRAWN
                draw_sprite = pygame.transform.rotate(current_sprite, 0)
                direction = 0
            else:
                current_sprite = CHAR_REST_1
                draw_sprite = pygame.transform.rotate(current_sprite, 0)
                direction = 0
        if s_flag == True:
            if sword_drawn == True:
                current_sprite = CHAR_DRAWN
                draw_sprite = pygame.transform.rotate(current_sprite, 180)
                direction = 180
            else:
                current_sprite = CHAR_REST_1
                draw_sprite = pygame.transform.rotate(current_sprite, 180)
                direction = 180
        
        #Movement flags
        if w_flag or s_flag or a_flag or d_flag:
            if w_flag and not a_flag or d_flag:
                target_y -= speed
            if s_flag and not a_flag or d_flag:
                target_y += speed
            if a_flag and not s_flag or w_flag: 
                target_x -= speed
            if d_flag and not s_flag or w_flag:
                target_x += speed
            if (w_flag or s_flag) and a_flag:
                if w_flag:
                    draw_sprite = pygame.transform.rotate(current_sprite, 45)
                    direction =45
                else:
                    draw_sprite = pygame.transform.rotate(current_sprite, 135)
                    direction = 135
            if (w_flag or s_flag) and d_flag:
                if w_flag:
                    draw_sprite = pygame.transform.rotate(current_sprite, 315)
                    direction = 315
                else:
                    draw_sprite = pygame.transform.rotate(current_sprite, 225)
                    direction = 225
            #Movement, normalized using the direction
            target_pos = (target_x, target_y)
            char_pos = (char_x, char_y)
            vec = (target_x - char_x, target_y - char_y)
            direction = math.normalize(vec)
            velocity = direction * speed
        draw(char_x, char_y, draw_sprite, rotation_fix_x, rotation_fix_y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pygame.quit()

if __name__ == "__main__":
    main()