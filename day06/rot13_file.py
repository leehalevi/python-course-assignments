# Create a script called rot13_file.py that given a file on the command line it will replace the content with the rot13 of it of it.
import sys

def rot13_letter(letter):
    if letter.isalpha():
        if letter.islower():
            return chr((ord(letter) - ord("a") + 13) % 26 + ord("a"))
        else:
            return chr((ord(letter) - ord("A") + 13) % 26 + ord("A"))
    else:
        return letter

def rot13(file_content):
    rot13_str = ''
    for letter in file_content:
        rot13_str += rot13_letter(letter)
    return rot13_str

def main():
    file_name = "rot13_file"
    # Open file and read
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    print(rot13(content))

if __name__ == '__main__':
    main()