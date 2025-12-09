import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
COOKIE = pygame.transform.scale(pygame.image.load("Cookie.png"), (30, 30))
CLICK_COOKIE = pygame.transform.scale(pygame.image.load("Cookie.png"), (200, 200))

FONT = pygame.font.SysFont("comicsans", 30)
BUTTON_FONT = pygame.font.SysFont("comicsans", 15)
SCORE = FONT.render("+1", 1, "white")

AUTO_CLICKER_COST = 10
AUTO_CLICKERS = 0

GRANNY_COST = 100
GRANNYS = 0

ROCKING_CHAIR_COST = 1000
ROCKING_CHAIRS = 0

TREE_COST = 10000
TREES = 0
    

areas = [pygame.Rect(400, 300, 200, 200), pygame.Rect(740, 10, 250, 100), pygame.Rect(740, 120, 250, 100), pygame.Rect(740, 230, 250, 100), pygame.Rect(740, 340, 250, 100), pygame.Rect(10, 100, 250, 100)]
buttons = []
buttons_text = []
buttons_textPOS = []
button1 = BUTTON_FONT.render("Buy Auto Clicker: " + str(AUTO_CLICKER_COST), 1, "black")
button2 = BUTTON_FONT.render("Buy Granny: " + str(GRANNY_COST), 1, "black")
button3 = BUTTON_FONT.render("Buy Rocking Chair: " + str(ROCKING_CHAIR_COST), 1, "black") 
button4 = BUTTON_FONT.render("Buy Tree: " + str(TREE_COST), 1, "black")

def draw(cookies, SCALED_IMAGE, buttons, button1, button2, button3, button4, button5, button6):
    WIN.blit(BG, (0, 0))
    WIN.blit(COOKIE, (10, cookies.get_height()/2 - 5))
    WIN.blit(SCALED_IMAGE, (WIDTH/2 - SCALED_IMAGE.get_width()/2, HEIGHT/2 - SCALED_IMAGE.get_height()/2))
    
    for button in buttons:
        pygame.draw.rect(WIN, "white", button)
        WIN.blit(button1, (865 - button1.get_width()/2, 60 + button1.get_height()/3))
        WIN.blit(button2, (865 - button2.get_width()/2, 170 + button2.get_height()/3))
        WIN.blit(button3, (865 - button3.get_width()/2, 280 + button3.get_height()/3))
        WIN.blit(button4, (865 - button4.get_width()/2, 390 + button4.get_height()/3))
        WIN.blit(button5, (135 - button5.get_width()/2, 130 + button5.get_height()/3))
        WIN.blit(button6, (135 - button6.get_width()/2, 150 + button6.get_height()/3))

    WIN.blit(cookies, (50, 10))
    pygame.display.update()

