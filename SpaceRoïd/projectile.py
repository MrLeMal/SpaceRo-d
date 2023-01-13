import pygame
from sprite import MySprite

class Projectile(MySprite):

    def __init__(self,player, image):
        super().__init__(image)
        self.player = player
        self.rect.x = self.player.rect.x + 35
        self.rect.y = self.player.rect.y + 62
        self.position = [self.rect.x,self.rect.y]
        self.speed = 5

    def remove(self):
        print("Projectile supprimé")
        self.player.projectiles.remove(self)

    def move(self):
        self.rect.y += self.speed

        for comete in self.player.game.check_collision(self, self.player.game.all_cometes):
            self.remove()
            comete.spawn()
            self.player.score += 5

        if self.rect.y > 720:
            self.remove()

    def draw(self,screen):
        screen.blit(self.image, self.position)




