#! /usr/bin/env python
# -*- coding: utf-8 -*-


def store_motifs_meme():
    with open("hypo_Zbtb_genes.fasta", "r") as filein:
        for ligne in filein:
            regex = re.compile("(^ATOM +)([0-9]+)( +([CONH]|H1) )")
            resultat = regex.search(ligne)
            if resultat:
                l = ligne.split()
                liste = l[2] + ' ' + l[3]+ ' ' + l[5] + ' ' + l[6] + ' ' + l[7] + ' ' +l[8] +'\n'
                l2.append(l[3])
    return 


if __name__ == '__main__':
    store_motifs_meme