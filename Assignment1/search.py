'''
The function of this code is to search for given word when it is searched in FST

'''

import argparse

ap = argparse.ArgumentParser()
#ap.add_argument("--l_fst", type=str)
ap.add_argument("--words", type=str)

args = ap.parse_args()

input_txt = open("input.txt", 'r')
word_fst = open('word.fst', 'w')

word_fst.write(str(0) + " " + str(1) + " " +
               args.words + " " + args.words + '\n')
word_fst.write(str(1) + '\n')

# l_dot_fst = open(args.l_fst, "r")
# lines = l_dot_fst.readlines()
# # print(lines[2][2])
# # print(l_dot_fst[0])
# # print(l_dot_fst[0])
#
# for i, words in enumerate(lines):
#     # print(words.split()[3])
#     if int(words.split()[0]) == 0 and words.split()[2] == args.words:
#         phones = words.split()[3]
#         print(phones)
#
#         while(len(lines[i + 1].split()) > 1):
#             # print("True")
#             phones = phones + " " + (lines[i + 1].split())[3]
#             i = i + 1
#         #phones.append(lines[i + 1][3])
#         # print("Hey")
# print(phones)


# l_dot_fst = open(args.l_fst, "r")
