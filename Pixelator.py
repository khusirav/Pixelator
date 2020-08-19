import random
from PIL import Image, ImageDraw

Close_check = '0'

while Close_check != '1':

    i, j, a, b, c, s1, s2, s3 = 0, 0, 0, 0, 0, 0, 0, 0 
    input_name = input('Enter image name (with extention)\n')
    output_name = input('Enter a name to save pixelart\n')
    image = Image.open(input_name) 
    draw = ImageDraw.Draw(image) #Creating a drawing instrument 
    width = image.size[0] 
    height = image.size[1] 
    pix = image.load() #Loading the pixels info
    
    Left_upper_x = 0
    Left_upper_y = 0
    Height_counter = 0
    Width_counter = 0
    Pixel_side = int(input('Enter a pixel side value\n'))

    pixels_in_height = height // Pixel_side
    pixels_in_width = width // Pixel_side

    while Height_counter != pixels_in_height:
        Width_counter = 0
        Left_upper_x = 0
        #s1_was_max = False
        #s2_was_max = False
        #s3_was_max = False
        while Width_counter != pixels_in_width:
            
            for i in range(Left_upper_x, Left_upper_x + Pixel_side):
                for j in range (Left_upper_y, Left_upper_y + Pixel_side):
                    a = pix[i,j] [0]
                    b = pix[i,j] [1]
                    c = pix[i,j] [2]
                    s1 += a
                    s2 += b
                    s3 += c

            s1 = round(s1/Pixel_side**2)
            s2 = round(s2/Pixel_side**2)
            s3 = round(s3/Pixel_side**2)

            #if s1 == max(s1,s2,s3):
            #    s1_was_max = True
        
            #if s2 == max(s1,s2,s3): 
            #    s2_was_max = True
            
            #if s3 == max(s1,s2,s3):
            #    s3_was_max = True
            

            if abs(s1-65) == min(abs(s1-65), abs(s1-190), abs(s1-255)):
                s1 = 65
            if abs(s1-190) == min(abs(s1-65), abs(s1-190), abs(s1-255)):
                s1 = 190
            if abs(s1-255) == min(abs(s1-65), abs(s1-190), abs(s1-255)):
                s1 = 255

            if abs(s2-65) == min(abs(s2-65), abs(s2-190), abs(s2-255)):
                s2 = 65
            if abs(s2-190) == min(abs(s2-65), abs(s2-190), abs(s2-255)):
                s2 = 190
            if abs(s2-255) == min(abs(s2-65), abs(s2-190), abs(s2-255)):
                s2 = 255

            if abs(s3-65) == min(abs(s3-65), abs(s3-190), abs(s3-255)):
                s3 = 65
            if abs(s3-190) == min(abs(s3-65), abs(s3-190), abs(s3-255)):
                s3 = 190
            if abs(s3-255) == min(abs(s3-65), abs(s3-190), abs(s3-255)):
                s3 = 255
  
            #if ((s1==65) and (s2==65) and (s3==65)):
                #if s1_was_max == True:
                    #s1 = 130
                #if s2_was_max == True:
                    #s2 = 130
                #if s3_was_max == True:
                    #s3 = 130

            #s1_was_max = False
            #s1_was_max = False
            #s1_was_max = False

            print(s1,s2,s3)
            for i in range(Left_upper_x, Left_upper_x + Pixel_side):
                for j in range (Left_upper_y, Left_upper_y + Pixel_side):
                    draw.point((i, j),(s1, s2, s3))

            Width_counter += 1
            Left_upper_x += Pixel_side

        Height_counter += 1
        Left_upper_y += Pixel_side

    image.show()
    image.save(output_name , "PNG")
    Close_check = input('Enter 1 to close the program\n')

