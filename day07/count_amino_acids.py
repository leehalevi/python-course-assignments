import sys

def split_to_codons(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.splitlines()
    joined_string = "".join(lines)
    codon_list = [joined_string[i:i+3] for i in range(0, len(joined_string), 3)]

    return codon_list

def translation(codon_list):
    codon_table = {
        'Phe': ['TTT', 'TTC'],
        'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'Ile': ['ATT', 'ATC', 'ATA'],
        'Met': ['ATG'],
        'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
        'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
        'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
        'Tyr': ['TAT', 'TAC'],
        'His': ['CAT', 'CAC'],
        'Gln': ['CAA', 'CAG'],
        'Asn': ['AAT', 'AAC'],
        'Lys': ['AAA', 'AAG'],
        'Asp': ['GAT', 'GAC'],
        'Glu': ['GAA', 'GAG'],
        'Cys': ['TGT', 'TGC'],
        'Trp': ['TGG'],
        'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
        'STOP': ['TAA', 'TAG', 'TGA']
    }

    codon_to_aa = {}
    for aa, codons in codon_table.items():
        for codon in codons:
            codon_to_aa[codon] = aa

    protein = []
    for codon in codon_list:
        amino_acid = codon_to_aa.get(codon, None)
        if amino_acid:
            protein.append(amino_acid)
        else:
            protein.append('Unknown')

    return protein

def main():
    # take a file and read it
    file_name = sys.argv[1]
    # split every 3 letters
    codon_list = split_to_codons(file_name)
    # translate to amino acids
    protein = translation(codon_list)
    # return it
    print(protein)


if __name__ == '__main__':
    main()