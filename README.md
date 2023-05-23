# file-visualiser
Visualises any computer file as an image. Applications include forensics, CTF, and art. The process is as follows:

1. Extract data from file
2. Render data to image
3. Display or save image 

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
### --extract, -e
| Argument  | Description |
| ------------- | ------------- |
| `raw` (default) | Takes the raw bytes of the file  |
| `shuffle` | Shuffles the raw bytes of the file  |
| `diff` | Takes the difference between bytes  |
| `prng` | Seeds a [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) with the bytes  |
| `csprng` | Seeds a [CSPRNG](https://en.wikipedia.org/wiki/CSPRNG) with the bytes  |
| `lsb` | Takes all the least significant bits  |

### --render, -r
| Argument  | Description |
| ------------- | ------------- |
| `grayscale` (default) | Maps the data to a grayscale image  |

### --final, -f
| Argument  | Description |
| ------------- | ------------- |
| `save` (default) | Saves image in specified location  |
| `show` | Displays image with default image viewer  |
| `saveshow` | Combination of `save` and `show`  |
| `none` | Exits without saving or displaying image  |
