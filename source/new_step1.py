#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os



sed -n '/P-value/,/--------------------------------------------------------------------------------/p' meme.txt > ../resmeme.txt 


def id_motifs_meme(filememe, dir_motif):
    """
        Fonction qui recupere les motifs de meme et le nom de la sequence fasta
        et les stock dans un dictionnaire clé:id seq, val: motif meme
    """
    fmotif = dir_motif+"/"+"lignes_motif_meme.txt"
    cmd = "sed -n '/P-value/,/--------------------------------------------------------------------------------/p' {}/meme.txt > {}".format(filememe, fmotif)
    os.system(cmd)
    lmotif_meme = []
    dico_meme = {}