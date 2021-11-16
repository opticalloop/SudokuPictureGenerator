import random
import threading

from PIL import Image, ImageFont, ImageDraw
from PIL.ImageFont import FreeTypeFont

from src.Font import Font
from queue import LifoQueue

from src.Rotate import Rotate


class Limit_Stack:
    limit = 32
    lock = threading.Lock()


class Digit:
    def __init__(self, value, font: FreeTypeFont) -> None:
        super().__init__()
        self._value = value
        self._img = Image.new(mode="L", size=(28, 28), color="#fff")  # 8-bit pixels, black and white
        self._image_editable = ImageDraw.Draw(self._img)

        self._font = font
        self._numbers_positions = list()
        self._string = ""

    def place_case(self,r = 0):

        try:
            self._image_editable.text((10, 0), str(self._value), 0, font=self._font)
        except OSError:
            if r < 100:
                print(f"Thread n°{self._value} crashed on place_case method ... Retry")
                self.place_case(r + 1)

    def save(self, index):
        """
        Save picture in this format : digit_{index}_{digit_value}.jpg
        """
        self._img.save(f"export/Digits-Only/digit_{index}_{self._value}.jpg")


class Digits(threading.Thread):
    def __init__(self, font: Font, index: int,characters: list):
        self._font = font
        self._index = index
        self._characters = characters
        super().__init__()

    def run(self) -> None:
        self._font.download()
        font_type = ImageFont.truetype(f'export/fonts/{self._font.name}.ttf', 20)
        for i in self._characters:
            digit = Digit(i, font_type)
            digit.place_case()
            digit.save(self._index)
        with Limit_Stack.lock:
            Limit_Stack.limit += 1
