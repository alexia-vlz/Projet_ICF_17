#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def store_motifs_meme(filememe):
    """
    Recuperation des motifs trouvé par MEME du fichier meme.txt
    """
    fileout = open("motif_meme_found.txt","w")
    with open(filememe, "r") as filein:
        l_motif = []
        for ligne in filein:
            regex = re.compile("Multilevel")
            resultat = regex.search(ligne)
            if resultat:
                l = ligne.split()
                liste = l[1] + '\n'
                l_motif.append(l[1])
                fileout.write(liste)
    fileout.close()
    return l_motif





if __name__ == '__main__':
    list_motif = store_motifs_meme("/home/avelasquez/Projet_ICF_17/results/results_test/meme.txt")