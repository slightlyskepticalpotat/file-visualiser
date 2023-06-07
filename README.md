# file-visualiser
Visualises any computer file as an image. Applications include forensics, CTF, and art. Note that in most cases, the image is only intended as an approximation of the input data—the aformentioned data may not always be easily recoverable. The process is as follows:

1. Extract data from file
2. Render data to image
3. Display or save image 

## Install
```bash
git clone https://github.com/slightlyskepticalpotat/file-visualiser.git
cd file-visualiser
pip install -r requirements.txt
python3 visualiser.py --help
```

## Usage
```py
usage: visualiser.py [-h] [--extract EXTRACT] [--render RENDER] [--final FINAL] input output

Renders file to image.

positional arguments:
  input                 Input file path, any format
  output                Output file path, image file

options:
  -h, --help            show this help message and exit
  --extract EXTRACT, -e EXTRACT
                        Byte extraction algorithm
  --render RENDER, -r RENDER
                        Image render algorithm
  --final FINAL, -f FINAL
                        Save or display the image
```

## Options
### --extract, -e
| Argument  | Description |
| ------------- | ------------- |
| `raw` (default) | Takes the raw bytes of the file  |
| `reverse` | Reverses the raw bytes of the file  |
| `shuffle` | Shuffles the raw bytes of the file  |
| `diff` | Takes the difference between bytes  |
| `prng` | Seeds a [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) with the bytes  |
| `csprng` | Seeds a [CSPRNG](https://en.wikipedia.org/wiki/CSPRNG) with the bytes  |
| `lsb` | Takes all the least significant bits  |

### --render, -r
| Argument  | Description |
| ------------- | ------------- |
| `grayscale` (default) | Maps the data to a grayscale image  |
| `rgb` | Maps the data to a [RGB](https://en.wikipedia.org/wiki/RGB_color_model) colour image  |
| `eightbit` | Maps to a 256-colour image  |
| `rgba` | Maps to a [RGBA](https://en.wikipedia.org/wiki/RGBA_color_model) colour image  |
| `cmyk` | Maps to a [CMYK](https://en.wikipedia.org/wiki/CMYK_color_model) colour image  |
| `hsv` | Maps to a [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) colour image  |
| `gif` | Maps data to a 1-second [GIF](https://en.wikipedia.org/wiki/GIF)  |

### --final, -f
| Argument  | Description |
| ------------- | ------------- |
| `save` (default) | Saves image in specified location  |
| `show` | Displays image with default image viewer  |
| `saveshow` | Combination of `save` and `show`  |
| `shred` | Saves image and deletes input file  |
| `shredshow` | Saves and shows image, deletes input  |
| `dump` | Dumps processed bytes as Python list  |
| `none` | Exits without saving or displaying image  |
