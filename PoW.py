
# -*- coding: utf-8 -*-
import hashlib

def goldennonce(D,iNum):
	test_str = '0'*int(D)
	block_data='COMSM0010cloud'
	value = str(iNum) + block_data
	hash1= hashlib.sha256(value.encode('utf-8')).hexdigest()
	# double hashing
	hash2= hashlib.sha256(hash1.encode('utf-8')).hexdigest()

	# print golden nonce
	if hash2.startswith(test_str):
		print('Lucky num is '+ str(iNum) + ', its hash is '+ hash2)
