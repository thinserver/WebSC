#!/usr/bin/python

import bobo

@bobo.post('/encrypt.py')
def encrypt(bobo_request, images='Error: No file received on the server'):
	print str(bobo_request)
	# gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc
	return images #open('img/key.png').read()

@bobo.query('/decrypt.py')
def decrypt():
	return 'Not implemented yet'

@bobo.query('/sign.py')
def sign():
	return 'Not implemented yet'

@bobo.query('/verify.py')
def verify():
	return 'Not implemented yet'
