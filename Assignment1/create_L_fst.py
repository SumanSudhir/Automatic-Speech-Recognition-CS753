'''
The function of this code is to crete L.fst text file. While creating L.fst
it also create some temprory file in order to convert fst to binary
'''

import argparse

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--lexfile", type=str)
args = ap.parse_args()

lex_txt = open(args.lexfile, "r")
l_fst = open('L.fst', 'w')
input_txt = open("input.txt", 'w')
output_txt = open('output.txt', 'w')


phones = []
n_state = 1
input_txt.write('<eps>' + ' 0' + '\n')
output_txt.write('<eps>' + ' 0' + '\n')

for i, words in enumerate(lex_txt):
    input_txt.write(words.split()[0] + " " + str(i + 1) + '\n')
    phones.extend(words.split()[1:])

    l_fst.write(str(0) + " " + str(n_state) + " " +
                words.split()[0] + ' ' + words.split()[1] + '\n')

    for current_phone in words.split()[2:]:
        #print(current_phone + '\n')
        l_fst.write(str(n_state) + ' ' + str(n_state + 1) +
                    " " + '<eps>' + " " + current_phone + '\n')

        n_state = n_state + 1

    l_fst.write(str(n_state) + '\n')
    n_state = n_state + 1

phones = np.unique(phones)

l_fst.write(str(0) + " " + str(n_state) + " " +
            '<eps>' + " " + '<OOV>' + '\n')
l_fst.write(str(n_state) + '\n')

output_txt.write('<OOV>' + ' ' + str(1) + "\n")
for i, c_phones in enumerate(phones):
    output_txt.write(c_phones + " " + str(i + 2) + '\n')
