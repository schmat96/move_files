#!/bin/python
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import shutil


def get_image_year_month(image):
    image = Image.open(image)
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        if tag == 'DateTime':

            date_format = '%Y:%m:%d %H:%M:%S'
            date_obj = datetime.strptime(data, date_format)
            return [date_obj.year, date_obj.month]

input_path = sys.argv[1]
output_path = sys.argv[2]
print(output_path)
files = [f for f in os.listdir(input_path)]
for file in files:
    path_of_file = os.path.join(input_path, file)
    if os.path.isfile(path_of_file):
        year_month = get_image_year_month(path_of_file)
        year = year_month[0]
        month = year_month[1]
        # print(year, month)
        outputyear = os.path.join(output_path, str(year))
        outputmonth = os.path.join(outputyear, str(year) + "-" + str(month).zfill(2))

        if os.path.exists(outputyear) == False:
            os.mkdir(outputyear)
        if os.path.exists(outputmonth) == False:
            os.mkdir(outputmonth)

        shutil.copyfile(path_of_file, os.path.join(outputmonth, file))
        # print(outputyear, outputmonth)



