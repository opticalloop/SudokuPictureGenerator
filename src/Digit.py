import random

from PIL import Image, ImageFont, ImageDraw
from PIL.ImageFont import FreeTypeFont

from src.Font import Font
from src.Rotate import Rotate


class Digit:
    def __init__(self, value: int, font: FreeTypeFont) -> None:
        super().__init__()
        self._value = value
        self._img = Image.new(mode="L", size=(28, 28), color="#fff")  # 8-bit pixels, black and white
        self._image_editable = ImageDraw.Draw(self._img)

        self._font = font
        self._numbers_positions = list()
        self._string = ""


    def place_case(self):
        self._image_editable.text((10, 0), str(self._value), 0, font=self._font)


    def save(self, index):
        """
        Save picture in this format : digit_{index}_{digit_value}.jpg
        """
        self._img.save(f"export/Digits-Only/digit_{index}_{self._value}.jpg")
