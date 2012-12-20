#!/usr/bin/python

#
# browser certificate manager
#

import bobo

@bobo.query('/logincerts.py')
def logincerts():
	return open('logincerts/certpile.html').read() % ('<h3>2 PKCS#12-Zertifikate:</h3><br/>Florian Paintner<br/>Beate Paintner')
