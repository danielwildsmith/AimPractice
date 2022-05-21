import pygame
from sys import exit


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load('Graphics/crosshair_red_small.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

    def player_input(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.player_input()


pygame.init()
pygame.mouse.set_visible(False)

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

crosshair = Crosshair(screen_width / 2, screen_height / 2)
crosshair_group = pygame.sprite.GroupSingle()
crosshair_group.add(crosshair)

background = pygame.image.load('Graphics/bg_green.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    crosshair_group.update()
    crosshair_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
