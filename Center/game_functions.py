import sys
import pygame
from ship import Ship

def check_events():
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

def update_screen(screen, ship):
	screen.fill((200, 123, 123))
	ship.blitme()
	pygame.display.flip()
