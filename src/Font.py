import requests
import random


class Font:
    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link

    def download(self):
        r = requests.get(self.link)
        if not r.ok:
            Exception("Cannot download {self.name} TTF Font.")
        open(f"./export/fonts/{self.name}.ttf", "wb").write(r.content)


class Fonts:
    def __init__(self, keyAPI) -> None:
        print("Establish connection to Google Fonts API.")
        r = requests.get("https://www.googleapis.com/webfonts/v1/webfonts?key=" + keyAPI)

        if not r.ok:
            raise Exception("Cannot establish connection to Google Fonts API. Check your internet connection or the validity of your API Key.")

        self._fonts = list()
        for item in r.json()["items"]:
            for font_name, font_link in item["files"].items():
                self._fonts.append(Font(item["family"] + font_name, font_link))
        print(f"Imported {len(self._fonts)} fonts.")

    def get_random_font(self) -> Font:
        return random.choice(self._fonts)
