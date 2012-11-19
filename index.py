#!/usr/bin/python

#
# main server functions
#

import bobo

@bobo.query('/')
def index():
	return open('index.html').read()

#bobo.query('/favicon.ico')
#def favicon():
#	return bobo.redirect('/img/favicon.ico')

@bobo.query('/img/:filename')
def img(filename='wait.gif'):
	return open('img/'+filename).read()

@bobo.query('/css/:filename')
def css(filename='jquery.css'):
	return open('css/'+filename).read()
