from Classes.image import Image
from Classes.gif   import GIF
from Classes.jpeg  import JPEG
from Classes.png   import PNG

class imageFormatConventer:

    def __init__(self, image):
       if not isinstance(image, Image): 
            raise TabError("Input is not an Image!")
       self.image = image

    def convert(self):
        if isinstance(self, Image, GIF):
            pass
        elif isinstance(self, Image, JPEG):
            pass
        elif isinstance(self, Image, PNG):
            pass
        else: 
            raise NotImplementedError("There is no adapter for the input")
    class gifAdapter:

        def __init__(self, gif):
            if not isinstance(gif, GIF):
                pass
            self.gif = gif
        
    class jpegAdapter:

        def __init__(self, jpeg):
            if not isinstance(jpeg, JPEG):
                pass
            self.jpeg = jpeg

    class pngAdapter:

        def __init__(self, png):
            if not isinstance(png, PNG):
                pass
            self.jpeg = png


