#!/usr/bin/python

#
# key manager
# designed after the Enigmail OpenPGP Key Manager
# http://www.enigmail.net/documentation/keyring.php
#

import bobo

pubkey_algo = {
			1: 'RSA',
			17: 'DSA'
			}

@bobo.query('/keyring.py')
def keyring():
	try:
		import gpgme
	except:
		return 'Exception: Python-GPGME library'

	# load templates
	key_template = open('keyring/key.html').read()
	uid_template = open('keyring/uid.html').read()
	subkey_template = open('keyring/subkey.html').read()
	signature_template = open('keyring/signature.html').read()

	# connect to GPG
	gpg = gpgme.Context()
	keylist = gpg.keylist()
	keys = ''
	
	# list keys
	for key in keylist:
		subkey = key.subkeys[0]
		title = ''
		certificate = ''
		signatures = ''
		
		# get title
		if len(key.uids) > 0:
			uid = key.uids[0]
			title +=	uid.name
			if uid.email.strip() != '':
				title += ' &lt;'+uid.email+'&gt;'
		
		# draw certificate
		for uid in key.uids:
			certificate += uid_template % (uid.name, uid.email)
#		for subkey in key.subkeys:
		subkey = key.subkeys[0]
		certificate += subkey_template % (pubkey_algo[subkey.pubkey_algo] + ', ' + str(subkey.length)+' bit', subkey.keyid, subkey.fpr)

		# get all signatures for this certificate
		# for signature in key.signatures:
		signatures += signature_template % ('Matthias Bock', 'mail@matthiasbock.net', '12345678')

		# render
		keys += key_template % (title, "C72A19AB", certificate, signatures)

#	from subprocess import Popen, PIPE
#	from shlex import split
#	keys = Popen(['whoami'], stdout=PIPE).communicate()[0]
#	"root"

	return open('keyring/keyring.html').read() % (keys)

