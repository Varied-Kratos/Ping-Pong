import pygame
pygame.init()
back = (200, 255, 255)
mw = pygame.display.set_mode((700, 500))
mw.fill(back)
clock = pygame.time.Clock()
#переменные, отвечающие за координаты платформы
racket_x = 300
racket_x1=300
racket_y = 450
racket_y1=27
#переменные, отвечающие за направления перемещения мяча
dx = 3
dy = 3
#флаги, отвечающие за движение платформы вправо/влево
move_right = False
move_left = False
move_right1 = False
move_left1 = False
#флаг окончания игры
game_over = False
#класс с предыдущего проекта
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = back
        # if color:
        #     self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
#класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('arial', fsize).render(text, True, text_color)
 
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
#создание мяча и платформы 
ball = Picture('ball.png', 160, 200, 50, 50)
player1 = Picture('player.png', racket_x, racket_y, 100, 30)
player2=Picture('player.png', racket_x1, racket_y1, 100, 30)
#создание врагов
start_x = 5
start_y = 5
count = 9
while not game_over:
    ball.fill()
    player1.fill()
    player2.fill()
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #если нажата клавиша
                move_right = True #поднимаем флаг
            if event.key == pygame.K_LEFT:
                move_left = True #поднимаем флаг
            if event.key==pygame.K_d:
                move_right1=True
            if event.key==pygame.K_a:
                move_left1=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False #опускаем флаг
            if event.key == pygame.K_LEFT:
                move_left = False #опускаем флаг
            if event.key==pygame.K_d:
                move_right1=False
            if event.key==pygame.K_a:
                move_left1=False
        elif event.type==pygame.QUIT:
            exit()
    
    if move_right == True: #флаг движения вправо
        player1.rect.x +=3
    if move_left: #флаг движения влево
        player1.rect.x -=3
    
    if move_right1 == True: #флаг движения вправо
        player2.rect.x +=3
    if move_left1: #флаг движения влево
        player2.rect.x -=3
    
    # придаём постоянное ускорение мячу по x и y
    ball.rect.x += dx
    ball.rect.y += dy #
    # #если мяч достигает границ экрана, меняем направление его движения
    if  ball.rect.y < 0:
        time_text=Label(150,150,50,50,back)
        time_text.set_text('Player 1 Win!',60,(0,0,255))
        time_text.draw(10,10)
        
    if ball.rect.x > 650 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 450:
        time_text=Label(150,150,50,50,back)
        time_text.set_text('Player 2 Win!',60,(255,0,0))
        time_text.draw(20,10)
        
    
    
    # #если мяч коснулся ракетки, меняем направление движения
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        dy *= -1
    player1.draw()
    player2.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)