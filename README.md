# file-visualiser
Visualises any computer file as an image. Applications include forensics, CTF, and art.

## Install
```bash
git clone https://github.com/slightlyskepticalpotat/file-visualiser.git
cd file-visualiser
pip install -r requirements.txt
cd src
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
### --extract
| Argument  | Description |
| ------------- | ------------- |
| `raw` (default) | Takes the raw bytes of the file  |

### --render
| Argument  | Description |
| ------------- | ------------- |
| `grayscale` (default) | Maps the data to a grayscale image  |

### --final
| Argument  | Description |
| ------------- | ------------- |
| `save` (default) | Saves image in specified location  |
| `show` | Displays image with default image viewer  |
| `saveshow` | Combination of `save` and `show`  |
| `none` | Exits without saving or displaying image  |
