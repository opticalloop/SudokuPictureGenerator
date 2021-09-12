import os
import shutil
from src.Generator import Generator


def create_directories():
    try:
        os.mkdir("./export")
    except FileExistsError:
        pass
    try:
        os.mkdir("./export/fonts")
    except FileExistsError:
        pass


if __name__ == "__main__":
    create_directories()

    generator = Generator()
    generator.generate()
    generator.save_results()

    shutil.rmtree("export/fonts") # remove tmp fonts

