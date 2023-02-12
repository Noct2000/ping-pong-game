import pygame

from over_game_scene import OverGameScene
from play_scene import PlayScene
from start_menu_scene import StartMenu

# Initialize Pygame
pygame.init()

display = pygame.display

start_menu = StartMenu(display)
play_scene = PlayScene(display)
over_game_scene = OverGameScene(display)
is_exited = False

# Global loop for restart game
while not is_exited:
    start_menu.show()
    play_scene.show(start_menu.maxScore, start_menu.isExited)
    over_game_scene.show(play_scene.winner)
    is_exited = over_game_scene.isExited


# Quit Pygame
pygame.quit()
