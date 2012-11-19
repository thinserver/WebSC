#
# Makefile
#

favicon:
	inkscape img/keycard.svg --export-png=img/keycard.png -w32 -h32
	convert img/keycard.png img/favicon.ico

