#!/usr/bin/python

import bobo

@bobo.query('/encrypt.py')
def encrypt(file, content_type='image/png'):
	
	return file #open('img/key.png').read()
