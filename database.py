import os
import sqlite3

class Database:
	""" Handles all the communication between the Library class
	and the database """

	conn = None

	def __init__(self, file="database.db"):
		if not os.path.exists(file):
			print "Database does not exist"
			self.createDatabase(file)
		else:
			self.conn = sqlite3.connect(file)

	def close(self):
		if self.conn is not None:
			self.conn.close()

	def commit(self):
		self.conn.commit()

	def createDatabase(self, file):
		self.conn = sqlite3.connect(file)
		c = self.conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS folders (path text UNIQUE, scanned integer)''')
		c.execute('''CREATE TABLE IF NOT EXISTS files (filename text UNIQUE)''')
		self.conn.commit()

	# Functions for library handling

	# Folder functions
	def getFolders(self):
		c = self.conn.cursor()
		c.execute('SELECT * FROM folders ORDER BY path')
		return c.fetchall()

	def addFolder(self, path, scanned):
		c = self.conn.cursor()
		c.execute('INSERT INTO folders VALUES (?, ?)', (path, scanned))
		self.conn.commit()
		return c.lastrowid

	# File functions
	def addFiles(self, files, folder):
		c = self.conn.cursor()
		for file in files: 
			c.execute('INSERT INTO files VALUES (?)', (file,))
		self.conn.commit()

	def getRandomFile(self):
		c = self.conn.cursor()
		c.execute('SELECT filename FROM files ORDER BY RANDOM() LIMIT 1')
		return c.fetchone()[0]


def main():
	db = Database()
	db.close()

if __name__ == u'__main__':
	main()
