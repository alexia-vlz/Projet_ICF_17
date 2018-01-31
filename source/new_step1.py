#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os


#sed -n '/P-value/,/--------------------------------------------------------------------------------/p' meme.txt > ../resmeme.txt 

def id_motifs_meme(filememe, dir_motif):
    """
        Fonction qui recupere les motifs de meme et le nom de la sequence fasta
        et les stock dans un dictionnaire clé:id seq, val: motif meme
    """
    fmotif = dir_motif+"/"+"lignes_motif_meme2.txt"
    cmd = "sed -n '/P-value/,/--------------------------------------------------------------------------------/p' {}/meme.txt > {}".format(filememe, fmotif)
    os.system(cmd)
    with open(fmotif, "r") as filein:
        lfinal = []
        for ligne in filein:
            lmotifdico = []
            if (ligne[0:3] != "Sequence") or (ligne[0:3] != "---"):         
                #l = ligne.split()
                #seq = l[3] + l[4] + l[5]
        #print len(l)
        #print l[1]



