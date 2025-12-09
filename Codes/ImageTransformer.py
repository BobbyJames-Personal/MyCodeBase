from PIL import Image
import keyboard
import pyperclip
import math
import tkinter as tk
import os

"""
Gets all images/folders, formats them into three lists
only_files_paths are what is behind the scenes, the full path needed
only_files_names are what the user sees, just the names
only_folders are all the folders take from
"""
only_files_paths = []
only_files_names = []
only_folders = []
image_folder = "Images"
with os.scandir(image_folder) as entries:
    only_folders = [entry.path for entry in entries if entry.is_dir()]

for folder in only_folders:
    with os.scandir(folder) as entries:
        for image in entries:
            if image.is_file:
                only_files_paths.append(image.path)
                only_files_names.append(image.name)

with os.scandir(image_folder) as entries:
    for image in entries:
        if image.is_file:
            only_files_paths.append(image.path)
            only_files_names.append(image.name)

imageTOT = len(only_files_paths)
image_num = -1
for i in range (0, len(only_files_paths)-1):
    print(f"{i+1} {only_files_names[i]}")


#Choose Image
while image_num > imageTOT or image_num < 0:
    try:
        image_num = int(input(f"Choose you image with a number 1-{imageTOT-1}: "))
        if image_num > imageTOT or image_num < 1:
            image_num = int(input(f"You can only write a number 1-{imageTOT-1}: "))
    except ValueError:
        print(f"You may only write a number 1-{imageTOT-1}")
        quit()   
image_num -= 1
print()

image_path = only_files_paths[image_num]
print(f"You chose: {only_files_names[image_num]}")
print("")


#Resize Image
start_img = Image.open(image_path)
start_height, start_width = start_img.size
done = "N"
resize_option = ""
resize_ratio = -1
min_resize = 134/min(start_width, start_height)
while done != "Y":
    while resize_ratio < 0:
        while resize_option != "S" and resize_option != "R":
            try:
                resize_option = (input("Choose either to set the size,\nor ratio of the print, S or R\n"))
            except ValueError:
                print("Please choose either 'S' or 'R'")
        if resize_option == "R":
            try:
                done = "N"
                resize_ratio = float(input(f"Choose a resize ratio for the image.\nOriginal width/height: {start_width}/{start_height}\nDont write fractions, only decimals\nMinimum: ~{(math.ceil(min_resize*10000)/10000)}\n"))
                print("")
                img_new_width, img_new_height = int(round(start_width*resize_ratio)), int(round(start_height*resize_ratio))
                if resize_ratio < min_resize:
                    print("Sorry thats too small\n")
                    done = "fail"
                if done != "fail":
                    done = input(f"With a resize ratio of {resize_ratio},\nyou will have an image size of {img_new_width}/{img_new_height},\nor {img_new_width*img_new_height} pixels\nare you happy with this Y/N?\n")   
                if done != "Y":
                    resize_ratio = -1
            except ValueError: 
                print("You can only input numbers\n")
        try:
            done = "N"
            resize_size = int(input(f"Choose a size for the image.\nOriginal width/height: {start_width}/{start_height}\nOnly write integers,\nMinimum: 134/134\n"))
            resize_ratio = resize_size/start_width
            print("")
            img_new_width, img_new_height = int(round(resize_size)), int(round(start_height*resize_ratio))
            if resize_ratio < min_resize:
                print("Sorry thats too small\n")
                done = "fail"
            if done != "fail":
                done = input(f"With a resize ratio of ~{round(resize_ratio, 3)},\nyou will have an image size of {img_new_width}/{img_new_height},\nor {img_new_width*img_new_height} pixels\nare you happy with this Y/N?\n")   
            if done != "Y":
                resize_ratio = -1
        except ValueError: 
            print("You can only input numbers\n")


print("")


img = start_img.resize((img_new_width, img_new_height), Image.LANCZOS)
width, height = img.size
list_length = 3100
new_copy = 0

