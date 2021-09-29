import pygame,sys,time,random
pygame.init()

clk = pygame.time.Clock()
background = pygame.image.load('pics and stuff/preview.jpg')
width = background.get_width()
height = background.get_height()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("It's gonna be fun")
icon = pygame.image.load('pics and stuff/watching-a-movie.png')
pygame.display.set_icon(icon)
run = True
pygame.mixer.music.load('pics and stuff/01 - Round Start.mp3')
pygame.mixer.music.play(0, 0,0)
w = 0
current_time = 0
enemy_removed_time = 0
game_over = False
bg_x=[]
bg_x.append(0)
for i in range(1,100):
  bg_x.append(width * i + bg_x[0])

right_pics =[
    pygame.image.load('pics and stuff/R1.png'),
    pygame.image.load('pics and stuff/R2.png'),
    pygame.image.load('pics and stuff/R3.png'),
    pygame.image.load('pics and stuff/R4.png'),
    pygame.image.load('pics and stuff/R5.png'),
    pygame.image.load('pics and stuff/R6.png'),
    pygame.image.load('pics and stuff/R7.png'),
    pygame.image.load('pics and stuff/R8.png'),
    pygame.image.load('pics and stuff/R9.png')
]
left_pics = [
    pygame.image.load('pics and stuff/L1.png'),
    pygame.image.load('pics and stuff/L2.png'),
    pygame.image.load('pics and stuff/L3.png'),
    pygame.image.load('pics and stuff/L4.png'),
    pygame.image.load('pics and stuff/L5.png'),
    pygame.image.load('pics and stuff/L6.png'),
    pygame.image.load('pics and stuff/L7.png'),
    pygame.image.load('pics and stuff/L8.png'),
    pygame.image.load('pics and stuff/L9.png')
]

class character(object):

    def __init__(self):

         self.right_pic = right_pics
         self.left_pic = left_pics
         self.speedX = 0
         self.speedY = 0
         self.x = 60
         self.y = 280
         self.space = pygame.Rect(10 , 240 , 100, 100)
         self.right = False
         self.left = False
         self.jump = False
         self.gravity = False

player = character()

class enemy_class(object):

    def __init__(self,x,y):
        self.image = pygame.image.load('pics and stuff/enemy.png')
        self.enemy = pygame.transform.scale(self.image,(50,50))
        self.x = x
        self.y = y
        self.rect = self.enemy.get_rect()
        self.rect.left = x + 10
        self.rect.y = y


enemy_x = random.randint(200,500)
enemy = []
enemy.append(1)
range1=[0,1,2,3,4,5,6,7,8,9,10]

class bullets(object):
   def __init__(self):
       self.x = player.x + 50
       self.y = player.y + 20
       self.bullet = None
       self.run = False


   def move_the_bullet(self):
       if self.run == True:
           self.bullet = pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 5)




bullet =[]
bullet.append(0)
bullet_hit_the_enemy = 0


def check_bullets_bounderies():
    global bullet

    for i in range( 1 ,len(bullet)-1):
         bullet[i].move_the_bullet()
         bullet[i].x += 20
         if bullet[i].x > width:
             bullet.pop(i)
             bullet.append(bullets())

def hit_the_enemy():
    global enemy,enemy_x,bullet_hit_the_enemy,enemy_removed_time

    for i in range(1,len(bullet)-1):
      if bullet[i].bullet != None and len(enemy) == 1:
        if enemy[0] != 0:
         if bullet[i].bullet.colliderect(enemy[0]):
           bullet.pop(i)
           print('enemy hit')
           bullet_hit_the_enemy +=1
           print(bullet_hit_the_enemy)
           if bullet_hit_the_enemy == 2:
              print('enemy removed')
              enemy.pop(0)
              bullet_hit_the_enemy = 0
              enemy_removed_time = pygame.time.get_ticks()
              enemy.append(0)





def check_enemy_boundery():
    global enemy_x
    if enemy[0] != 0 :
      enemy[0] = enemy_class(enemy_x, 280)
      enemy_x -= 3
    if enemy_x <= -10 and player.x > 0:
        enemy.pop(0)
        enemy_x = random.randint(width / 2, 500)
        enemy.append(enemy_class(enemy_x, 280))
    if enemy[0] == 0:
        if current_time - enemy_removed_time > 4000 and player.x < 500:
            enemy_x = random.randint(400, 600)
            enemy[0] = enemy_class(enemy_x, 280)

