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

	def createDatabase(self, file):
		self.conn = sqlite3.connect(file)
		c = self.conn.cursor()
		c.execute('''CREATE TABLE folders (path text, scanned integer)''')
		c.execute('''CREATE TABLE files (filename text)''')
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


def main():
	db = Database()
	db.close()

if __name__ == u'__main__':
	main()
