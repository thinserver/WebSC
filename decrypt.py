#!/usr/bin/python

import bobo

@bobo.query('/decrypt.py')
def decrypt(content_type='image/png'):
	return open('img/key.png').read()
