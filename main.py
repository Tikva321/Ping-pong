from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

font.init()
font_score = font.Font(None, 36)
font_message = font.Font(None, 72)

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

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width, image_height):
        super().__init__(player_image, player_x, player_y, player_speed, image_width, image_height)
        self.direction_x = 1  
        self.direction_y = 1  
        
    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        
        if self.rect.y <= 0 or self.rect.y >= win_height - 60:
            self.direction_y *= -1
        
        if self.rect.colliderect(player1.rect) and self.direction_x == -1:
            self.direction_x *= -1
            self.direction_y = 1 if self.rect.centery > player1.rect.centery else -1
        
        if self.rect.colliderect(player2.rect) and self.direction_x == 1:
            self.direction_x *= -1
            self.direction_y = 1 if self.rect.centery > player2.rect.centery else -1

    def reset_ball(self):
        ball.rect.x = win_width // 2 - 25
        ball.rect.y = win_height // 2 - 25
        ball.direction_x = 1 if ball.direction_x == -1 else -1
        ball.direction_y = 1

clock = time.Clock()
FPS = 60
game = True
game_over = False
score_1 = 0
score_2 = 0
win_score = 3

player1 = Player('racket.png', 50, 200, 5, 20, 100)  
player2 = Player('racket.png', 535, 200, 5, 20, 100)  
ball = Ball('ball.png', 270, 220, 2, 60, 60)  

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not game_over:
        player1.update_1()
        player2.update_2() 
        ball.update()
        
        if ball.rect.x <= 0:
            score_2 += 1 
            ball.reset_ball()
            
        if ball.rect.x >= win_width - 50:
            score_1 += 1 
            ball.reset_ball()
        
        if score_1 >= win_score:
            game_over = True
            winner = "Левый игрок победил!"
        elif score_2 >= win_score:
            game_over = True
            winner = "Правый игрок победил!"

    window.fill(back)
    player1.reset()
    player2.reset()
    ball.reset()

    score_1_text = font_score.render(str(score_1), True, (0, 0, 0))
    score_2_text = font_score.render(str(score_2), True, (0, 0, 0))
    window.blit(score_1_text, (win_width // 2 - 40, 20))
    window.blit(score_2_text, (win_width // 2 + 20, 20))

    if game_over:
        win_text = font_message.render(winner, True, (255, 0, 0))
        window.blit(win_text, (win_width // 2 - win_text.get_width() // 2, win_height // 2 - 50))

    display.update()
    clock.tick(FPS)

    display.update()
    clock.tick(FPS)