rgb = []
base20 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '/', ';', '[']
alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', ')', '!', '@', '#', '$', '%', '^', '&', '*', '()', '<', '>', '?', ':', '{']
alphabet3 = alphabet + alphabet2
rgb_segments = {}
current_copy = 0



def encode(num):
    char1 = base20[int(num%20)]
    char2 = base20[int((num/20)%20)]
    return f"{char1}{char2}"


#Adds one to the counter
def increment_counter():
    global new_copy
    global lowreq
    if not new_copy+1 > lowreq:
        new_copy = new_copy + 1
        key = f'rgb{new_copy+1}'
        pyperclip.copy("".join(rgb_segments[key]))
        print(f"Now pasting # {new_copy + 1}/{req}")
    update_overlay()


#Subtracts one from the counter
def decrement_counter():
    global new_copy
    if not new_copy-1 <0:
        new_copy = new_copy - 1
        key = f'rgb{new_copy+1}'
        pyperclip.copy("".join(rgb_segments[key]))
        print(f"Now pasting # {new_copy + 1}/{req}")
    update_overlay()


#creates the overlay, positions and styles it
def create_overlay():
    # Make the window undecorated (no title bar, borders)
    root.overrideredirect(True)

    # Set the window to always be on top
    root.attributes('-topmost', True)

    # Set the background as a transparent key color (e.g., magenta)
    root.config(bg='Magenta')
    root.wm_attributes('-transparentcolor', 'magenta')

    # Create and position the label
    global counter_label
    counter_label = tk.Label(root, text=f"Copy: {new_copy+1} Total: {req}", font=('Helvetica', 24), bg='Black', fg='white')
    counter_label.pack(padx=10, pady=10)

    # Set the initial position of the window
    root.geometry('+10+10')  # Position at top-left corner

#Sets the text of the overlay
def update_overlay():
    counter_label.config(text=f"Copy: {new_copy+1} Total: {req}")

print("Please wait for everything to load before pressing anything")
print("")
#Gets the image data, encodes it, and adds it to the rgb list
#this sorts data into rgb or hsv based on the returned values (hsv returns 4)
try:
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r2 = encode(r)
            g2 = encode(g)
            b2 = encode(b)
            rgb.append(f"{r2}{g2}{b2}")
    print("Color Type: RGB")
except ValueError:
    for y in range(height):
        for x in range(width):
            h, s, v, o = img.getpixel((x, y))
            h2 = encode(h)
            s2 = encode(s)
            v2 = encode(v)
            rgb.append(f"{h2}{s2}{v2}")
    print("Color Type: HSV")


#gets how many lists we will need, pastes the amount of lists and pixels
req = math.ceil(len(rgb)/list_length)
lowreq = req - 1
print(f"Original Size(w/h): {start_width}, {start_height}")
print(f"Print Size: {img_new_width}, {img_new_height}")
print(f"Total Pastes: {req}")
print(f"Total Pixels: {len(rgb)}")
print("")




#Creates each list (rgb1,rgb2,rgb3)
for m in range(0,req):
    key = f'rgb{m+1}'
    start_index = m * list_length
    end_index = (m + 1) * list_length
    rgb_segments[key] = rgb[start_index:end_index]    

#Write each list to Output.txt
with open("Output.txt", "w") as f:
    for m in range(0,req):
        key = f'rgb{m+1}'
        print("".join(rgb_segments[key]), file=f)
    f.close()

#Sets the keybinds up and down arrows to their respective functions
keyboard.on_press_key("up", lambda _: increment_counter())
keyboard.on_press_key("down", lambda _: decrement_counter())


#Main loop
if __name__ == "__main__":
    root = tk.Tk()
    create_overlay()
    
    print("Press UP and DOWN to change the counter. Press ESC in the console to exit.")
    
    pyperclip.copy("".join(rgb_segments['rgb1']))
    print(f"Now pasting # 1/{req}")

    def check_esc_key():
        if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
            print("Exiting")
            root.destroy()
        else:
            root.after(100, check_esc_key)

    check_esc_key()

    root.mainloop()