#!/usr/bin/python

#
# browser certificate manager
#

import bobo
import os

@bobo.query('/cacerts.py')
def cacerts():
	list = "<ul>\n"
	for cert in sorted(os.listdir("cacerts")):
		list += "\t<li>"+cert+"</li>\n"
	list += "</ul>\n"
	return list
