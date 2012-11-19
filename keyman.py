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
	key_template = open('keyman/key.html').read()
	uid_template = open('keyman/uid.html').read()
	subkey_template = open('keyman/subkey.html').read()
	gpg = gpgme.Context()
	keylist = gpg.keylist()
	keys = ''
	br = '<br/>\n'
	for key in keylist:
		subkey = key.subkeys[0]
		title = ''
		content = ''
		if len(key.uids) > 0:
			uid = key.uids[0]
			title +=	uid.name
			if uid.email.strip() != '':
				title += ' &lt;'+uid.email+'&gt;'
#		for uid in key.uids:
#		for subkey in key.subkeys:
		subkey = key.subkeys[0]
		content +=	subkey_template % (pubkey_algo[subkey.pubkey_algo] + ', ' + \
									str(subkey.length)+' bit' + br + \
									subkey.keyid + br + \
									subkey.fpr + br + \
									str(subkey.expired))
		keys += key_template % (title, content)
	return open('keyman/keyring.html').read() % (keys)

@bobo.query('/keyman')
def keyman():
	return keyring()
