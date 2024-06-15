from abc import ABC, abstractmethod

class Image(ABC):
    def __init__(self, format, width, height, pixels):
        self.format = format
        self.width  = width
        self.height = height
        self.pixels = pixels
    
    @abstractmethod
    def convert(self):
        pass