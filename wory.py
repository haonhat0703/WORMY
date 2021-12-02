#       {}     []
import pygame, sys, random
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("wormy")
clock = pygame.time.Clock()

score_font = pygame.font.SysFont("comicsansms", 35)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

foodx = round(random.randrange(10, 750))
foody = round(random.randrange(10, 750))

score = 0
vt_x_change = 8
vt_y_change = 0
vt_x = 300
vt_y = 300
SIZE_SNAKE = 20
snake_list = []

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, RED)
    screen.blit(value, [300, 0])
    
def draw_snake(SIZE_SNAKE, snake_list):
    for snake in snake_list:
        pygame.draw.rect(screen, BLUE, [snake[0], snake[1], SIZE_SNAKE, SIZE_SNAKE])
        
ok = True

while ok:
    screen.fill(WHITE)
    Your_score(score)
    draw_snake(SIZE_SNAKE, snake_list)
    pygame.draw.rect(screen, BLACK, [foodx, foody, SIZE_SNAKE, SIZE_SNAKE])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vt_x_change = 0
                vt_y_change = -8
            if event.key == pygame.K_DOWN:
                vt_y_change = 8
                vt_x_change = 0
            if event.key == pygame.K_LEFT:
                vt_x_change = -8
                vt_y_change = 0
            if event.key == pygame.K_RIGHT:
                vt_x_change = 8
                vt_y_change = 0
    vt_x += vt_x_change
    vt_y += vt_y_change    
    snake_head = []
    snake_head.append(vt_x)
    snake_head.append(vt_y)
    snake_list.append(snake_head)
    while len(snake_list)-1 > score:
        del snake_list[0]
    for x in snake_list[:-1]:
        if x == snake_head:
            ok = False                            
    if (vt_x >= foodx and vt_x <= foodx + SIZE_SNAKE and vt_y + SIZE_SNAKE >= foody and vt_y + SIZE_SNAKE<= foody + SIZE_SNAKE) or (vt_x + SIZE_SNAKE >= foodx and vt_x + SIZE_SNAKE <= foodx + SIZE_SNAKE and vt_y >= foody and vt_y <= foody + SIZE_SNAKE) or (vt_x + SIZE_SNAKE >= foodx and vt_x + SIZE_SNAKE <= foodx + SIZE_SNAKE and vt_y + SIZE_SNAKE >= foody and vt_y + SIZE_SNAKE <= foody + SIZE_SNAKE):
            score += 1
            foodx = round(random.randrange(10, 750))
            foody = round(random.randrange(10, 750))
    if vt_x >= 800 or vt_x <= 0 or vt_y>= 800 or vt_y <= 0:
        ok = False 
    pygame.display.update()
    clock.tick(30)        