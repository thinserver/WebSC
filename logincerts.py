#!/usr/bin/python

#
# browser certificate manager
#

import bobo

@bobo.query('/logincerts.py')
def logincerts():
	pkcs12 = "<h3>2 PKCS#12-Zertifikate:</h3><br/>\n"
	for p12 in ["Florian Paintner", "Beate Paintner"]:
		pkcs12 += p12+"<br/>\n"
	ssh = '<h3>SSH-Zug&auml;nge:</h3><br/>'+open('/root/.ssh/authorized_keys').read()
	return open('logincerts/certpile.html').read() % (pkcs12+'<hr/>'+ssh)
