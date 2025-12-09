from PIL import Image
import keyboard
import pyperclip
import math
import tkinter as tk

image_path = "Images\Mushroom.png"  # Replace with the actual image path
start_img = Image.open(image_path)
img = start_img.resize((480, 480), Image.LANCZOS)
width, height = img.size
list_length = 2200
new_copy = 0

rgb = []
base20 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '/', ';', '[']
alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', ')', '!', '@', '#', '$', '%', '^', '&', '*', '()', '<', '>', '?', ':', '{']
alphabet3 = alphabet + alphabet2
rgb_segments = {}
current_copy = 0


def encode(num):
    char1 = base20[int(num%20)]
    char2 = base20[int((num/20)%20)]
    return f"{char1}{char2}"

def decode(code):
    first = code[0:1]
    second = code[1:2]
    index1 = base20.index(first)
    index2 = base20.index(second)
    num1 = index1 * 1 #index1 * 20^0
    num2 = index2 * 20 #index2 * 20^1
    #we only use two because thats the maximum length we will have, 
    #normally you would interate through each letter
    end = num1 + num2
    return end

r, g, b, a = img.getpixel((0, 0))
r2,g2,b2 = encode(r),encode(g),encode(b)
r3,g3,b3 = decode(r2),decode(g2),decode(b2)
print(r,g,b)
print(r2,g2,b2)
print(r3,g3,b3)
print('qg;og;tf')
