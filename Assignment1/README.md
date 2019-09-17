How to run Question 3.1
First Create L.fst by running the command
'''
$ chmod +x create-dict.sh
$ ./create-dict.sh lex.txt > L.fst
'''
Now check the phones of any word given in lex.txt by running command

'''
$ ./lookup.sh L.fst ALICE
'''
NOTE:- Replace word ALICE by word you want to search,the answer will be appended in file ANSWER and will also be printed in terminal


How to run question 3.2

Run the command
$ chmod +x create-let-dict.sh
$ ./create-let-dict.sh lex.txt L.fst > Q.fst

File named Q.fst will be created in working directory which maps words to its spelling
