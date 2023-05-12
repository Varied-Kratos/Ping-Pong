import pygame
pygame.init()
mw=pygame.display.set_mode((700,800))
mw.fill((120,30,50))
clock=pygame.time.Clock()
GREEN=(0,255,0)
BLUE=(0,0,255)
dx,dy=6,6
bx,by=350,400
x=30
y=400
x1,y1=640,400
class Player():
    def __init__(self, x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect=pygame.Rect(x,y,width,height)
    
    def create(self):
        pygame.draw.rect(mw,self.color,(self.x,self.y,self.width,self.height))
    
class Ball():
    def __init__(self,x,y,rad):
        self.x=x
        self.y=y
        self.rad=rad
        self.rect=pygame.Rect(x,y,rad,rad)
    def create(self):
        pygame.draw.circle(mw,(255,255,255),(self.x,self.y),self.rad)
    
up=False 
down=False
up1,down1=False,False
while True:
    mw.fill((120,30,50))
    Player1=Player(x,y,30,100,GREEN)
    Player2=Player(x1,y1,30,100,BLUE)
    Ball1=Ball(bx,by,20)
    Ball1.create()
    
    keys=pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key==pygame.K_w:
                up=True
            if e.key==pygame.K_s:
                down=True
            if e.key==pygame.K_UP:
                up1=True
            if e.key==pygame.K_DOWN:
                down1=True
        elif e.type==pygame.KEYUP:
            if e.key==pygame.K_w:
                 up=False
            if e.key==pygame.K_s:
                 down=False
            if e.key==pygame.K_UP:
                up1=False
            if e.key==pygame.K_DOWN:
                down1=False
    bx+=dx
    by+=dy
    if by>750 or by<0:
        dy*=-1
    if Ball1.rect.colliderect(Player1):
        dx*=-1
        dy*=-1

    if Ball1.rect.colliderect(Player2):
        dx*=-1
        dy*=-1

    if up ==True and y>0:
        y-=20
    if down==True and y<700:
        y+=20
    if up1 ==True and y1>0:
        y1-=20
    if down1==True and y1<700:
        y1+=20
    Player1.create()
    Player2.create()
    pygame.display.update()
    clock.tick(40)