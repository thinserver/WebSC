#!/usr/bin/python

import bobo
from smartcard import *

@bobo.query('/')
def index():
	if smartcard_is_present():
		if smartcard_is_locked():
			return enter_pin()
		else:
			return smartcard_menu()
	else:
		return smartcard_not_present()

@bobo.query('/favicon.ico')
def favicon():
	return bobo.redirect('/img/favicon.ico')

@bobo.query('/img/:filename')
def img(filename='wait.gif'):
	return open('img/'+filename).read()

@bobo.query('/css/:filename')
def css(filename='jquery.css'):
	return open('css/'+filename).read()
