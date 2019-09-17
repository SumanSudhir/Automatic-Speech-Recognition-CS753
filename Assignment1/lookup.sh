
python3 search.py  --words $2

fstcompile --isymbols=input.txt --osymbols=input.txt --keep_isymbols --keep_osymbols word.fst word.fst
fstcompose word.fst L.fst compose.fst

fstprint --isymbols=input.txt --osymbols=output.txt compose.fst final.fst
python print_.py
