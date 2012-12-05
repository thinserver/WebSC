#!/usr/bin/python

import bobo

@bobo.post('/encrypt.py')
def encrypt(file='no file received on the server'):
	# gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc
	return file #open('img/key.png').read()
