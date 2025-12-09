import pyperclip
base20 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

def encode(num):
    char1 = base20[int(num%20)]
    char2 = base20[int((num/20)%20)]
    return f"{char1}{char2}"

for x in range (1,361):
    print(f"{x} {encode(x)}")

pyperclip.copy(", ".join(base20))


