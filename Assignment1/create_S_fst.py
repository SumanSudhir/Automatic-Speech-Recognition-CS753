'''
The function of this code is to crete S.fst text file. While creating S.fst
it also create some temprory file in order to convert fst to binary
'''

import argparse

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--lexfile", type=str)
args = ap.parse_args()

lex_txt = open(args.lexfile, "r")
s_fst = open("S.fst", 'w')
input_alpha = open("input_alpha.txt", 'w')
output_alpha = open("output_alpha.txt", 'w')

alphabet_used = []
a_state = 1

input_alpha.write('<eps>' + ' 0' + '\n')
output_alpha.write('<eps>' + ' 0' + '\n')

for i, words in enumerate(lex_txt):
    # Creating S.fst
    input_alpha.write(words.split()[0] + " " + str(i + 1) + '\n')
    alphabet = list(words.split()[0])
    s_fst.write(str(0) + " " + str(a_state) + " " +
                words.split()[0] + " " + alphabet[0] + '\n')

    for current_alphabet in alphabet[1:]:
        s_fst.write(str(a_state) + " " + str(a_state + 1) +
                    " " + '<eps>' + " " + current_alphabet + '\n')
        a_state = a_state + 1

    alphabet_used.extend(alphabet)
    # print(alphabet_used)
    s_fst.write(str(a_state) + '\n')
    a_state = a_state + 1

alphabet_used = np.unique(alphabet_used)

s_fst.write(str(a_state) + '\n')

for i, c_alpha in enumerate(alphabet_used):
    output_alpha.write(c_alpha + " " + str(i + 2) + '\n')
