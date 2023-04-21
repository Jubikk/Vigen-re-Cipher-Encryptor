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

def encrypt_vigenere(plaintext, keyword):
    table = vigenere_table()

    # To convert plaintext and keyword to uppercase and remove spaces
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()

    #To match the len of the plaintext
    keyword = keyword * (len(plaintext) // len(keyword) + 1)
    keyword = keyword[:len(plaintext)]

    ciphertext = ""
    for i in range(len(plaintext)):
        row = ord(plaintext[i]) - ord("A")
        col = ord(keyword[i]) - ord("A")
        ciphertext += chr(table[row][col] + ord("A"))

    return ciphertext
