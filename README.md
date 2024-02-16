# Border-Watermark 边框水印

Border Watermark (边框水印) adds a white border waterwark at the bottom of each of your photo.

The text displayed in the watermark includes EXIF information read from the photo: shooting device, shooting time, shutter speed and aperture.

Various sizes are supported.

边框水印可以批量为你的照片添加一个底部的白色边框水印。

水印内容包括从照片中读取的EXIF信息：拍摄设备、拍摄时间、快门速度、光圈。

支持多种照片尺寸。

## Example 效果展示

![1708049459396](image/README/1708049459396.jpg)

![1708049512689](image/README/1708049512689.jpg)

![1708049630434](image/README/1708049630434.jpg){:height="200px"}

## How to execute 运行说明

* Please install these python packages via `pip install`:

请通过 `pip install`安装有关python环境：

```
from PIL import Image, ImageDraw, ImageFont
import exifread
import math
import os
from tqdm import tqdm
```

* Please gather the photos you want to process in a folder, and put the program files (espacially main.py) in the same folder. The program will read the photos in the current folder, create a new folder called 'output' and generate the new photos with border watermark there.

请把你要处理的照片放在一个文件夹下，然后把程序也放在这个文件夹下。该程序会在当前文件夹批量读取其中的照片，并创建一个新文件夹“output”，生成添加过水印的图片存放在output中。


* Please note that the current program only deals with jpg files. If you want to process other kinds of files, please try to manually edit the program code.

请注意，当前程序只能处理jpg文件，如果您想处理其他文件，请尝试手动修改程序代码。

* The default font in the code is called "STZHONGS.TTF" and its default path was the current folder. You can manually add this font file or convert to a certain font you want. Please note that this project is open source and does not supply or infringe on the copyright of any font. 

程序代码中使用的字体是STZHONGS.TTF并默认存放在当前文件夹下。你需要手动添加这一字体或改成其他字体。请注意，这个项目是开源的，而且并不提供和侵犯任何字体的版权。


