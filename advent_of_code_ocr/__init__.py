"""Convert Advent of Code ASCII art"""

import numpy as np

from .characters import ALPHABET_6

__version__ = "0.2.0"


def convert_6(input_text: str, *, fill_pixel: str = "#", empty_pixel: str = "."):
    input_text = input_text.replace(fill_pixel, "1").replace(empty_pixel, "0")

    array = np.array([[char == fill_pixel for char in row]
                     for row in input_text.split("\n")], dtype=bool)

    return convert_6_np(array)


def convert_6_np(array):
    rows, cols = array.shape
    if cols % 5 == 0:
        array = array[:,:-1]

    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    result = ""

    for character in range(cols//5):
        string = "\n".join(
            "".join("#" if e else "." for e in r)
            for r in array[:, 5*character:5*(character+1)-1])

        letter = ALPHABET_6[string]
        result += letter

    return result
