# coding=utf-8

'''
@company:guomingyu
@version:0.1
@file:image_transformation.py
@time:2019/06/06
@function:128*128
'''
from PIL import Image
import os.path
import glob

class image_aspect():

    def __init__(self, image_file, aspect_width, aspect_height):
        self.img = Image.open(image_file)
        self.aspect_width = aspect_width
        self.aspect_height = aspect_height
        self.result_image = None

    def change_aspect_rate(self):

        img_width = self.img.size[0]
        img_height = self.img.size[1]

        if img_width > img_height:
            rate = self.aspect_width / img_width
        else:
            rate = self.aspect_height / img_height

        rate = round(rate, 1)
        self.img = self.img.resize((int(img_width * rate), int(img_height * rate)))
        return self

    def past_background(self):
        self.result_image = Image.new("RGB", [self.aspect_width, self.aspect_height], (0, 0, 0, 255))
        self.result_image.paste(self.img, (int((self.aspect_width - self.img.size[0]) / 2), int((self.aspect_height - self.img.size[1]) / 2)))
        return self

    def save_result(self, file_name):
        self.result_image.save(os.path.join('you save route', os.path.basename(file_name)))
        #self.result_image.save(file_name)

#example
if __name__ == "__main__":
	for image_file in glob.glob('you read path*.jpg'):
		print ('converting %s ... ' % (image_file))
		try:
			image_aspect(image_file, 128, 128)\
				.change_aspect_rate()\
				.past_background()\
				.save_result(image_file)
			print ('Successfully saved  ... ' )
		except Exception as e:
			print ('Save failed %s ... ' % e)
print ('...complete...')
