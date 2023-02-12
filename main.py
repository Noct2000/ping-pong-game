import pygame
from play_scene import PlayScene
from start_menu_scene import StartMenu

# Initialize Pygame
pygame.init()

display = pygame.display

start_menu = StartMenu(display)
play_scene = PlayScene(display)

start_menu.show()
print(start_menu.maxScore)
play_scene.show(start_menu.maxScore, start_menu.isExited)


# Quit Pygame
pygame.quit()
