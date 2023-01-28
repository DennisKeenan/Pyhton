import pygame

pygame.init()
screenwidth=1369
screenheight=720
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.update()
pygame.display.set_caption("Snake Game")
gameover=False

Blue=(0,0,255)
Red=(255,0,0)
x=screenwidth/2
y=screenheight/2
x_speed=0
y_speed=0
time=pygame.time.Clock()
snake_speed=30
font=pygame.font.SysFont("Comic Sans",50)

def showtext(msg,msg_color):
    message=font.render(msg,True,msg_color)
    screen.blit(message,[x,y])

while not gameover:
    for event in pygame.event.get():
        print(event)
        showtext("Hello",Red)
        if event.type==pygame.QUIT:
            gameover=True
            
    pygame.draw.rect(screen,Blue,[x,y,30,30])
    pygame.display.update()

pygame.quit()
quit()