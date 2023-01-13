import pygame


class MySprite(pygame.sprite.Sprite):

    def __init__(self,image, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
