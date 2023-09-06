from tkinter import *
from PIL import Image, ImageOps

new_width = 50
ascii_char = ["@", "!", "$", "%", "^", "&", "*", "~", ",", "`", "\"", "=", ">", ".", " "]

ascii_char_alt = ["@", "!", "$", "%", "^", "&", "*", "~", ",", "`", "\"", "=", ">", "{", "}", "[", "]", "?", "±", "§",
                  "+", "#", "|", ":", ".", " "]

# image must be in same location as .py file
pre_image = Image.open("image.png")


def process_image(image):
    image_width, image_height = image.size
    ratio = image_height / image_width
    new_height = int(ratio * new_width)
    new_image = image.resize((new_width, new_height))

    new_image = ImageOps.grayscale(new_image)

    return new_image


def ascii_generator():
    new_image = process_image(pre_image)
    new_image.save("newimage.png")
    get_pixels = new_image.getdata()

    char_string = ""
    for a in get_pixels:
        char_string += "".join(ascii_char[a//18])
        char_string += " "

    return char_string


img_string = ascii_generator()
final_image = "\n".join(img_string[i:(i + (new_width * 2))] for i in range(0, len(img_string), new_width * 2))

root = Tk()
label1 = Text(root, wrap=WORD, font=("", 5), width=150, height=100)
label1.insert(INSERT, final_image)
label1.grid(row=0, column=0)
root.mainloop()

with open("ascii_prime.txt", "w") as f:
    f.write(final_image)
