from pygame import *
import os

windowWidth = 1000
windowHeight = 700
player_speed_x = 1.0
player_speed_y = 1.0
speed_max = 3
a = 0.03
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, img_x, img_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (img_x, img_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < windowWidth-100 and self.speed_x <= speed_max:
            self.speed_x += a
        elif not(keys_pressed[K_RIGHT]) and self.speed_x > 0 and self.rect.x < windowWidth-100 :
            self.speed_x -= a

        if keys_pressed[K_LEFT] and self.rect.x > 0 and self.speed_x >= -speed_max:
            self.speed_x -= a
        elif not(keys_pressed[K_LEFT]) and self.speed_x < 0 and self.rect.x > 0:
            self.speed_x += a


        if keys_pressed[K_DOWN] and self.rect.y < windowWidth-100 and self.speed_y <= speed_max:
            self.speed_y += a
        elif not(keys_pressed[K_DOWN]) and self.speed_y > 0 and self.rect.y < windowWidth-100 :
            self.speed_y -= a

        if keys_pressed[K_UP] and self.rect.y > 0 and self.speed_y >= -speed_max:
            self.speed_y -= a
        elif not(keys_pressed[K_UP]) and self.speed_y < 0 and self.rect.y > 0:
            self.speed_y += a
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


clock = time.Clock()
clock.tick(FPS)

window = display.set_mode((windowWidth, windowHeight))
display.set_caption("NYGame")

player = Player("circle.png", 0, 0, player_speed_x, player_speed_y, 90, 100)

game = True
finish = False

while game:

    window.fill((255, 255, 255))

    for e in event.get():
        if e.type == QUIT:
            game = False

    player.update()
    player.reset()

    if player.rect.x >= windowWidth-100:
        windowWidth += round(player.speed_x)
        display.set_mode((windowWidth, windowHeight))
        window.fill((255, 255, 255))
        player.reset()

    if player.rect.y >= windowHeight-100:
        windowHeight += round(player.speed_y)
        display.set_mode((windowWidth, windowHeight))
        window.fill((255, 255, 255))
        player.reset()



    display.update()    