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
	gpg = gpgme.Context()
	keys = ''
	key_template = open('keyman/key.html').read()
	keylist = gpg.keylist()
	br = '<br/>\n'
	for key in keylist:
		subkey = key.subkeys[0]
		keys += key_template % (key, 	pubkey_algo[subkey.pubkey_algo] + br +
									str(subkey.length)+' bit' + br +
									subkey.keyid + br +
									subkey.fpr + br +
									str(subkey.expired)
							)
	return open('keyman/keyring.html').read() % (keys)

@bobo.query('/keyman')
def keyman():
	return keyring()
