from Classes.image                import Image
from Classes.gif                  import GIF
from Classes.jpeg                 import JPEG
from Classes.png                  import PNG
from Classes.imageFormatConverter import imageFormatConventer

print(imageFormatConventer("image", "PNG").calculate())
print(imageFormatConventer("image", "JPEG").calculate())
print(imageFormatConventer("image", "GIF").calculate())


