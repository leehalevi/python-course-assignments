
def main():
    celestial_objects = [
        'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
    ]
    lst = celestial_objects.copy()
    count_words_in_lists(lst)

def count_words_in_lists(lst):
    word_count = {}

    for word in lst:
        try:
            word = str(word)
        except ValueError:
            print(f"{word} is not a string")
        else:
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1

    for word in word_count.keys():
        print(word, word_count[word])

if __name__ == '__main__':
    main()