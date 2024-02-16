from fractions import Fraction

from PIL import Image, ImageDraw, ImageFont
import exifread
import math
import os
from tqdm import tqdm

if not os.path.exists("output"):
    os.makedirs("output")

file_list = [filename for filename in os.listdir() if filename.endswith(".jpg")]

# file_list = [filename for filename in os.listdir() if filename.endswith(".jpg") and not filename.startswith("output_")]

# for image_filename in file_list:
for image_filename in tqdm(file_list, desc="Processing images"):  # 使用tqdm创建进度条

    image_filename = image_filename

    # 读入图片
    image = Image.open(image_filename)

    # 获取图片宽度和高度
    width, height = image.size

    # 创建一条白边
    border_height = int((0.15-0.03*(height/width)) * height)
    border = Image.new('RGB', (width, border_height), (255, 255, 255))

    # 合并图片和白边
    image_with_border = Image.new('RGB', (width, height + border_height))
    image_with_border.paste(image, (0, 0))
    image_with_border.paste(border, (0, height))

    # 读取图片的Exif信息
    with open(image_filename, 'rb') as image_file:
        tags = exifread.process_file(image_file)

    # 从Exif信息中获取相机品牌、型号、拍摄时间、光圈和快门信息
    camera_make = str(tags.get('Image Make', 'Unknown'))
    camera_model = str(tags.get('Image Model', 'Unknown'))

    shoot_time = str(tags.get('EXIF DateTimeOriginal', 'Unknown'))
    
    # 原始日期时间格式
    # shoot_time_tag = tags.get('EXIF  DateTimeOriginal')
    # original_shoot_time = str(shoot_time_tag)
    # if shoot_time_tag:
    #     # 将冒号替换为斜杠，只影响日期部分
    #     formatted_shoot_time = original_shoot_time.replace(":", "/")
    #     # 使用格式化的日期时间
    #     shoot_time = formatted_shoot_time
    # else:
    #     shoot_time  = 'Unknown'

    shutter_speed = str(tags.get('EXIF ExposureTime', 'Unknown'))

    # 获取快门速度并转换格式
    aperture_tag = tags.get('EXIF FNumber')
    if aperture_tag:
        # 如果快门速度有效，将其转换为浮点数并保留一位小数
        aperture = float(Fraction(str(aperture_tag)))
        aperture = f"F{aperture:.1f}"
    else:
        aperture = 'Unknown'

    # 创建ImageDraw对象来在图片上绘制文本
    draw = ImageDraw.Draw(image_with_border)

    if width > height:
        # 横构图
        # 设置文本字体和大小
        # font = ImageFont.load_default()
        font_height = int((0.15 + 0.06 * (height / width)) * border_height)
        font = ImageFont.truetype("STZHONGS.TTF", font_height)
        text = f"{camera_make} {camera_model}   |   {shoot_time}   |   Aperture: {aperture}   |   Shutter Speed: {shutter_speed}"
        text_width, text_height = draw.textsize(text, font)
        # 计算文本的位置
        text_x = (width - text_width) // 2
        text_y = height + (border_height - text_height) // 2

        # 在白边上绘制文本
        draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

    else:
        # 竖构图
        # 设置文本字体和大小
        # font = ImageFont.load_default()
        font_height = int((0.12 + 0.04 * (height / width)) * border_height)
        font = ImageFont.truetype("STZHONGS.TTF", font_height)

        line1 = f"{camera_make} {camera_model}   |   {shoot_time}"
        line2 = f"Aperture: {aperture}   |   ShutterSpeed: {shutter_speed}"
        text_width1, text_height1 = draw.textsize(line1, font)
        text_width2, text_height2 = draw.textsize(line2, font)

        text_x1 = (width - text_width1) // 2
        text_x2 = (width - text_width2) // 2
        text_y1 = height + (border_height - text_height1 - text_height2) // 2
        text_y2 = text_y1 + text_height1

        # 在白边上绘制两行文本
        draw.text((text_x1, text_y1), line1, fill=(0, 0, 0), font=font)
        draw.text((text_x2, text_y2), line2, fill=(0, 0, 0), font=font)

    # 保存最终图片到 "output" 子文件夹
    output_filename = os.path.join("output", "output_" + image_filename)
    image_with_border.save(output_filename)

    # 关闭图片
    image.close()
