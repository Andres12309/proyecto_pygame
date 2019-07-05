fondo='1.jpg'
personaje='2.jpg'
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode(640,480)
pygame.display.set_caption("Bienvenidos")
background=pygame.image.load(fondo).convert()
mouse_cursor=pygame.image.load(personaje).convert_alpha()


running=True

while running:
	for event in pygame.event.get():
		if event.type==pyageme.QUIT:
			pygame.QUIT()
			exit()
		screen.blit(background,(0,0))
		x,y=pygame.mouse.get_pos()
		x-=mouse_cursor.get_width()/2
		y-=mouse_cursor.get_height()/2
		screen.blit(mouse_cursor,(x,y))
		pygame.display.update()


	screen.fill(color[0])
	display.flip()

