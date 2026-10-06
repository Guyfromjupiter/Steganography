import numpy as np
import hashlib as hash
import numpy as np
# let's concentrate on fibonacci conversion of image lets first print image shall we ?
from PIL import Image
Image_Name = input("enter the name of the image : ")
image = Image.open(Image_Name).convert("RGB")
data = np.array(image, dtype=np.uint8)
data = data.reshape(-1 , 3)
# print(data)
a = np.array([1,1,1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0
 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1
 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1
 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,0 ,1
 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,1])
# print(a)
fibonacci_arr = np.array([233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1])
# print(fibonacci_arr[-3])
'''
let's take 160
160 - 144 = 16

'''
def fibo(a,fibarr=fibonacci_arr):
    fib = fibarr
    temp = np.array([])
    for i in fib:
        if a >= i:
            a -= i
            temp = np.append(temp, 1)
        else:
            temp = np.append(temp, 0)

    return temp

def fibo_to_decimal (X, fibarr=fibonacci_arr):
    return int(np.dot(X, fibarr))

def TopSecretHider(x, i, k):
    # 0,1,2,3,4,5,6,7,8,9,10,11

    X = x.copy()

    if X[k] == 0 and i == 1:
        X[k] = i
        X[k+1: 11] = 0
        if X[k-1] == 1:
            X[k-1] = 0
            for p in range(k + 2, len(X)-1, 2):
                X[p] = 1
    elif X[k] == 1 and i == 0:
        X[k] = i
        X[k + 1: 11] = 0
        for p in range(k + 1, len(X)-1, 2):
            X[p] = 1

    tf = vallah_date_pixili(X)
    attempts = 0
    max_attempts = 15
    while not tf and attempts < max_attempts:
        for i in range(k-1 , -1 , -1):
            if X[i] == 1:
                X[i] = 0
                break
        for p in range(k + 1, len(X)-1):
            X[p] = 0
        for p in range(k + 1, len(X) - 1, 2):
            X[p] = 1

        tf = vallah_date_pixili(X)
        attempts += 1

    if not tf:
        raise ValueError("khel khatam")
    ans = fibo_to_decimal(X)
    return ans


def vallah_date_pixili(X):
    value = fibo_to_decimal(X)

    if not 0 <= value <= 255:
        return False

    # No consecutive 1s in the Fibonacci representation
    if np.any((X[:-1] == 1) & (X[1:] == 1)):
        return False

    return True


def ISCcombiner(Data , X):
    for v,  key in enumerate(X):
        if v>=len(Data):
            break
        if key == 0:
            arr = fibo(Data[v][1])
            Data[v][1] = TopSecretHider(arr,key,5)
        elif key == 1:
            arr = fibo(Data[v][2])
            Data[v][2] = TopSecretHider(arr,key,5)














