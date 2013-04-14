# -*- coding: utf-8 -*-

import pygst
pygst.require("0.10")
import gst

import sys, os
import time

from gui import GUI
from library import Library
from player import Player
import settings



def main():
	track_playing = None
	track_next = None

	# Load config file
	config = settings.loadConfig('config.json')

	# Spawn GUI
	gui = GUI()

	# Initialize library
	lib = Library(config['library']['dbfile'])

	for folder in config['library']['folders']:
		lib.addFolder(folder)


	player = Player()

	track_playing = lib.getRandomFile()
	track_next = lib.getRandomFile()

	player.cue(u"file:///"+track_playing)
	player.play()
	print track_playing
	

	player.cue(u"file:///"+track_next)
	print track_next


	#gui.queueTrack(track_playing)
	while True:
		gui.set_status(track_playing + " " + str(player.get_position()) + " / " + str(player.get_duration()))
		gui.update()
		if player.queue is None:
			track_playing = track_next
			track_next = lib.getRandomFile()
			player.cue(u"file:///"+track_next)
			print player.queue
		#time.sleep(1)

if __name__ == u'__main__':
	main()
