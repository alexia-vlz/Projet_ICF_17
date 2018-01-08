#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def nb_seq_fasta(fastafilename):
    with open(fastafilename, "r") as filein1:
        iseq = 0
        for ligne1 in filein1:
            regex = re.compile("^>")
            resultat1 = regex.search(ligne1)
            if resultat1:
                iseq += 1
    return iseq








if __name__ == '__main__':
    list_motif = store_motifs_meme("/home/avelasquez/Projet_ICF_17/results/results_test/meme.txt")