import pygame
import sys
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
#if not pygame.mixer: print 'Warning, sound disabled'
#if not pygame.mixer.music: print 'Warning, music playback disabled'

class GUI:
	window = None
	screen = None
	fpsClock = None

	def __init__(self):
		#Init pygame
		pygame.init()

		# Get an fps clock to limit framerate
		self.fpsClock = pygame.time.Clock()

		# Set up window
		self.window = pygame.display.set_mode((640, 480))

		# Set window caption
		pygame.display.set_caption('Sherilyn')


		self.screen = pygame.display.get_surface()

		if pygame.font:
			font = pygame.font.Font(None, 36)
			text = font.render("Sherilyn is your media master", 1, (255, 10, 10))
			textpos = text.get_rect()
			textpos.centerx = self.screen.get_rect().centerx
			self.screen.blit(text, textpos)
			pygame.display.flip()

	def input(self, events):
		for event in events:
			if event.type == QUIT:
				pygame.quit()	
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
			else:
				#print event
				1

	def set_status(self, status):
		font = pygame.font.Font(None, 12)
		text = font.render(status, 1, (255, 255, 10))
		textpos = text.get_rect()
		textpos.centerx = self.screen.get_rect().centerx
		textpos.centery = 400
		self.screen.blit(text, textpos)
		pygame.display.flip()

	def update(self):
		self.input(pygame.event.get())
		pygame.display.update()
		self.fpsClock.tick(30)
		self.window.fill(pygame.Color(0, 0, 0))



#	def queueTrack(self, filename):
#		pygame.mixer.music.load(filename)
#		pygame.mixer.music.play()
