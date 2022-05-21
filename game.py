import pygame
from sys import exit
from random import randint


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('Graphics/crosshair_red_small.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.gunshot_sound = pygame.mixer.Sound('Sound/gunshot.mp3')
        self.player_score = 0

    def crosshair_movement(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        if pygame.sprite.spritecollide(crosshair, target_group, True):
            self.player_score += 1
        self.gunshot_sound.play()

    def update(self):
        self.crosshair_movement()


class Target(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('Graphics/target_red3.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)


def display_score(score):
    display_surface = pygame.display.get_surface()
    score_text = font.render(f'Score: {score}', False, 'White')
    score_rect = score_text.get_rect(center=(screen_width / 2, 10))
    pygame.draw.rect(display_surface, 'Black', score_rect)
    display_surface.blit(score_text, score_rect)


pygame.init()
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, 40)

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

crosshair = Crosshair(screen_width / 2, screen_height / 2)
crosshair_group = pygame.sprite.GroupSingle()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
target_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(target_spawn_timer, 600)

background = pygame.image.load('Graphics/bg_green.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
background_music = pygame.mixer.Sound('Sound/background_music.mp3')
background_music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

        if event.type == target_spawn_timer:
            target_group.empty()
            target = Target(randint(0, screen_width), randint(0, screen_height))
            target_group.add(target)

    screen.blit(background, (0, 0))
    display_score(crosshair.player_score)

    target_group.draw(screen)

    crosshair_group.update()
    crosshair_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
