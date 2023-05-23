import argparse
import math
import os
import random
import sys

import numpy
import randomgen

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="Renders file to image.")
    parser.add_argument("input",
                        help="Input file path, any format")
    parser.add_argument("output",
                        help="Output file path, image file")
    parser.add_argument("--extract", "-e",
                        default="raw", help="Byte extraction algorithm")
    parser.add_argument("--render", "-r",
                        default="grayscale", help="Image render algorithm")
    parser.add_argument("--final", "-f",
                        default="save", help="Save or display the image")
    global args
    args = parser.parse_args()

    # part 1, getting bytes from image
    match args.extract:
        case "raw":
            file_bytes = get_data_raw(args.input)
        case "shuffle":
            file_bytes = get_data_shuffle(args.input)
        case "diff":
            file_bytes = get_data_diff(args.input)
        case "prng":
            file_bytes = get_data_prng(args.input)
        case "csprng":
            file_bytes = get_data_csprng(args.input)
        case "lsb":
            file_bytes = get_data_lsb(args.input)
        case _:
            sys.exit("Unknown extraction algorithm")

    # part 2, building the final image
    print(f"Bytes: {len(file_bytes)}")
    match args.render:
        case "grayscale":
            image = build_image_bw(file_bytes)
        case "rgb":
            image = build_image_rgb(file_bytes)
        case "eightbit":
            image = build_image_p(file_bytes)
        case "rgba":
            image = build_image_rgba(file_bytes)
        case "hsv":
            image = build_image_hsv(file_bytes)
        case "gif":
            image = build_image_gif(file_bytes)
        case _:
            sys.exit("Unknown render algorithm")

    # part 3, saving processed image
    print(f"Entropy: {image.entropy():.4f}")
    match args.final:
        case "save":
            image.save(args.output)
        case "show":
            image.show()
        case "saveshow":
            image.save(args.output)
            image.show()
        case "shred":
            image.save(args.output)
            os.remove(args.input)
        case "none":
            pass
        case _:
            sys.exit("Unknown final instruction")


def write_data_raw(file_name, data):
    try:
        with open(file_name, "wb") as file:
            file.write(bytes(data))
    except Exception:
        sys.exit("Error writing file")


def get_data_raw(file_name):
    try:
        with open(file_name, "rb") as file:
            return [int(i) for i in file.read()]
    except Exception:
        sys.exit("Error reading file")


def get_data_shuffle(file_name):
    data = get_data_raw(file_name)
    random.shuffle(data)
    return data


def get_data_diff(file_name):
    data = get_data_raw(file_name)
    diff = []
    for i in range(len(data) - 1):
        diff.append((data[i + 1] - data[i]) % 256)
    return diff


def get_data_prng(file_name):
    data = get_data_raw(file_name)
    random.seed(bytes(data))
    return [random.randint(0, 255) for i in range(len(data))]


def get_data_csprng(file_name):
    data = get_data_raw(file_name)
    aes_random = numpy.random.Generator(randomgen.AESCounter(seed=data))
    return [int(aes_random.integers(0, 256)) for i in range(len(data))]


def get_data_lsb(file_name):
    data = get_data_raw(file_name)
    data = [i & 1 for i in data]
    if args.render == "grayscale":
        return data
    return [255 * i for i in data]


def build_image_bw(bytes):
    size = math.ceil(math.sqrt(len(bytes)))
    image = Image.new("L", (size, size), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(size):
        for j in range(size):
            if current := next(source, None):
                pixels[j, i] = current
    return image


def build_image_rgb(bytes):
    size = math.ceil(len(bytes) / 3)
    size = math.ceil(math.sqrt(size))
    image = Image.new("RGB", (size, size), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(size):
        for j in range(size):
            current = (next(source, None), next(source, None), next(source, None))
            if None not in current:
                pixels[j, i] = current
    return image


def build_image_p(bytes):
    image = build_image_rgb(bytes)
    return image.quantize(palette=Image.WEB)


def build_image_rgba(bytes):
    size = math.ceil(len(bytes) / 4)
    size = math.ceil(math.sqrt(size))
    image = Image.new("RGBA", (size, size), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(size):
        for j in range(size):
            current = (next(source, None), next(source, None), next(source, None), next(source, None))
            if None not in current:
                pixels[j, i] = current
    return image


def build_image_hsv(bytes):
    size = math.ceil(len(bytes) / 3)
    size = math.ceil(math.sqrt(size))
    image = Image.new("HSV", (size, size), "white")
    pixels = image.load()
    source = next_byte(bytes)
    for i in range(size):
        for j in range(size):
            current = (next(source, None), next(source, None), next(source, None))
            if None not in current:
                pixels[j, i] = current
    return image.convert("RGB")


def build_image_gif(bytes):
    frames = []
    size = math.ceil(len(bytes) / 24)
    for i in range(0, len(bytes), size):
        if i + size < len(bytes):
            frames.append(build_image_rgb(bytes[i:i+size]))
        else:
            frames.append(build_image_rgb(bytes[i:]))
    frames[0].save(args.output, save_all=True, append_images=frames[1:], optimize=False, duration=42, loop=0)
    if args.final == "shred":
        os.remove(args.input)
        args.final = "none"
    return Image.open(args.output)


def next_byte(bytes):
    for i in bytes:
        yield i


if __name__ == "__main__":
    main()
