#!/usr/bin/env python
### cryptBreak.py
###  Kshitij Jain (jain98@purdue.edu)
###  January 21, 2014, modified January 11, 2016

###  Brute foce attack on the encryption/decryption algorithms used
###  Version used is: PYTHON
###  Call syntax:
###
###       cryptBreak.py  encrypted.txt
###
###  The encrypted output is deposited in the file `output.txt'

import sys
from BitVector import * 

#Error checking
if len(sys.argv) is not 2:                                                   
    sys.exit('''Needs one command-line arguments, one for '''
             '''the message file and the other for the '''
             '''encrypted output file''')

PassPhrase = "Hopes and dreams of a million years"                         

BLOCKSIZE = 16                                                             
numbytes = BLOCKSIZE // 8                                                  
ctr = 0
MAXSIZE = 2 ** 16


# Create a bitvector from the ciphertext hex string:
FILEIN = open(sys.argv[1])                                                 
encrypted_bv = BitVector( hexstring = FILEIN.read() )

 
# Reduce the passphrase to a bit array of size BLOCKSIZE:
bv_iv = BitVector(bitlist = [0]*BLOCKSIZE)                                 
for i in range(0,len(PassPhrase) // numbytes):                             
    textstr = PassPhrase[i*numbytes:(i+1)*numbytes]   
    bv_iv ^= BitVector( textstring = textstr )

print 'Now brutally attacking the algorithm...'

for ctr in range(MAXSIZE):
    # Generating all possible permutations of the 16 bitvector
    key_bv = BitVector(intVal = ctr, size = BLOCKSIZE)      
      
    # Create a bitvector for storing the decrypted plaintext bit array. This bitvector has to reinitialized every time.
    msg_decrypted_bv = BitVector( size = 0 ) 

    # Carry out differential XORing of bit blocks and decryption:
    previous_decrypted_block = bv_iv                                           
    for i in range(0, len(encrypted_bv) // BLOCKSIZE):                        
        bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]                        
        temp = bv.deep_copy()                                                  
        bv ^=  previous_decrypted_block                                      
        previous_decrypted_block = temp                                        
        bv ^=  key_bv                                                           
        msg_decrypted_bv += bv                                             

    # Extract plaintext from the decrypted bitvector:    
    outputtext = msg_decrypted_bv.get_text_from_bitvector()                    
    str = outputtext
    if str.find("funerals") != -1:
        print 'You have found the key.'
        print'The key used for encryption is: ',
        print key_bv
        print 'Below is the plaintext for the given ciphertext-'
        print str
        break
