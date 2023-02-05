import pygame
import time
import random

# Game Display
pygame.init()
screenwidth=1369
screenheight=720
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.update()
pygame.display.set_caption("Snake Game")
gameover=False
font=pygame.font.SysFont("Comic Sans",50)
score_font=pygame.font.SysFont("Corbel",50)
score=0
snake_list=[]
snake_length=1

# Color Pallete
Blue=(0,0,255)
Red=(255,0,0)
Green=(0,255,0)
White=(255,255,255)

# Positioning and Speed
x=screenwidth/2
y=screenheight/2
x_speed=0
y_speed=0
food_x=random.randint(30,screenwidth-30)
food_y=random.randint(30,screenheight-30)
game_time=pygame.time.Clock()
snake_speed=30

#Rendering Snake
def showsnake(snake_size,snake_list):
    for i in snake_list:
        pygame.draw.rect(screen,Blue,[i[0],i[1],snake_size,snake_size])

# Rendering Text
def showtext(msg,msg_color,xpos,ypos):
    message=font.render(msg,True,msg_color)
    screen.blit(message,[xpos,ypos])

# Game Controls
while not gameover:
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            gameover=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                x_speed=0
                y_speed=-10
            elif event.key==pygame.K_a:
                x_speed=-10
                y_speed=0
            elif event.key==pygame.K_s:
                x_speed=0
                y_speed=10
            elif event.key==pygame.K_d:
                x_speed=10
                y_speed=0               
    if x>=screenwidth:
        x-=screenwidth
    if y>=screenheight:
        y-=screenheight  
    if x<=0:
        x=screenwidth-1
    if y<=0:
        y=screenheight-1
    x+=x_speed
    y+=y_speed
    screen.fill(White)

    #Snake
    snake_head=[]
    snake_head.append(x)
    snake_head.append(y)
    if snake_head in snake_list and len(snake_list)>4:
        gameover=True
    snake_list.append(snake_head)
    if len(snake_list)>snake_length:
        del snake_list[0]
    showsnake(30,snake_list)

    #Food
    pygame.draw.rect(screen,Green,[food_x,food_y,30,30])
    showtext("Score:"+str(score),Red,0,0)
    pygame.display.update()
    if x<=food_x+20 and x>=food_x-20 and y<=food_y+20 and y>=food_y-20:
        print("The food has been eaten")
        snake_length+=5
        food_x=random.randint(30,screenwidth-30)
        food_y=random.randint(30,screenheight-30)
        score+=1
    game_time.tick(snake_speed)

    #Poisoned Food

showtext("Game Over!",Red,(screenwidth/2)-90,(screenheight/2)-30)
pygame.display.update()
time.sleep(5)

pygame.quit()
quit()