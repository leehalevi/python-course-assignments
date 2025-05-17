import sys

def sequence_seperating(sequence):
    final_list = []
    i = 0

    for idx in range(len(sequence)):
        nucleotide = sequence[i]

        if nucleotide not in "ACGT":
            string = sequence[:i]
            sequence = sequence[i + 1:]  # Remove the invalid nucleotide
            final_list.append(string)
            i = -1

        i += 1

    final_list.append(sequence)
    final_list.sort(key=len, reverse = True)
    final_list = [s for s in final_list if s]

    return final_list


def main():
    sequence = sys.argv[1]

    print(sequence_seperating(sequence))

if __name__ == '__main__':
    main()