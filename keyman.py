#!/usr/bin/python

# after http://www.enigmail.net/documentation/keyman.php

class myKeys:
	def __init__(self, username="user", userkey="ABCDEF"):
		self.username = username
		self.userkey = userkey

	# returns array of local key IDs
	def list(self):
		return []

	# allow web user to upload a key
	def add(self, key):
		# parse
		return None

	# set trust level of a specific key
	def set_trust(self, id, trust):
		return None

	# sign specific key
	def sign(self, id):
		return None

	# download a specific key by it's ID
	# in ASCII format
	# return None on error
	def export(self, id):
		asc = '...'
		return asc

	def get_photo(self, id):
		return None

	def get_signatures(self, id):
		return []

	# download foreign signatures to keys, which I have in my keyring
	# download other people's key revocations
	# download other people's signature revocations
	# upload my signatures to foreign keys
	# upload my key revocations
	# upload my signature revocations
	def sync(self, keyserver):
		return []

# demo
if __name__ == "__main__":
	print str(myKeys().list())

