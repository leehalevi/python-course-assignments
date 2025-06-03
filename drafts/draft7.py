# Try pair-programming?

# we will be skipping dictionaries

# YAML format
# Usually used to configure things.

import yaml

filename = "data.yaml"

with open(filename) as fh:
    data = yaml.load(fh, Loader=yaml.Loader) # A better way to open than without the "Loader" statment

import json
filename2 = "data.json"
with open(filename2) as fh:
    ...

# Ask keren about how much time rotations took her, and when did she start the rotations.

import requests, json


city_name = input("Enter city name: ")
complete_url = base_url + "appid"
response = requests.get(complete_url)
x = response.json()


{"fname": "Foo", "lname": "Bar", "email": "<EMAIL>"}

# The way to use json is to allow us to communicate easily between programs.
# How do I square the square that needs the squaring? what do I do here? How do I do here?
# writing is do much more fun like that. I an ok ar whar i do. I rhinks? srill need some improvments though. an I ewallt dont listan ro hi,. which is and issue.
# Marshalilng - transformin the memort representation of

# Fasta - format to store a sequence, with metadata about it. also FASTQ, EMBL, etc.
# There is a library - biopython (or bio), import Seq, and you can use it

from Bio.seq import Seq

my_dna = Seq("ATGCGTCGTC")
print(my_dna)
print(my_dna.translate())
print(my_dna.complement())