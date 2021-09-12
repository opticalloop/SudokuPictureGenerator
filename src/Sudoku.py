import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter

from PIL import Image

from src.Font import Font

from src.Rotate import Rotate


class Sudoku:
    def __init__(self, image: Image, font: Font, difficulty) -> None:
        super().__init__()
        self._img = image
        self._image_editable = ImageDraw.Draw(image)

        font.download()
        self._font = ImageFont.truetype(f'export/fonts/{font.name}.ttf', 50)

        self._numbers_positions = list()
        self._string = ""
        self._mode = difficulty

    def __place_case(self):
        while True:
            x, y = random.randint(0, 8), random.randint(0, 8)
            if (x, y) not in self._numbers_positions:
                self._numbers_positions.append((x, y))
                break
        value = random.randint(1, 9)
        self._image_editable.text((150 + 80 * (x + 0.3), 128 + 80 * (y + 0.2)), str(value), 0,
                                  font=self._font)
        self._string += f"({x},{y},{value})"

    def place_cases(self, nb: int):
        """
        Place nb case in the sudoku
        :param nb: Number of cases
        """
        for i in range(nb):
            self.__place_case()

    def rotate_img(self):
        """
        Rotate picture
        """
        if Rotate.auto_rotate:
            self._img = self._img.rotate(random.randint(Rotate.min, Rotate.max), fillcolor="#fff")

    def add_filters(self):
        self._img.effect_noise((5, 5))

    def transform_img(self):
        width, height = self._img.size
        m = random.uniform(-0.3, 0.3)
        xshift = abs(m) * width
        new_width = width + int(round(xshift))
        self._img = self._img.transform((new_width, height), Image.AFFINE,
                                        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC, fillcolor="#fff")

    def save(self, index):
        """
        Save picture
        """
        self._img.save(f"export/{self._mode}/sudoku_{index}.jpg")

    def resize_img(self):
        scale = random.uniform(1, 3)
        self._img = self._img.resize((int(self._img.width // scale), int(self._img.height // scale)))

    def export_string(self, index):
        return f"{index} {self._string}\n"
