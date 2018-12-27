import pygame
import game_functions as gf
from ship import Ship


def run_game():
	pygame.init()
	screen=pygame.display.set_mode((800, 800))
	ship=Ship(screen)
	while True:
		gf.check_events()
		gf.update_screen(screen, ship)
		

run_game()