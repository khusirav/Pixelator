import random
import os
from PIL import Image, ImageDraw
i, j, a, b, c, s1, s2, s3 = 0, 0, 0, 0, 0, 0, 0, 0 
input_name = input('Введите имя фотографии с расширением\n')
output_name = input('Введите имя, под которым будет сохранён файл\n')
image = Image.open(input_name) #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.
 
Left_upper_x = 0
Left_upper_y = 0
Height_counter = 0
Width_counter = 0
Pixel_side = int(input('Введите сторону пиксела \n'))

pixels_in_height = height // Pixel_side
pixels_in_width = width // Pixel_side

while Height_counter != pixels_in_height:
    Width_counter = 0
    Left_upper_x = 0
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

        print(s1,s2,s3)
        for i in range(Left_upper_x, Left_upper_x + Pixel_side):
            for j in range (Left_upper_y, Left_upper_y + Pixel_side):
                draw.point((i, j),(s1, s2, s3))
        Width_counter += 1
        Left_upper_x+=Pixel_side
    Height_counter += 1
    Left_upper_y += Pixel_side

image.show()
image.save(output_name , "PNG")

os.system("pause")
