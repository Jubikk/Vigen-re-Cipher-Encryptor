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

def encrypt_and_display():
    #Input
    plaintext = plaintext_entry.get()
    keyword = keyword_entry.get()

    # Encrypt the plaintext
    ciphertext = encrypt_vigenere(plaintext, keyword)

    # Display the result
    ciphertext_label.config(text="Your Ciphertext is: " + ciphertext)
    

#Tkinter
root = tk.Tk()
root.title("Vigenere Cipher by Gusi")
root.geometry("400x150")

#Url/Image
url = "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80"
response = requests.get(url)
img_data = response.content
img = Image.open(io.BytesIO(img_data))
tk_image = ImageTk.PhotoImage(img)

background_label = tk.Label(root, image=tk_image)
background_label.place(x=0, y=0, relwidth=1,relheight=1)

plaintext_label = tk.Label(root, text="Enter your plaintext:")
plaintext_entry = tk.Entry(root, width= 50)
keyword_label = tk.Label(root,width=20, text="Enter your keyword:")
keyword_entry = tk.Entry(root)
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_and_display)


ciphertext_label = tk.Label(root, text="")
ciphertext_label['bg'] = 'orange'

plaintext_label.pack()
plaintext_entry.pack()
keyword_label.pack()
keyword_entry.pack()
encrypt_button.pack()
ciphertext_label.pack()

root.resizable(width=True, height=True)

root.mainloop()

