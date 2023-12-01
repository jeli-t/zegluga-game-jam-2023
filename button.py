import pygame, os
from config import *

#button class
class Button():
	def __init__(self, x, y, text, size):
		self.text = text
		self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), size)
		self.font_img = self.font.render(text, True, (198, 189, 0))
		self.font_img_hovered = self.font.render(text, True, (78, 69, 0))
		self.font_img_glow = self.font.render(text, True, (11, 11, 11))
		self.rect = self.font_img.get_rect()
		self.rect.center = (x, y)
		self.clicked = False
		self.hovered = False

	def draw(self, screen):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			self.hovered = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		else:
			self.hovered = False

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		screen.blit(self.font_img_glow, (self.rect.x - 5, self.rect.y + 10))
		if not self.hovered:
			screen.blit(self.font_img, (self.rect.x, self.rect.y))
		else:
			screen.blit(self.font_img_hovered, (self.rect.x, self.rect.y))

		return action