'''Project To Convert String To Morse Code'''
from morsecode import MORSE_CODE_DICT

def encrypt(string):
    output_string = ''
    for char in string:
        if char != ' ':
            output_string = output_string + MORSE_CODE_DICT[char] + " "
        else:
            output_string = output_string + char
    return output_string

def decrypt(string):
    output_string = ''
    key = ''
    prev = ''
    for char in string:
        if char == ' ':
            if key != '':
                value = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(key)]
                output_string += value
            if prev == ' ' and char == ' ':
                output_string += ' '
                key =''
            else:
                key = ''
            prev = char
        else:
            key += char
            prev = char
    return output_string


input_string = input("Enter The String Which You Want To Convert Into Morse Code :  ").upper()
masked_string = encrypt(input_string)
print(masked_string)
unmasked_string = decrypt(masked_string)
print(unmasked_string.title())


