#reference used which turned out to be the simplest way just for testing purposes
#for me -- the syntax setup -- not meaning the hashlib is a simple construct nor the md5
#https://bobbyhadz.com/blog/python-calculate-md5-hash-checksum-of-file

import hashlib


file_name1 = 'file1.txt'
file_name2 = 'file2.txt'

with open(file_name1, 'rb') as file_obj:
    file_contents = file_obj.read()

    md5_hash = hashlib.md5(file_contents).hexdigest()

    print(md5_hash + 'file1')

with open(file_name2, 'rb') as file_obj:
    file_contents = file_obj.read()

    md5_hash = hashlib.md5(file_contents).hexdigest()

    print(md5_hash + 'file2')
