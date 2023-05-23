import math, sys

from PIL import Image

def main():
    # part 1, getting bytes in the image
    file_bytes = get_file_raw()
    # part 2, actually building the image
    try:
        size = math.ceil(math.sqrt(len(file_bytes)))
        image = build_image_bw(file_bytes, size)
    except:
        sys.exit("Error building image")
    # part 3, saving the completed image
    image.save(input("Output image: "))

def get_file_raw():
    while True:
        try:
            with open(input("Input file: "), "rb") as file:
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

def write_bytes(raw_data):
    while True:
        try:
            with open(input("Output file: "), "wb") as file:
                file.write(bytes(raw_data))
        except:
            raise ValueError("Error writing file")
        else:
            break

if __name__ == "__main__":
    main()
