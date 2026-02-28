import sys
from PIL import Image
from PIL import ImageOps



def shirt(input, output):
    check_input(input, output)
    try:
        with Image.open(input) as input_img, Image.open("shirt.png") as shirt_img:
            new_img = ImageOps.fit(input_img, (600, 600))
            new_img.paste(shirt_img, mask=shirt_img, box=None)
            new_img.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_input(input, output):
    input_ext = input.lower().split(".")[1]
    output_ext = output.lower().split(".")[1]
    extensions = ["jpg", "jpeg", "png"]
    if input_ext not in extensions or output_ext not in extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")


def get_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        shirt(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    get_input()

