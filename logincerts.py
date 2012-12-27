#!/usr/bin/python

#
# browser certificate manager
#

import bobo

@bobo.query('/logincerts.py')
def logincerts():
	pkcs12 = "<ul>\n"
	for p12 in ["Florian Paintner", "Beate Paintner"]:
		pkcs12 += "<li>"+p12+"</li>\n"
	pkcs12 += "</ul>\n"
	ssh = open('/root/.ssh/authorized_keys').read().strip()
	return open('logincerts/logincerts.html').read() % (pkcs12, ssh)
