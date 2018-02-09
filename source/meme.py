#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os


def nb_seq_fasta(fastafilename):
    """
        Fonction qui calcul le nombre de sequence
        fasta il y a en entree
    """
    with open(fastafilename, "r") as filein1:
        iseq = 0
        for ligne1 in filein1:
            regex = re.compile("^>")
            resultat1 = regex.search(ligne1)
            if resultat1:
                iseq += 1
    return iseq


def parse_motifs_meme(filememe, dir_motif):
    """
        Fonction qui recupere les motifs de meme, sa position et le nom
        de la sequence fasta et les stock dans un dictionnaire
        clé:id seq, val: positions + motif + seq contenant le motif meme
        et 10 pb avant et apres le motif.
    """
    fmotif = dir_motif+"/"+"lignes_motif_meme2.txt"
    cmd = "sed -n '/P-value/,/--------------------------------------------------------------------------------/p' {}/meme.txt > {}".format(filememe, fmotif)
    os.system(cmd)
    dicomeme = {}
    with open(fmotif, "r") as filein:
        for ligne in filein:
            linfo = []
            if (ligne[0:3] != "Sequence") or (ligne[0:3] != "---"):
                regex = re.compile("(.+[^ ]) +([0-9]+) +(.+) ([ATGC|atgc]+) ([ATGC|atgc]+) ([ATGC|atgc]+)")
                resultat = regex.search(ligne)
                if resultat:
                    seqjoin = resultat.group(4) + resultat.group(5) + \
                              resultat.group(6)
                    info_match = [resultat.group(2), resultat.group(5), seqjoin]
                    if resultat.group(1) not in dicomeme.keys():
                        dicomeme[resultat.group(1)] = linfo
                        dicomeme[resultat.group(1)].append(info_match)
                    if resultat.group(1) in dicomeme.keys():
                        if info_match not in dicomeme[resultat.group(1)]:
                            dicomeme[resultat.group(1)].append(info_match)
        # print dicomeme
    return dicomeme
