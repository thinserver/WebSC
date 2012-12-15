#!/usr/bin/python

# PHP SCRIPT: var_dump($_POST, $_FILES);

import bobo

@bobo.post('/encrypt.py')
def encrypt(file='no file received on the server'):
	# gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc
	return file #open('img/key.png').read()
