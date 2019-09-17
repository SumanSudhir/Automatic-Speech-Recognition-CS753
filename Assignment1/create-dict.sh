python3 create_L_fst.py --lexfile $1

fstcompile --isymbols=input.txt --osymbols=output.txt --keep_isymbols --keep_osymbols L.fst $3
