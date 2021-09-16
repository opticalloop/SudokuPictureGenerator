import os
import random

from src.Digit import Digit
from src.Font import Fonts
from PIL import Image, ImageFont
import json

from src.Rotate import Rotate
from src.Sudoku import Sudoku


class Generator:
    def __init__(self) -> None:
        super().__init__()
        self._index = 0
        self.export_results = ""
        self._image: Image = None
        self._number_of_tests = 0
        self.__load_settings()

    def generate(self):
        """
        Generate the number of pictures specified in the settings.json
        """
        print(f"Generating {self._number_of_tests * (9 if self._mode == 'Digits-Only' else 1)} ({self._mode}) pictures")
        if self._mode == "Easy":
            for i in range(self._number_of_tests):
                self.__progressBar()
                self.__generateEasy()
        elif self._mode == "Medium":
            for i in range(self._number_of_tests):
                self.__progressBar()
                self.__generateMedium()
        elif self._mode == "Hard":
            for i in range(self._number_of_tests):
                self.__progressBar()
                self.__generateHard()
        elif self._mode == "Digits-Only":
            for i in range(self._number_of_tests):
                self.__progressBar()
                self.__generate_digits()

        print(f"Exported {self._number_of_tests} pictures in the export folder")

    def __progressBar(self, bar_len=50, title='Please wait'):
        """
        Update ProgressBar in the Console
        """
        percent_done = round((self._index + 1) / self._number_of_tests * 100, 1)

        done = round(percent_done / (100 / bar_len))
        togo = bar_len - done

        done_str = '█' * int(done)
        togo_str = '░' * int(togo)

        print(f'\t⏳\t{title}: [{done_str}{togo_str}] {percent_done}% done (n°{self._index})', end='\r')
        if round(percent_done) == 100:
            print('\t✅')

    def save_results(self):
        """
        Save File in ./export/sudoku_answers.txt
        """
        if self._mode != "Digits-Only":
            open(f"./export/{self._mode}/sudoku_answers.txt", "w").write(self.export_results)

    def __load_settings(self):
        """
        Load all the settings specified in settings.json
        """
        with open('settings.json', 'r') as outfile:
            var = json.load(outfile)
        if var["version"] != "1.0.0":
            raise Exception("File version is not corresponding. Check "
                            "https://github.com/opticalloop/SudokuPictureGenerator/blob/main/settings.json for any update.")
        if not var["GoogleFontAPI_key"]:
            raise Exception("GoogleFontAPI_key cannot be empty")
        self._fonts = Fonts(var["GoogleFontAPI_key"])

        var = var["settings"]

        self._image = Image.open(var["base_image"])
        self._index = var["start_index"]
        self._number_of_tests = var["nb_exports"]
        if self._number_of_tests < 0:
            self._number_of_tests = len(self._fonts.fonts)
        if var["difficulty_mode"] not in ("Easy", "Medium", "Hard", "Digits-Only"):
            raise Exception("Difficulty mode is not valid. Should be Easy | Medium | Hard | Digits-Only")
        self._mode = var["difficulty_mode"]

        try:
            os.mkdir("./export/" + self._mode)
        except FileExistsError:
            pass

        if var["rotate"]["auto_rotate"]:
            Rotate.auto_rotate = True
            if var["rotate"]["minRotate"] == var["rotate"]["maxRotate"]:
                raise Exception("minRotate and maxRotate are equal")
            Rotate.min = var["rotate"]["minRotate"]
            Rotate.max = var["rotate"]["maxRotate"]
        if var["noise"]:
            print("Noise is not available right now.")

    def __generateEasy(self):
        sudoku = Sudoku(self._image.copy(), self._fonts.get_random_font(), "Easy")
        sudoku.place_cases(random.randint(4, 30))
        sudoku.rotate_img()
        sudoku.save(self._index)
        self.export_results += sudoku.export_string(self._index)
        self._index += 1

    def __generateMedium(self):
        sudoku = Sudoku(self._image.copy(), self._fonts.get_random_font(), "Medium")
        sudoku.place_cases(random.randint(4, 30))
        sudoku.rotate_img()
        sudoku.transform_img()
        sudoku.save(self._index)
        self.export_results += sudoku.export_string(self._index)
        self._index += 1

    def __generateHard(self):
        sudoku = Sudoku(self._image.copy(), self._fonts.get_random_font(), "Hard")
        sudoku.place_cases(random.randint(4, 30))
        sudoku.rotate_img()
        sudoku.transform_img()
        sudoku.save(self._index)
        self.export_results += sudoku.export_string(self._index)
        self._index += 1

    def __generate_digits(self):
        font = self._fonts.fonts[self._index]

        font.download()
        fontType = ImageFont.truetype(f'export/fonts/{font.name}.ttf', 20)

        for i in range(1, 10):
            digit = Digit(i, fontType)
            digit.place_case()
            digit.save(self._index)
        self._index += 1
