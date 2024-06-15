from .jpeg import JPEG
from .png  import PNG
from .gif  import GIF

class formatFactory:
    def create_format(self, format, *args):
        self.image_classes = {
            "JPEG": JPEG,
            "PNG" : PNG,
            "GIF" : GIF
        }
        image_class = self.image_classes.get(format)
        return image_class(format, *args)