def main():
    run = True

    cookies = 0
    cookies_score = FONT.render(str(0), 1, "white")
    
    clock = pygame.time.Clock()
    AUTO_CLICKERS = 0
    AUTO_CLICKER_COST  = 10
    GRANNYS = 0
    GRANNY_COST = 100
    ROCKING_CHAIRS = 0
    ROCKING_CHAIR_COST = 1000
    TREES = 0
    TREE_COST = 10000

    SPEED_COST = 1000
    SPEED = 1

    granny_count = 0
    rocking_count = 0
    tree_count = 0
    auto_interval = 1000
    auto_count = 0
    while run:
        auto_count += clock.tick(60)
        auto_interval = SPEED * 1000

        

        SCALED_COOKIE = pygame.transform.smoothscale(CLICK_COOKIE, (200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
            elif event.type == pygame.MOUSEBUTTONUP:
                if areas[0].collidepoint(event.pos):
                    cookies += 1
                    cookies_score = FONT.render(str(cookies), 1, "white")
                    SCALED_COOKIE = pygame.transform.smoothscale(CLICK_COOKIE, (210, 210))
                if areas[1].collidepoint(event.pos):
                    if cookies >= AUTO_CLICKER_COST:
                        cookies -= AUTO_CLICKER_COST
                        AUTO_CLICKERS += 1
                        AUTO_CLICKER_COST += 10
                        cookies_score = FONT.render(str(cookies), 1, "white")
                if areas[2].collidepoint(event.pos):
                    if cookies >= GRANNY_COST:
                        cookies -= GRANNY_COST
                        GRANNYS += 1
                        GRANNY_COST += 100
                        cookies_score = FONT.render(str(cookies), 1, "white")
                if areas[3].collidepoint(event.pos):
                    if cookies >= ROCKING_CHAIR_COST:
                        cookies -= ROCKING_CHAIR_COST
                        ROCKING_CHAIRS += 1
                        ROCKING_CHAIR_COST += 1000
                        cookies_score = FONT.render(str(cookies), 1, "white")
                if areas[4].collidepoint(event.pos):
                    if cookies >= TREE_COST:
                        cookies -= TREE_COST
                        TREES += 1
                        TREE_COST += 10000
                        cookies_score = FONT.render(str(cookies), 1, "white")
                if areas[5].collidepoint(event.pos):
                    if cookies >= SPEED_COST and SPEED > .1:
                        cookies -= SPEED_COST
                        SPEED = max(.1, SPEED - .1)
                        SPEED_COST *= 10
                        cookies_score = FONT.render(str(cookies), 1, "white")
                    elif SPEED == .1:
                        alert1 = BUTTON_FONT.render("Max Speed Reached", 1, "black")
                        alert1.set_alpha(255)
                        WIN.blit(alert1, (135 - button6.get_width()/2, 110))
                        pygame.display.update()
        if auto_count > auto_interval:
            cookies += AUTO_CLICKERS
            
            cookies_score = FONT.render(str(cookies), 1, "white")
            auto_count = 0
            granny_count += 1
            rocking_count += 1
            tree_count += 1
            if granny_count > 5:
                AUTO_CLICKERS += GRANNYS
                AUTO_CLICKER_COST += 10 * GRANNYS
                granny_count = 0
                BUTTON_FONT.render("Buy Auto Clicker: " + str(AUTO_CLICKER_COST), 1, "black")
            if rocking_count > 10:
                GRANNYS += ROCKING_CHAIRS
                GRANNY_COST += 100 * ROCKING_CHAIRS
                rocking_count = 0
                BUTTON_FONT.render("Buy Granny: " + str(GRANNY_COST), 1, "black")
            if tree_count > 30:
                ROCKING_CHAIRS += TREES
                ROCKING_CHAIR_COST += 1000 * TREES
                tree_count = 0
                BUTTON_FONT.render("Buy Rocking Chair: " + str(ROCKING_CHAIR_COST), 1, "black")

        for each in buttons_text:
            buttons_text.remove(each)
        buttons.append(pygame.Rect(740, 10, 250, 100))
        buttons.append(pygame.Rect(740, 120, 250, 100))
        buttons.append(pygame.Rect(740, 230, 250, 100))
        buttons.append(pygame.Rect(740, 340, 250, 100)) 
        buttons.append(pygame.Rect(10, 100, 250, 100))  
        button1 = BUTTON_FONT.render("Buy Auto Clicker: " + str(AUTO_CLICKER_COST), 1, "black")
        button2 = BUTTON_FONT.render("Buy Granny: " + str(GRANNY_COST), 1, "black") 
        button3 = BUTTON_FONT.render("Buy Rocking Chair: " + str(ROCKING_CHAIR_COST), 1, "black") 
        button4 = BUTTON_FONT.render("Buy Tree: " + str(TREE_COST), 1, "black")
        button5 = BUTTON_FONT.render("Increase Auto Speed:", 1, "black")
        button6 = BUTTON_FONT.render(str(SPEED_COST), 1, "black")    
        alert1 = BUTTON_FONT.render("Max Speed Reached", 1, "black")    

        draw(cookies_score, SCALED_COOKIE, buttons, button1, button2, button3, button4, button5, button6)
        
        
    
    pygame.quit()

if __name__ == "__main__":
    main()