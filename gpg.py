#!/usr/bin/python

# gpg wrapper

hkp = "hkp"
gnupg_keyserver = "keys.gnupg.net"

class Keyserver:
	def __init__(self, protocol=hkp, host=gnupg_keyserver):
		self.protocol = protocol
		self.host = host

	def search_keys(self, keyword):
		return []

# demo
if __name__ == "__main__":
	from sys import argv
	try:
		arg = argv[1]
	except:
		arg = "Matthias Bock"

	print "Searching a key for "+arg+" ..."
	keys = Keyserver().search_keys(arg)
	if len(keys) == 0:
		print "No keys found, sorry"
	else:
		print str(keys)

