from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width, image_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_width, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width, image_height):
        super().__init__(player_image, player_x, player_y, player_speed, image_width, image_height)

    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 110: 
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 110: 
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60
game = True

player1 = Player('racket.png', 50, 200, 5, 20, 100)  
player2 = Player('racket.png', 535, 200, 5, 20, 100)  
player3 = Player('ball.png', 270, 220, 5, 60, 60)  

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    player1.update_1()
    player2.update_2() 

    window.fill(back)
    player1.reset()
    player2.reset()
    player3.reset()

    display.update()
    clock.tick(FPS)
