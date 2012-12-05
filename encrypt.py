#!/usr/bin/python

import bobo

@bobo.query('/encrypt.py')
def encrypt(file='no file received on the server'):
	
	return file #open('img/key.png').read()
