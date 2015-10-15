#!/usr/bin/env python
import pygame

def play_sound():
	pygame.init()
	song = pygame.mixer.Sound('motion-sound.ogg')
	clock = pygame.time.Clock()
	while True:
		song.play()
	pygame.quit()
		
play_sound()
