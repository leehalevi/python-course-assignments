import sys

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    word_list = content.split()
    return word_list

def print_menu(word_list):
    i = 1
    for color in word_list:
        print(f"{i}. {color}")
        i += 1

def main():
    try:
        # bring a list of colors from a file
        file_name = 'color_list'
        word_list = read_file(file_name)
        print_menu(word_list)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return

    # choose a color
    color = input("Please pick a color from the list above by typing it's number: ")
    try:
        if int(color) > len(word_list) or int(color) <= 0:
            print("Your number is not on the list")
        else:
            print(f"Your color is: {word_list[int(color) - 1]}")

    except ValueError:
        print("Please enter a valid number")

if __name__ == '__main__':
    main()