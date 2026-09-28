from PIL import Image
import numpy as np
Image_Name = input("enter the name of the image : ")
image = Image.open(Image_Name)
Grayscale_Image = image.convert('L')
Grayscale_Image.save("GreyScaleImage.png")

Message = str(input ('enter the message : '))
Binary = ''.join(format(ord(x), '08b') for x in Message)

grayOutputImage = Grayscale_Image

wid, hgt = grayOutputImage.size

data = np.array(grayOutputImage.get_flattened_data() , dtype=np.uint8)

data = data.reshape((hgt, wid))

OutputData = np.array([])

message_index = 0
pixel_count = 0

for element in np.nditer(data, op_flags=['readwrite']):
    pixel = element.item()
    pixel_count += 1
    if pixel_count % 100 == 0:
        print(pixel_count)

    if message_index < len(Binary):
        #here we are converting the binary which was in format of string from above to the format of int
        message_bit = int(Binary[message_index])
        element[...] = (pixel & 254) | message_bit
        message_index += 1

OutputData = data.reshape((hgt, wid))
OutputImage = Image.fromarray(data , 'L')

OutputImage.save("StegoImage.png")
OutputImage = Image.open("../testing tools/StegoImage.png")
InputImage = Image.open("../testing tools/GreyScaleImage.png")
