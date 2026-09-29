import numpy as np
import hashlib as hash
import numpy as np

simpli_cell = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
])
for i in range(50):
    up = np.roll(simpli_cell, -1, axis=0)
    up[-1, :] = 0
    down = np.roll(simpli_cell, 1, axis=0)
    down[0, :] = 0
    left = np.roll(simpli_cell, -1, axis=1)
    left[:, -1] = 0
    right = np.roll(simpli_cell, 1, axis=1)
    right[:, 0] = 0

    up_left = np.roll(up, -1, axis=1)
    up_right = np.roll(up, 1, axis=1)
    down_left = np.roll(down, -1, axis=1)
    down_right = np.roll(down, 1, axis=1)

    neigh_count = (up + down + left + right + up_left + up_right + down_left + down_right)
    next_gen = neigh_count % 2
    arrTF = (simpli_cell == next_gen)
    arrT = arrTF[np.where(arrTF)]
    if
    print(arrT)



