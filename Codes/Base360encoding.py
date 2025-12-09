import math
import pyperclip
base20 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

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

encoded = encode(123)
#print(encoded)
#print(decode("ba"))
for x in range(1,361):
    print(encode(x))
    print(decode(encode(x)))
pyperclip.copy(", ".join(base20))



