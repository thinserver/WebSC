#!/usr/bin/python
# PHP SCRIPT: var_dump($_POST, $_FILES);
import bobo
@bobo.post('/encrypt.py')
def encrypt(file='file received'):
    # gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc
    return file #open('img/key.png').read()