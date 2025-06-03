import sys

def count_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    word_list = content.split()

    word_count = {}

    for word in word_list:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def main():
    file_name = sys.argv[1]
    word_count = count_words(file_name)

    for word, count in word_count.items():
        print(f"{word} -> {count}")

if __name__ == '__main__':
    main()