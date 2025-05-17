
def main():
    numbers = [1203, 1256, 312456, 98] # Should numbers be given by input? the assignment is not clear

    number_counting(numbers)

def number_counting(numbers):
    while True:
        try:
            numbers = [int(num) for num in numbers]
        except ValueError:
            numbers = input("Please enter a list of integers, separated by a space: ").split()
        else:
            break

    string = ''
    for num in numbers:
        string = string + str(num)

    for i in range(10):
        count = string.count(str(i))
        print(i, count)

if __name__ == '__main__':
    main()