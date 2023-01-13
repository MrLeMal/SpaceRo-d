import pygame
from sprite import MySprite
from projectile import Projectile

class Player(MySprite):

    def __init__(self, image, game):
        super().__init__(image, 500, 50)
        self.game = game
        self.image = pygame.transform.scale(self.image,(100,100))
        self.speed = 5
        self.position = [0,0]
        self.projectiles = pygame.sprite.Group()
        self.health = 100
        self.score = 0

    def launch_projectile(self):
        self.projectiles.add(Projectile(self, "assets/projectile/projectile.png"))

    def damage(self):
        for comete in self.game.check_collision(self,self.game.all_cometes):
            comete.spawn()
            self.health -= 10

            if self.health <= 0:
                self.health = 0

    def move(self):
        self.rect.move_ip(self.position[0] * self.speed, self.position[1] * self.speed)

    def draw(self,screen):
        screen.blit(self.image,self.rect)