 #Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer

font.init()
font1 = font.SysFont('Arial',80)
win = font1.render('Молодец!', True, (0,255,0))
lose = font1.render('Ты ЧЕБУРАШКА!', True, (180, 0, 0))


font2 = font.SysFont('Arial',36)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
score = 0

rel_time = False
num_fire = 30

win_width = 700
win_height = 500
w = display.set_mode((win_width,win_height))
display.set_caption('Чебурашка лысый!')

background = transform.scale(image.load('galaxy.jpg'),(win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update (self):
        self.rect.y -= self.speed
        global lost  

class Enemy(GameSprite):
    def update(self):        
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            global lost
            lost = lost + 1
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            

lost = 0
live = 3
max_lost = 10
max_scor = 100
font.init()
font1 = font.Font(None, 36)

        
class Player(GameSprite):
    def fire(self):
        pass
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > -10:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 640:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10,20,10)
        Bullets.add(bullet)

run = True
player = Player('rocket.png', 5, win_height - 100, 80, 100, 10)
clock = time.Clock()

Bullets = sprite.Group()


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(1, 6):
    asteroid = Asteroid('asteroid.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)

finish = False
while run:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire > 0 and rel_time == False:
                    num_fire = num_fire - 1                    
                    player.fire()
                    fire_sound.play()
                if num_fire == 0 and rel_time == False : 
                    last_time = timer()
                    rel_time = True
    if not finish:
        w.blit(background, (0,0))

        text = font1.render('Счет: ' + str(score), 1, (255,255,255))
        w.blit(text, (10, 20))
        text_lose = font1.render('Пропущено: ' + str(lost),True,(255,255,255))
        w.blit(text_lose, (10,50))
        live1 = font1.render('Сколько лет ты будеш жить: ' + str(live),True,(255,255,255))
        w.blit(live1, (10,80))
        player.update() 
        monsters.update()
        monsters.draw(w)
        collider = sprite.groupcollide(monsters, Bullets, True, True)
        for i in collider:
            score = score + 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        if sprite.spritecollide(player, asteroids, True) or sprite.spritecollide(player, monsters, False): 
            live -= 1 
        if live==0 or lost >= max_lost:
            finish = True
            w.blit(lose, (200, 200))
        if score >= max_scor:
            finish = True
            w.blit(win, (200, 200))
        Bullets.update()
        Bullets.draw(w)
        asteroids.update()
        asteroids.draw(w)
        player.reset()
        display.update()
        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font1.render('ПЕРЕЗАРЯДКА.....', 1, (255,0,0))
                w.blit(reload, (250, 460))
            else:
                num_fire = 30
                rel_time = False
                
                 
        clock.tick(25)

    

