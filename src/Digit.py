import random

from PIL import Image, ImageFont, ImageDraw

from src.Font import Font
from src.Rotate import Rotate


class Digit:
    def __init__(self, font: Font) -> None:
        super().__init__()
        self._value = random.randint(1, 9)
        self._img = Image.new(mode="L", size=(28, 28), color="#fff") #8-bit pixels, black and white
        self._image_editable = ImageDraw.Draw(self._img)

        font.download()
        self._font = ImageFont.truetype(f'export/fonts/{font.name}.ttf', 20)

        self._numbers_positions = list()
        self._string = ""

    def place_case(self):
        self._image_editable.text((10, 0), str(self._value), 0,
                                  font=self._font)

    def rotate_img(self):
        """
        Rotate picture
        """
        if Rotate.auto_rotate:
            self._img = self._img.rotate(random.randint(Rotate.min, Rotate.max), fillcolor="#fff")

    # def add_filters(self):
    #     na = np.array(YourPILImage)
    #     self._img.effect_noise((5, 5))

    def transform_img(self):
        width, height = self._img.size
        m = random.uniform(0, 0.3)
        xshift = abs(m) * width
        new_width = width + int(round(xshift))
        self._img = self._img.transform((new_width, height), Image.AFFINE,
                                        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC, fillcolor="#fff")

    def save(self, index):
        """
        Save picture in this format : digit_{index}_{digit_value}.jpg
        """
        self._img.save(f"export/Digits-Only/digit_{index}_{self._value}.jpg")

    def resize_img(self):
        scale = random.uniform(1, 3)
        self._img = self._img.resize((int(self._img.width // scale), int(self._img.height // scale)))
