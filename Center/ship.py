import pygame

class Ship():
	def __init__(self, screen):
		self.screen=screen
		self.ima=pygame.image.load('ship.bmp')
		self.coor=self.ima.get_rect()
		self.screen_coor=self.screen.get_rect()
		self.coor.centerx=self.screen_coor.centerx
		self.coor.centery=self.screen_coor.centery
	def blitme(self):
		self.screen.blit(self.ima, self.coor)