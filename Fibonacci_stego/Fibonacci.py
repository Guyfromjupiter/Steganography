from PIL import Image
import numpy as np
import secrets
import hashlib as hash

import random
# C:\Users\Sukhu\Desktop\suku_sign_copy_1_2.jpg
class Fibonacci:
    def __init__(self):
        image_name = input("enter the name of the image : ")
        image = Image.open(image_name)
        self.image = image
        self.message = input("enter the message : ")
        self.data = np.array(image.get_flattened_data(), dtype=np.uint8)
        self.fibonacci_arr = np.array([233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1])

    def message_encryption(self):

        sec_key_arr = []
        for i in range(10):
            sec_key = ''.join(secrets.choice(self.message) for i in range(32))
            upp_sec_key = ''.join(i.upper() if i.isalpha() and secrets.randbelow(2) else i.lower()
                                  for i in sec_key)
            sec_key_arr = np.append(sec_key_arr, upp_sec_key)

        secret_key = secrets.choice(sec_key_arr)
        sec_key = self.key_to_cipher(secret_key)
        rand_Seed = np.random.default_rng(sec_key)
        rArray = rand_Seed.random((256,256))

        # in numpy array we can directly do the comparison operator with entire array

        simpli_cell = (rArray >= 0.5).astype(np.uint8)




    def key_to_cipher(self , key):
        # what does this do is first sha 256 return 256 bit of hash, digest convert it to bytes
        # .encode() is just to formalize the string
        # int class has from_bytes which treat byte as int
        # byte order tells how to order the bytes big being most significant bit first and little mean least insignificant bit first

        sec_digest = hash.sha256(key.encode()).digest()
        # First 8 bytes = 64-bit seed
        h = int.from_bytes(sec_digest[:8], byteorder='big')
        return h

    def fibonacci(self):
        pass

# fib = Fibonacci()
# fib.message_encryption()


