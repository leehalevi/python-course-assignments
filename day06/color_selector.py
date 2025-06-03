import sys

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print('hi')

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
        file_name = sys.argv[1]
        word_list = read_file(file_name)
        print_menu(word_list)
    except IndexError:
        print("Error: Please provide a file name as a command-line argument.")
        return
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return

    # print a menu
    word_list = read_file(file_name)
    print_menu(word_list)

    # choose a color
    color = input("Please pick a color from the list above: ")
    if color not in word_list:
        print("The color you picked is not on the list.")


if __name__ == '__main__':
    main()