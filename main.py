import numpy
import pygame
import time


class IconLocation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load("slot/Image/" + icon + ".png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self, image):
        self.image = image


def rd():
    global rand_numbs
    rand_numbs = numpy.random.choice(numbs, 3)


def start():
    rd()
    loc_left.set_image(icon_dict[rand_numbs[0]])
    loc_middle.set_image(icon_dict[rand_numbs[1]])
    loc_right.set_image(icon_dict[rand_numbs[2]])
    print(rand_numbs)
    if rand_numbs[0] == rand_numbs[1] == rand_numbs[2]:
        jackpot_sound.play()


def start_fake():
    rd()
    loc_left.set_image(icon_dict[rand_numbs[0]])
    loc_middle.set_image(icon_dict[rand_numbs[0]])
    loc_right.set_image(icon_dict[rand_numbs[0]])
    print(rand_numbs)
    if rand_numbs[0] == rand_numbs[0] == rand_numbs[0]:
        jackpot_sound.play()


def wait():
    a = time.time()
    while True:
        if time.time() - a > 1:
            break


pygame.init()
width = 1280
height = 720
FullScreen = False
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("슬롯머신")
logo = pygame.image.load('slot-back.png')
pygame.display.set_icon(logo)
white = [250, 250, 250]
black = (0, 0, 0)
screen.fill(black)

background = pygame.image.load('slot-back.png')
police_total_coins = pygame.font.Font('slot/Fonts/Ft.ttf', 15)
police_menu = pygame.font.Font('slot/Fonts/Ft.ttf', 15)

background_sound = pygame.mixer.Sound('slot/Sound/music.wav')
background_sound.play(-1)
background_sound.set_volume(1)
effect_sound = pygame.mixer.Sound('slot/Sound/sound.wav')
effect_sound.set_volume(0.001)
effect_sound_2 = pygame.mixer.Sound('slot/Sound/sound_2.wav')
jackpot_sound = pygame.mixer.Sound('slot/Sound/jackpot.wav')
jackpot_sound.set_volume(1)

height_location = 209
loc_left = IconLocation(230, height_location, "Q")
loc_middle = IconLocation(531, height_location, "Q")
loc_right = IconLocation(837, height_location, "Q")

Location = pygame.sprite.Group()
Location.add(loc_left)
Location.add(loc_middle)
Location.add(loc_right)

fake = False

imageView = True

numbs = ['A', 'B', 'C', 'D', 'E', 'F', 'X', '7']

icon_dict = {
    'A': pygame.image.load("slot/Image/A.PNG"),
    'B': pygame.image.load("slot/Image/B.PNG"),
    'C': pygame.image.load("slot/Image/C.PNG"),
    'D': pygame.image.load("slot/Image/D.PNG"),
    'E': pygame.image.load("slot/Image/E.PNG"),
    'F': pygame.image.load("slot/Image/F.PNG"),
    'X': pygame.image.load("slot/Image/X.PNG"),
    '7': pygame.image.load("slot/Image/7.png"),
    'Q': pygame.image.load("slot/Image/Q.png")
}

# Main loop
run = True
while run:
    screen.fill(black)
    screen.blit(background, (0, 0))
    Location.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
            quit()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_0]:
                if fake == True:
                    effect_sound_2.play()
                    wait()
                    effect_sound_2.stop()
                    start_fake()
                else:
                    effect_sound_2.play()
                    wait()
                    effect_sound_2.stop()
                    start()
            if keys[pygame.K_z]:
                if fake == True:
                    fake = False
                    print("false")
                else:
                    if fake == False:
                        fake = True
                        print("True")

        if keys[pygame.K_TAB]:
            if FullScreen != True:
                screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                FullScreen = True
            else:
                screen = pygame.display.set_mode((width, height))
                FullScreen = False

# eet.mjlee@gmail.com 이민정선생님 이메일
