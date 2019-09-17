python3 create_S_fst.py --lexfile $1

fstcompile --isymbols=input_alpha.txt --osymbols=output_alpha.txt --keep_isymbols --keep_osymbols S.fst S.fst

fstinvert S.fst S.fst
fstcompose S.fst $2 $4    #l_fst and #q_fst
