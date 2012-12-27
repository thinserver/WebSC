#!/usr/bin/python

import bobo

@bobo.query('/filemanager.py')
def filemanager():
	import os, time
	template = open('filemanager/file.html').read()
	rows = ""
	filenames = sorted(os.listdir("files/"))
	for filename in filenames:
		size = os.path.getsize("files/"+filename)
		date = time.ctime(os.path.getmtime("files/"+filename))
		encryption = "-"
		signature = "-"
		rows += template % (filename, size, date, encryption, signature) 
	count = str(len(filenames))
	return open('filemanager/filemanager.html').read() % (rows, count)

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
