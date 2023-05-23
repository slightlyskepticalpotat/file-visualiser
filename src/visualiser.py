import argparse
import math
import sys

from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Visualises any file to an image.")
    parser.add_argument("input", help="Input file name or file path, any file format", type=str)
    parser.add_argument("output", help="Output file name or file path, image file format", type=str)
    args = parser.parse_args()
    # part 1, getting bytes from image
    file_bytes = get_data_raw(args.input)
    # part 2, building the final image
    size = math.ceil(math.sqrt(len(file_bytes)))
    try:
        image = build_image_bw(file_bytes, size)
    except:
        sys.exit("Error building image")
    # part 3, saving the completed image
    image.save(args.output)

def get_data_raw(file_name):
    try:
        with open(file_name, "rb") as file:
            return [int(i) for i in file.read()]
    except:
        raise ValueError("Error reading file")

def build_image_bw(bytes, x):
    image = Image.new("L", (x, x), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(x):
        for j in range(x):
            if current := next(source, None):
                pixels[i, j] = current
    return image

def next_byte(bytes):
    for i in bytes:
        yield i

if __name__ == "__main__":
    main()
