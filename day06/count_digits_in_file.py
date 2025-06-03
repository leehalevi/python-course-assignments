#Given the file examples/files/numbers.txt (or a similar file),
# create a file called count_digits_in_file.py that will count how many times each digit appears?
# The output will look like this. Just different values.
# Save the results in a file called report.txt.

import sys

def number_counting(numbers):
    while True:
        try:
            numbers = [int(num) for num in numbers]
        except ValueError:
            numbers = input("Please enter a file name that contains only numbers, separated by a space\enter: ").split()
        else:
            break

    string = ''
    for num in numbers:
        string = string + str(num)

    results = []
    for i in range(10):
        count = string.count(str(i))
        results.append([i, count])

    return results

def save_file(numbers):
    file_name = 'report.txt'
    number_list = number_counting(numbers)
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in number_list:
            content = f"{i[0]} {i[1]}\n"
            file.write(content)



def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        content = f.read()
    numbers = [int(num) for num in content.split()]

    save_file(numbers)

    print(number_counting(numbers))

if __name__ == "__main__":
    main()