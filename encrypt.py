#!/usr/bin/python

import bobo

@bobo.post('/encrypt.py')
def encrypt(bobo_request, images='no file received on the server'):
	print str(bobo_request)
	# gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc
	return images #open('img/key.png').read()
