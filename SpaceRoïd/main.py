from game import Game
import pygame
pygame.init()

resolutions = (1080,720)
title = "SpaceRoïd"
screen = pygame.display.set_mode(resolutions)
pygame.display.set_caption(title)

game = Game(screen)
game.run()
pygame.quit()


