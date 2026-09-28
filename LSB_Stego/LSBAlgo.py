#gray scalling

from PIL import Image
import numpy as np
Image_Name = input("enter the name of the image : ")
image = Image.open(Image_Name)
Grayscale_Image = image.convert('L')
Grayscale_Image.save("GreyScaleImage.png")


#Convert the message into binary
#this is second step. we are not doing resize. it is not needed for now
#ord function returns unicode value of a specific character
#format return formatted value according to formatter given
#we are using 'b' here for binary
Message = str(input ('enter the message : '))
Binary = ''.join(format(ord(x), '08b') for x in Message)

#intialize the input gray scale image into output gray scale image
grayOutputImage = Grayscale_Image

#traverse the image
#we will be using numpy for this

wid, hgt = grayOutputImage.size

data = np.array(grayOutputImage.get_flattened_data() , dtype=np.uint8)# convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
# converts it into row
#suppose wid = 4 and hgt = 3
#pixels are 12 in total
#[10 ,20, 30, 40, 50, 60, 70, 80, 90, 100, 120]
data = data.reshape((hgt, wid))
# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].
OutputData = np.array([])

message_index = 0
pixel_count = 0
#this is the main logic of traversal
# well let me tell you what is happening
# we apply for loop to loop the data, data being the numpy array we got
# np.nditer(data) interate over all scalar value of data
# scalar value is like single value, a numpy scalar is kind og integer that follows numpy rule
#well optimizing to be doine taking a lot of time
# so after optimization this is the code, yes lets explain it op_flags readwrite gives me a way to both read and modify the pixel which i get from the data
#gone is the other array as copyting it was bad, and it was not worth it as only few 100 of first pixel is needed
#
for element in np.nditer(data, op_flags=['readwrite']):
    pixel = element.item()
    pixel_count += 1
    if pixel_count % 100 == 0:
        print(pixel_count)

    if message_index < len(Binary):
        #here we are converting the binary which was in format of string from above to the format of int
        message_bit = int(Binary[message_index])

        #most imp part which even i learn just recently is this
        # with this we are changing only the last bit of the pixel or least significant pixel grey scale pixel range is from  0 to 255 or 8 bit value
        # here we are kinda forcing the pixel value using and gate to reemain same and only change the last value
        # as we know and is only 1 when both is 1, and we know int or any value is stored in format of binary so binary and on them will cause it to implicitly change and do the
        # operation
        #now thw main logic is as follow
        # lets take a pixel value of 11010011 and operate and operate AND on it we get
        #11010011 = 211
        #11111110 = 254
        #11010010 = 210 so we gurantee last digit would be 0 in any case
        # after which we apply OR with message bit let say message bit is 1
        #11010010 = 210
        #00000001 = 1
        #is 11010011 = 211
        #or else is message bit is 0
        #new pixel still is 11010010

        element[...] = (pixel & 254) | message_bit
        message_index += 1


'''
my earlier very time consuming idea, well it was the first thing i though up and well thats how it is 
for element in np.nditer(data):
    pixel = element.item()
    pixel_count += 1
    if pixel_count % 100 == 0:
        print(pixel_count)

    if message_index < len(Binary):
        message_bit = Binary[message_index]

        binary_fixed = format(pixel, '08b')
        last_bit = binary_fixed[-1]
        if last_bit == Binary[message_index]:
            OutputData = np.append(OutputData ,element)

        elif last_bit != Binary[message_index]:
            binary_fixed = binary_fixed[:-1] + message_bit
            OutputData =np.append(OutputData, int (binary_fixed, 2))

        message_index += 1
    else:
        OutputData =  np.append(OutputData, int(element))
'''

OutputData = data.reshape((hgt, wid))
OutputImage = Image.fromarray(data , 'L')

OutputImage.save("StegoImage.png")
OutputImage = Image.open("../testing tools/StegoImage.png")
InputImage = Image.open("../testing tools/GreyScaleImage.png")









