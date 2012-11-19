#!/usr/bin/python

#
# main server functions
#

import bobo

@bobo.query('/')
def index():
	return open('index.html').read()

@bobo.query('/favicon.ico')
def favicon():
	return bobo.redirect('/img/favicon.ico')

@bobo.query('/img/:filename', content_type='image')
def img(filename='wait.gif'):
	return open('img/'+filename).read()

@bobo.query('/js/:filename', content_type='text/javascript')
def js(filename='jquery.js'):
	return open('js/'+filename).read()

@bobo.query('/css/:filename', content_type='text/css')
def css(filename='jquery.css'):
	return open('css/'+filename).read()
