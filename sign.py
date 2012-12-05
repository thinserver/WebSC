#!/usr/bin/python

import bobo

@bobo.query('/sign.py')
def sign(content_type='image/png'):
	return open('img/key.png').read()
