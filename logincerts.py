#!/usr/bin/python

#
# browser certificate manager
#

import bobo
# openssl ...

@bobo.query('/logincerts')
def keyring():
	return open('logincerts/certpile.html').read() % ('Zertifikate')
