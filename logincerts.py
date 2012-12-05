#!/usr/bin/python

#
# browser certificate manager
#

import bobo

@bobo.query('/logincerts.py')
def logincerts():
	return open('logincerts/certpile.html').read() % ('Zertifikate')