def move():

     global bg_x,enemy_x,bullet_hit_the_enemy

     if player.jump and  player.y > 180:
        player.y += player.speedY

     if player.gravity and player.y <280:
         player.y += player.speedY

     if player.right or player.left:
         player.x += player.speedX

     if player.space.x + 100 > width:
         for i in range1:
           bg_x[i] = bg_x[i] - 9*width/10
         if len(enemy) ==1:
            enemy_x -= 9*width/10
            bullet_hit_the_enemy=0
         if len(enemy) != 1:
             enemy.append(0)
         player.x = player.x - 9*width/10

     if player.x < 10 :
           player.x =20


pic = player.right_pic

def def_pic():

  global pic

  if player.right and player.left == False:
    pic = player.right_pic
  if player.left and player.right == False:
    pic = player.left_pic

mouse_position = None
mouse_click = False

def mouse():
    global mouse_position,mouse_click
    mouse_position = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == True:
        mouse_click = True
    else:
        mouse_click = False

def Game_Over():
    global game_over,run,bg_x,enemy,enemy_x,bullet
    pygame.mixer.music.stop()

    font = pygame.font.Font('pics and stuff/Blazed.ttf', 30)
    font2 = pygame.font.Font('pics and stuff/8514oem.fon', 15)
    text1 = font.render('GAME OVER', False, (255, 0, 0))
    text2 = font2.render('Do You wanna play again?', False, (120, 30, 40))
    text3 = font2.render('YES', False, (120, 30, 40))
    text4 = font2.render('NO', False, (120, 30, 40))
    window.fill((0, 0, 0))
    window.blit(text1, (130, 120))
    window.blit(text2, (190, 180))
    YES = window.blit(text3, (190, 210))
    NO = window.blit(text4, (260, 210))
    mouse()
    rect = pygame.Rect(mouse_position[0], mouse_position[1], 30, 30)
    if mouse_click:
        if rect.colliderect(YES):
            bg_x[0] = 0
            for i in range1:
                bg_x[i] = width * i + bg_x[0]
            player.x = 60
            player.y = 280
            player.right = False
            player.left = False
            player.jump = False
            enemy.pop(0)
            enemy_x = random.randint(200, 500)
            enemy.append(1)
            for i in range(1,len(bullet)-1):
                bullet.pop(i)

            pygame.mixer.music.play(0, 0, 0)
            game_over = False

        if rect.colliderect(NO):
            pygame.quit()



while run :


       for i in range(100):
          bg_x[i] -=3
          window.blit(background,(bg_x[i],0))
       player.space = pygame.Rect(player.x -50,player.y - 50,100,100)


       for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:

               if event.key == pygame.K_UP:
                 player.jump = True
                 player.gravity = False
                 player.speedY = -40
               if event.key == pygame.K_RIGHT:
                 player.right = True
                 player.speedX = 30
               if event.key == pygame.K_LEFT:
                 player.left = True
                 player.speedX = -30
               if event.key == pygame.K_SPACE:
                   bullet.append(bullets())
                   bullet[len(bullet)-1].run = True

           if event.type == pygame.KEYUP:

               if event.key == pygame.K_UP:
                 player.jump = False
                 player.gravity = True
                 player.speedY = 15

               if event.key == pygame.K_RIGHT:
                  player.right = False
               if event.key == pygame.K_LEFT:
                  player.left = False



           if event.type == pygame.QUIT:
               run = False

       if w <8:
          w += 1
       else:
          w = 0



       move()
       def_pic()
       player1 = window.blit(pic[w], (player.x, player.y))
       check_bullets_bounderies()
       check_enemy_boundery()
       hit_the_enemy()
       current_time = pygame.time.get_ticks()
       if enemy[0] != 0:
          window.blit(enemy[0].enemy,(enemy[0].x,enemy[0].y))
          if player1.colliderect(enemy[0].rect):
              print('hit')
              game_over  = True


       if game_over:
         Game_Over()

       clk.tick(9)
       pygame.display.update()