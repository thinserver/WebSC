#!/usr/bin/python

#
# login certificate manager
#

#
# To convert a certificate from DER to PEM:
# x509 -in cert.der -inform DER -out cert.pem -outform PEM
# To convert a key from DER to PEM:
# rsa -in privatekey.der -inform DER -out privatekey.pem -outform PEM
# To convert a key from NET to PEM:
# rsa -in privatekey.net -inform NET -out privatekey.pem -outform PEM
#
# openssl pkcs12 -export -in cert.pem -inkey privatekey.pem -out logincert.p12
#

from subprocess import Popen
from shlex import split

def generateLoginCert(cert, key):
	if isDERcert(cert):
		cert = DER2PEMcert(cert)

	if isDERkey(key):
		key = DER2PEMkey(key)
	elif isNETkey(key):
		key = NET2PEMkey(key)

	Popen(split('openssl pkcs12 -export -in cert.pem -inkey privatekey.pem -out logincert.p12')).wait()
