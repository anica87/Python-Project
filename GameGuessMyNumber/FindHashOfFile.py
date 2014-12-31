'''
Created on Dec 30, 2014

@author: anicam
'''

import hashlib


def hash_file(filename):
    '''This function returns the SHA-1 hash of the file passed into it0 '''
    # make a hash object
    
    h = hashlib.sha1()
    
    # open file for reading in binary mode
    with open (filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
            
    # return  the hex representation of digest    
    return h.hexdigest()

message = hash_file('Kalimba.mp3')
print message

'''
When working with files in text mode, it is recommended to specify the endcoding type.
Files are stored in bytes in the disk, we need to decode them into str when we read into
We should specify a encoding type 


 w mode as it will overwrite into the file if it already exists. All previous data are erased
 The best way to do this is using the with statement. This ensures that the file is closed when the block inside with is exited
 We do not need to explicitly call the close() method. It is done internally.
 
'''