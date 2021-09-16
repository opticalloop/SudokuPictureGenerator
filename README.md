# SudokuPictureGenerator
## Generate procedural pictures for OCR Neural Network
![sudoku_4](https://user-images.githubusercontent.com/14821642/132985699-b047670d-e450-4314-961e-2464aa77499c.gif)

### Warning : Exported Sudoku might not be resolvable
## Installation

Install all the dependencies using `requirements.txt`
```bash
 pip freeze > requirements.txt
```

You'll need to get you own Google Font API Key. 
[Check this link](https://developers.google.com/fonts/docs/developer_api) 
for more information.

## How it works
SudokuPictureGenerator use random fonts from Google Fonts API (near 4000 fonts are available) 
to generate random patterns of sudoku grid.


Run 
```bash
 $  ./main.py
```

Exported pictures will be saved into the `./export/{Easy|Medium|Hard|Digits-Only}` folder with a file `sudoku.answers.txt` containing all the values 
and theirs positions of all pictures.
File format :

```text
format: indexOfthePicture (xPos,yPos,value)(xPos,yPos,value)(xPos,yPos,value)(xPos,yPos,value)
ex :    6 (5,7,5)(6,2,2)(8,1,2)(8,0,4)
```
See [Case positions](##Cases-positions) section for more detail.

## Change settings
Edit [settings.json](/settings.json) to change program settings :

```js
    {
      "version": "1.0.0", //dont change
      "GoogleFontAPI_key": "yourAPIKey" // change this value by your own Google Font API Key
      "settings": {
        "base_image": "./sudokuGrid.jpg", // sudoku grid base path
        "nb_exports": 10, // number of sudoku you want
        "start_index": 0, // index for filename
        "difficulty_mode": "Easy", // difficulty mode
        "rotate": {
          "auto_rotate": true, // set to false if you don't want to get a rotated picture
          "minRotate": -30, 
          "maxRotate": 30
        },
        "noise": false // add random noise to picture (does not work in 1.0.0)
      }
    }
```
## Difficulty modes
### Mode Easy
>*  Rotation on pictures

### Mode Medium
>*  Including Mode Easy parameters
>
>* Transform picture perspectives

### Mode Hard
>*  Including Mode Medium parameters
> 
>* ####  Will include noise and others picture degradation

### Digits-Only
>* Only generate 28x28 jpg image containg one digit (from 1 to 9)
## Case positions
>### Here the position XY of all cases:
>![image](https://user-images.githubusercontent.com/14821642/132983889-ca2988d0-0b6d-4dec-ad21-368690ce9ae0.png)


## Licensing
MIT License

Copyright 2021 opticalloop/EPITA

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.