#!/usr/bin/python

#
# key manager
# designed after the Enigmail OpenPGP Key Manager
# http://www.enigmail.net/documentation/keyman.php
#

import bobo
import gpgme

pubkey_algo = {
			1: 'RSA',
			17: 'DSA'
			}

@bobo.query('/keyring')
def keyring():
	# load templates
	
	new_data = encrypt(AJAX_data)
	
	return new_data
	
	key_template = open('keyman/key.html').read()
	uid_template = open('keyman/uid.html').read()
	subkey_template = open('keyman/subkey.html').read()
	signature_template = open('keyman/signature.html').read()

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

	return open('keyman/keyring.html').read() % (keys)

@bobo.query('/keyman')
def keyman():
	return keyring()
