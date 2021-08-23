import os
from Scripts.utils import compress_clip, categorize


GoPro_Path = 'E:\\DCIM\\100GOPRO'
GoPro_files = os.listdir(GoPro_Path)

for f in GoPro_files:
    file_split = os.path.splitext(f'{GoPro_Path}\{f}')
    name_split = os.path.splitext(f)
    source_file_name = name_split[0]
    source_file_path = file_split[0]
    source_file_ext = file_split[1]
    

    catagory = categorize(source_file_ext)

    print (catagory)