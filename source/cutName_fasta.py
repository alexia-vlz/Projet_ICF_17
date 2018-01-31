#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
"""
with open("../data/genes_zbtb.fasta", "r") as filein1:
    with open("../data/genes_zbtbClean.fasta", "w") as filein:
        regex = re.compile(r"(_[0-9]+_\+) ([0-9]+)", re.IGNORECASE)
        for ligne1 in filein1:
            resligne = regex.sub("",ligne1)
            filein.write(resligne)   
"""

#Numeroter toutes les lignes entre 2 patterns (affiche 1 numero par ligne)
#sed -n '/pattern1/,/pattern2/{=;d;}' in.txt 

cmd = "grep -A2 '^BL' {}/meme.txt > {}".format(filememe, fmotif)
os.system(cmd)

sed -n '/P-value/,/--------------------------------------------------------------------------------/p' meme.txt > ../resmeme.txt 