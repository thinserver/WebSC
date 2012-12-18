#
# Makefile
#

favicon:
	inkscape img/keycard.svg --export-png=img/keycard.png -w32 -h32
	convert img/keycard.png img/favicon.ico

key:
	inkscape img/key.svg --export-png=img/key.png -w128 -h128
	
person:
	inkscape img/person.svg --export-png=img/person.png -w45 -h45

