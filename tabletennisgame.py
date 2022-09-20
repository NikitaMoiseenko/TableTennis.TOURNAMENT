from pygame import *

W = 1500
H = 840
FPS = 60

font.init()

window = display.set_mode((W, H))
backgroung = transform.scale(image.load('background_tt.jpg'), (W, H))


class GameMenu(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,w,h):
        super(GameMenu, self).__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,w,h,player_speed):
        super(GameSprite, self).__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GamePlayer(GameSprite):
    def update_blackRacket(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed

    def update_redRacket(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed



blackRacket = GamePlayer("red_racket.png",150,300,200,200,10)

redRacket = GamePlayer("black_racket.png",1150,300,200,200,10)

ballIMG = GameSprite("ttball-removebg-preview.png",300,500,50,50,6)

game = True
finish = False

speed_x = 10
speed_y = 10

ff = font.Font(None, 35)

#res = rect.collidepoint(x, y)

firstPlayer_amount = 0
secondPlayer_amount = 0

while game:
    for eventic in event.get():
        if eventic.type == QUIT:
            exit()
        if eventic.type == MOUSEBUTTONDOWN and eventic.button == 1:
            x, y = eventic.pos

    if finish != True:
        ballIMG.rect.x += speed_x
        ballIMG.rect.y += speed_y

        if ballIMG.rect.y > H-50 or ballIMG.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(redRacket, ballIMG) or sprite.collide_rect(blackRacket, ballIMG):
            speed_x *= -1


    #########################

    firstPlayer = ff.render('Кол - во очков у первого игрока:' + str(firstPlayer_amount), True, (250, 250, 250))
    secondPlayer = ff.render('Кол - во очков у второго игрока:' + str(secondPlayer_amount), True, (250, 250, 250))

    if ballIMG.rect.x > W:
        firstPlayer_amount += 1
    elif ballIMG.rect.x < W:
        secondPlayer_amount += 1

    ###################################

    window.blit(backgroung, (0, 0))
    window.blit(firstPlayer, (30, 30))
    window.blit(secondPlayer, (1000, 30))
    blackRacket.reset()
    blackRacket.update_blackRacket()
    redRacket.reset()
    redRacket.update_redRacket()
    ballIMG.reset()

    ###################################

    display.update()
    #clock.tick(FPS)