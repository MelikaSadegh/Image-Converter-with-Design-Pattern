from Classes.formatFactory import formatFactory

def convert_image(image, format, *args):
    factory = formatFactory()
    format_conventer = factory.create_format(format, *args)
    return image.convert()

image1 = convert_image("image", "PNG")
image2 = convert_image("image", "JPEG")
image3 = convert_image("image", "GIF")
#The orgianl image format doesn't matter, this code will convert image to the desired format.

