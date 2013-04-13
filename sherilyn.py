import sys, os
from gui import GUI
from library import Library
import settings

def main():
	# Load config file
	config = settings.loadConfig('config.json')

	# Spawn GUI
	gui = GUI()

	# Initialize library
	lib = Library(config['library']['dbfile'])

	for folder in config['library']['folders']:
		lib.addFolder(folder)

	while True:
		gui.update()

if __name__ == u'__main__':
	main()
