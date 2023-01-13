import pygame
from sprite import MySprite
from random import randint

class Comete(MySprite):

    def __init__(self,image,screen, game):
        super().__init__(image)
        self.game = game
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = randint(3, 5)
        self.screen = screen
        self.spawn()

    def spawn(self):
        self.rect.x = randint(5, self.screen.get_width() - self.rect.width)
        self.rect.y = self.screen.get_height() - self.rect.width

    def move(self):
        # self.rect.move_ip(self.rect.x, self.rect.y - self.speed)
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.spawn()

    def draw(self):
        self.screen.blit(self.image, self.rect)

