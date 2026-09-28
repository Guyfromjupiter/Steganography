import numpy as np
import hashlib as hash
a = "hello"
#this create ',\xf2M\xba_\xb0\xa3\x0e&\xe8;*\xc5\xb9\xe2\x9e\x1b\x16\x1e\\\x1f\xa7B^s\x043b\x93\x8b\x98$'

digest = hash.sha256(a.encode()).digest()
h = int.from_bytes(digest[:8], byteorder='big')
rand_Seed = np.random.default_rng(h)
rArray = rand_Seed.random((256, 256))
print(rArray)