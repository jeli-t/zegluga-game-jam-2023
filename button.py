import pygame, os
from config import *

#button class
class Button():
	def __init__(self, x, y, image, text, scale):
		width = image.get_width()
		height = image.get_height()
		self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 40)
		self.font_img = self.font.render(text, True, (255, 255, 255))
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, screen):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		screen.blit(self.image, (self.rect.x, self.rect.y))
		screen.blit(self.font_img, ((self.rect.x + self.rect.width / 2) - (self.font_img.get_width() / 2), (self.rect.y + self.rect.height / 2) - (self.font_img.get_height() / 2)))

		return action