#!/usr/bin/python

#
# key manager
# designed after the Enigmail OpenPGP Key Manager
# http://www.enigmail.net/documentation/keyman.php
#

import bobo

class Keyring:
	def __init__(self, home="/home/user"):
		self.home = home

	def list(self):
		return ['a', 'b', 'c']

	# download foreign signatures to keys, which I have in my keyring
	# download other people's key revocations
	# download other people's signature revocations
	# upload my signatures to foreign keys
	# upload my key revocations
	# upload my signature revocations
	def sync(self, keyserver):
		return []

# demo for myKeys class
if __name__ == "__main__":
	print str(myKeys().list())

@bobo.query('/keyring')
def keyring():
	k = myKeys()
	keys = ''
	key_template = open('keyman/key.html').read()
	for key in k.list():
		keys += key_template % (key, 'test')
	return open('keyman/keyring.html').read() % (keys)

@bobo.query('/keyman')
def keyman():
	return keyring()
