#Joebeck Adndrew F. Gusi | BSCPE 1-5 | Assignment No.3 |

import tkinter as tk
import time
from PIL import Image, ImageTk
import requests
import io
from io import BytesIO

# First we define vigenere_table
def vigenere_table():
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append((i+j)%26)
        table.append(row)
    return table
