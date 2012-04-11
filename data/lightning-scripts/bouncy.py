#!/usr/bin/env python

import sys, pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Bouncy the Box")

clock = pygame.time.Clock()

box_x = 300
box_dx = 4

while True:
	clock.tick(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	screen.fill(BLACK)

	box_x += box_dx
	if box_x > 620:
		box_x = 620
		box_dx = -4
	elif box_x <= 0:
		box_x = 0
		box_dx = 4
	
	pygame.draw.rect(screen, WHITE, (box_x, 200, 20, 20))

	pygame.display.flip()
