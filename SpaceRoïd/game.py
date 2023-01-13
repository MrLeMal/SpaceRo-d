import pygame
from player import Player
from comete import Comete

class Game:
    __FPS = 60
    def __init__(self,screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.background = (255,255,255)
        self.runApp = True
        self.player = Player("assets/vaisseau/vaisseau1.png", self)
        self.all_cometes = pygame.sprite.Group()
        self.nb_cometes = 10
        self.spawn_comete()
        self.goal_points = 1000

    def end_game(self, text):
        self.display_score()
        self.display_end_party_message(text)

    def display_score(self):
        font_text = pygame.font.SysFont('Arial', 30)
        surface_text = font_text.render(f'Votre score : {self.player.score}.', False, (0, 0, 0))
        self.screen.blit(surface_text, [(self.screen.get_width() // 2 - surface_text.get_width() // 2),
                                        (self.screen.get_height() // 2 + 10)])

    def display_end_party_message(self, text: str):
        font_text = pygame.font.SysFont('Arial', 30)
        surface_text = font_text.render(text, False, (0, 0, 0))
        self.screen.blit(surface_text, [(self.screen.get_width() // 2 - surface_text.get_width() // 2),
                                        (self.screen.get_height() // 2 - surface_text.get_height() // 2)])

    def display_health_player(self):
        font_text = pygame.font.SysFont('Arial', 30)
        surface_text = font_text.render(f'Vie : {self.player.health}', False, (0, 0, 0))
        self.screen.blit(surface_text, [0,0])

    def check_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_comete(self):
        for comete in range(self.nb_cometes):
            self.all_cometes.add(Comete("assets/comete/comete.png", self.screen, self))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runApp = False
            if event.type == pygame.KEYDOWN:
                # tir
                if event.key == pygame.K_SPACE:
                    print("Le joueur tire")
                    self.player.launch_projectile()

        keys = pygame.key.get_pressed()

        # horizontal move
        if keys[pygame.K_RIGHT]:
            self.player.position[0] = 1
        elif keys[pygame.K_LEFT]:
            self.player.position[0] = -1
        else:
            self.player.position[0] = 0

        # verticaly move
        if keys[pygame.K_DOWN]:
            self.player.position[1] = 1
        elif keys[pygame.K_UP]:
            self.player.position[1] = -1
        else:
            self.player.position[1] = 0

    def update(self):
        self.player.move()
        self.player.damage()

        for projectile in self.player.projectiles:
            projectile.move()

        for comete in self.all_cometes:
            comete.move()

    def draw(self):
        self.screen.fill(self.background)
        self.display_health_player()
        self.player.draw(self.screen)
        self.player.projectiles.draw(self.screen)
        self.all_cometes.draw(self.screen)

    def run(self):
        while self.runApp:
            if self.player.health > 0 and self.player.score < self.goal_points:
                self.handle_event()
                self.update()
                self.draw()
            elif self.player.score == self.goal_points:
                self.handle_event()
                self.end_game('Victoire')
            else:
                self.handle_event()
                self.end_game('Perdu')

            pygame.display.flip()
            self.clock.tick(Game.__FPS)

