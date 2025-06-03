# os.path.exsits
# os.path.isfile


import sys
import os

# This function takes a letter and returns its ROT13 equivalent
def rot13_1(letter):
    if letter.isalpha():
        if letter.islower():
            return chr((ord(letter) - ord("a") + 13) % 26 + ord("a"))
        else:
            return chr((ord(letter) - ord("A") + 13) % 26 + ord("A"))
    else:
        return letter

# This function is a more verbose version of the above function
def rot13_2(letter):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if letter.isalpha():
        if letter.islower():
            index = lowercase.find(letter)
            return lowercase[index + 13 if index < 13 else index - 13]
        else:
            index = uppercase.find(letter)
            return uppercase[index + 13 if index < 13 else index - 13]
    else:
        return letter

def rot13_string():
    rot13_str = ''
    for letter in sys.argv[1]:
        rot13_str += rot13_1(letter)
    return rot13_str

def printing():
    txt = "hello world!"
    for ch in txt:
        if ch == " ":
            #continue
            #break
            #pass
            try:
                raise ValueError()
            except ValueError as e:
                print(f"Caught error: {e}")
        print(ch)
    print('done')

"""def process_file(input_filename, output_filename=None):
    try:
        if not os.path.exists(input_filename):
            print(f"Error: {input_filename} does not exist")
            
            with open(input_filename, 'r', encoding='utf-8') as infile:
                content = infile.read()"""

def main():
    printing()

if __name__ == "__main__":
    main()