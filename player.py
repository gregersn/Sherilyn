# -*- coding: utf-8 -*-

import pygst
pygst.require("0.10")
import gst

import sys
import time
import gobject

class Player:
	queue = None
	def __init__(self):
		gobject.threads_init()
		self.filename = None
		self.time_format = gst.Format(gst.FORMAT_TIME)
		self.duration = None
		self.is_playing = False

		#this only works with playbin2
		self.player = gst.element_factory_make("playbin2", "player")

		# create fake video sink
		self.fake_video_sink = gst.element_factory_make("fakesink", "Fake sink for video")
		
		# Add fake video sink to player
		#self.player.set_property("videosink", self.fake_video_sink)

		# Method for processing playing queued song
		self.player.connect("about-to-finish", self.on_about_to_finish)

		# Set up message handling
		self.bus = self.player.get_bus()
		self.bus.add_signal_watch()
		self.bus.connect("message", self.on_message)

		# Set file to play
		#self.player.set_property("uri", filename)

	def play(self):
		if self.player.get_property("uri") is None:
			if self.queue is None:
				return
			else:
				self.play_queue()

		self.player.set_state(gst.STATE_PLAYING)


	def stop(self):
		self.player.set_state(gst.STATE_READY)

	def pause(self):
		self.player.set_state(gst.STATE_PAUSED)

	def null(self):
		self.player.set_state(gst.STATE_NULL)

	def cue(self, filename):
		# TODO: Make sure file exists before queueing
		self.queue = filename

	def play_queue(self):
		# If there's a track queued up, play it, and reset queue.
		if self.queue is not None:
			self.player.set_property("uri", self.queue)
			self.queue = None


	def on_about_to_finish(self, player):
		#The current song is about to finish, if we want to play another
		#song after this, we have to do that now
		self.play_queue()

	def on_message(self, bus, message):
		if message.type == gst.MESSAGE_EOS:
			print "End of stream"
			self.null()

		elif message.type == gst.MESSAGE_ERROR:
			self.null()
			(err, debug) = message.parse_error()
			print "Error: %s" % err, debug

	def get_position(self):
		try:
			pos = self.player.query_position(gst.FORMAT_TIME, None)[0]
			return pos/1000000000
		except:
			return 0

	def get_duration(self):
		try:
			dur = self.player.query_duration(gst.FORMAT_TIME, None)[0]
			return dur/1000000000
		except:
			return 0





def main():
	#player = Player("file:///D:/music/Traktor/Project Pitchfork/02 - Timekiller.mp3")
	player = Player()
	player.cue("file:///D:/music/Traktor/Project Pitchfork/02 - Timekiller.mp3")
	player.play()
	i = 0
	while True:
		#print "Do we get here?"
		print player.get_position()
		time.sleep(1)
		i = i + 1
	

if __name__ == u'__main__':
	main()
