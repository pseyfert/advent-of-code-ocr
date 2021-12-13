"""Convert Advent of Code ASCII art"""

import numpy as np

from .characters import ALPHABET_6

__version__ = "0.2.0"


def convert_6(input_text: str, *, fill_pixel: str = "#", empty_pixel: str = "."):
    array = np.array([[char == fill_pixel for char in row]
                     for row in input_text.split("\n")], dtype=bool)

    return convert_6_np(array)


def convert_6_np(array):
    rows, cols = array.shape
    if (trunk := cols % 5) < 4:
        array = array[:, :-(1+trunk)]
    rows, cols = array.shape

    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    result = ""

    for character in range(1 + cols//5):
        tmp = array[:, 5*character:5*(character+1)-1]
        if tmp.shape !=(6,4):
            continue
        string = "\n".join( "".join("#" if e else "." for e in r) for r in tmp)

        letter = ALPHABET_6[string]
        result += letter

    return result
