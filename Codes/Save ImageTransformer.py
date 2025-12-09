from PIL import Image
import keyboard
import pyperclip
import math

image_path = "Images\Cookie.png"  # Replace with the actual image path
start_img = Image.open(image_path)
img = start_img.resize((400, 400), Image.LANCZOS)
width, height = img.size
list_length = 2200

rgb = []
base20 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '/', ';', '[']
alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', ')', '!', '@', '#', '$', '%', '^', '&', '*', '()', '<', '>', '?', ':', '{']
alphabet3 = alphabet + alphabet2
print(len(alphabet))
rgb_segments = {}
current_copy = 0

def encode(num):
    char1 = base20[int(num%20)]
    char2 = base20[int((num/20)%20)]
    return f"{char1}{char2}"

try:
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r2 = encode(r)
            g2 = encode(g)
            b2 = encode(b)
            rgb.append(f"{r2};{g2};{b2}")
    print("Color Type: RGB")
            # Process the RGB values (e.g., store them, analyze frequency)
except ValueError:
    for y in range(height):
        for x in range(width):
            h, s, v, o = img.getpixel((x, y))
            h2 = encode(h)
            s2 = encode(s)
            v2 = encode(v)
            rgb.append(f"{h2};{s2};{v2}")
    print("Color Type: HSV")

req = math.ceil(len(rgb)/list_length)


print(f"Total Pastes: {req}")

print(f"Total Pixels: {len(rgb)}")
for m in range(0,req):
    key = f'rgb{m+1}'  # Create the key 'rgb1', 'rgb2', etc.
    start_index = m * list_length
    end_index = (m + 1) * list_length
    rgb_segments[key] = rgb[start_index:end_index]
    print(f"{m} {alphabet3[m]} {len(rgb_segments[key])}")
    
print("esc to stop")

lowreq = req - 1
with open("Output.txt", "w") as f:
    for m in range(0,req):
        key = f'rgb{m+1}'
        if not m == lowreq:
            print(",".join(rgb_segments[key]), file=f)
        else:
            print_amount = len(rgb_segments[key])//2
            print(",".join(rgb_segments[key]), file=f)
    f.close()
    
# Register a callback for a key press event
def on_key_press(event):
    for m in range(0,req): 
        key = f'rgb{m+1}'
        letter = alphabet3[m]
        if keyboard.is_pressed(f'{letter}'):
            pyperclip.copy(", ".join(rgb_segments[key]))
            print(f"success {letter}")
            


keyboard.on_press(on_key_press)

# Keep the script running to listen for events
keyboard.wait('esc')