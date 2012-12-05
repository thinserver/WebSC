#!/usr/bin/python

import bobo

@bobo.query('/verify.py')
def verify(content_type='image/png'):
	return open('img/key.png').read()
