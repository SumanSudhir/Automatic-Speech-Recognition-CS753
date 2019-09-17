'''
The function of this code is to print the searched string in terminal and
also append in ANSWER file
'''


final_fst = open("final.fst", "r")
lines = final_fst.readlines()
# print(lines[2][2])
# print(l_dot_fst[0])
# print(l_dot_fst[0])
# print(words.split()[3])
i = 0
phones = lines[i].split()[3]
while(len(lines[i + 1].split()) > 1):
    # print("True")
    phones = phones + " " + (lines[i + 1].split())[3]
    i = i + 1
#phones.append(lines[i + 1][3])
# print("Hey")

answer = open('ANSWERS', 'a')
answer.write(phones + '\n')
print(phones)
