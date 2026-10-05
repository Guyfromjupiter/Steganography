import numpy as np
import hashlib as hash
import numpy as np
# let's concentrate on fibonacci conversion of image lets first print image shall we ?
from PIL import Image
Image_Name = input("enter the name of the image : ")
image = Image.open(Image_Name)
data = np.array(image.get_flattened_data(), dtype=np.uint8)
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

    return X

def validate_pixel(X):
    value = fibo_to_decimal(X)

    if not 0 <= value <= 255:
        return False

    # No consecutive 1s in the Fibonacci representation
    if np.any((X[:-1] == 1) & (X[1:] == 1)):
        return False

    return True



pixel = 172
coefficients = fibo(pixel)

modified = TopSecretHider(coefficients, 1, 4)

print("Original:", pixel)
print("Before:", coefficients)
print("After:", modified)
print("New pixel:", fibo_to_decimal(modified))
print("Valid:", validate_pixel(modified))
print("Embedded bit:", modified[4])

        
        








