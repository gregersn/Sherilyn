# -*- coding: utf-8 -*-

import os
import fnmatch

from database import Database

class Library:
	""" Library functions, and access to database """
	db = None
	folders = []

	def __init__(self, file="database.db"):
		self.db = Database(file)
		self.folders = self.getFolders()

	def addFolder(self, folder):
		if folder not in self.folders:
			self.db.addFolder(folder, 0)
			self.folders.append(folder)
			self.scanFolder(folder)

	def getFolders(self):
		ret = self.db.getFolders()
		folders = []
		for folder in ret:
			folders.append(folder[0])
		return folders

	def scanFolder(self, folder):
		matches = []
		for root, dirnames, filenames, in os.walk(folder):
			for filename in fnmatch.filter(filenames, '*.mp3'):
				matches.append(os.path.join(root, filename))

		self.addFiles(matches, folder)

	def rescan(self):
		for folder in self.folders:
			self.scanFolder(folder)

	def addFiles(self, files, folder):
		self.db.addFiles(files, folder)

	def getRandomFile(self):
		return self.db.getRandomFile()
				



def main():
	lib = Library('test.db')
	lib.addFolder('/tmp/test/')
	lib.addFolder('/tmp/test2/')
	lib.addFolder('/tmp/test/')

	print "Folders in library", lib.folders

if __name__ == u'__main__':
	main()
