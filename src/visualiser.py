import argparse
import math
import sys

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="Visualises any file to an image.")
    parser.add_argument("input", help="Input file path, any format", type=str)
    parser.add_argument("output", help="Output file path, image file", type=str)
    parser.add_argument("--extract", "-e", default="raw", help="Byte extraction algorithm", type=str)
    parser.add_argument("--render", "-r", default="bw", help="Image rendering algorithm", type=str)
    parser.add_argument("--final", "-f", default="save", help="Save or display the image", type=str)
    args = parser.parse_args()

    # part 1, getting bytes from image
    match args.extract:
        case "raw":
            file_bytes = get_data_raw(args.input)
        case _:
            sys.exit("Unknown extraction algorithm")

    # part 2, building the final image
    match args.render:
        case "bw":
            image = build_image_bw(file_bytes)
        case _:
            sys.exit("Unknown rendering algorithm")

    # part 3, saving processed image
    match args.final:
        case "save":
            image.save(args.output)
        case _:
            sys.exit("Unknown final instruction")


def get_data_raw(file_name):
    try:
        with open(file_name, "rb") as file:
            return [int(i) for i in file.read()]
    except Exception:
        sys.exit("Error reading file")


def build_image_bw(bytes):
    size = math.ceil(math.sqrt(len(bytes)))
    image = Image.new("L", (size, size), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(size):
        for j in range(size):
            if current := next(source, None):
                pixels[i, j] = current
    return image


def next_byte(bytes):
    for i in bytes:
        yield i


if __name__ == "__main__":
    main()
