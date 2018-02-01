#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

#def store_motifs_meme(filememe):
    """
    Recuperation des motifs trouvé par MEME du fichier meme.txt
    """
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

"""

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



# tomtom <query morifs> <target motif database>
# tomtom results/results_testdna/meme.txt bin/motif_databases/HUMAN/HOCOMOCOv9.meme
tomtom /home/avelasquez/Projet_ICF_17/results/results_testdna/meme.txt /home/avelasquez/Projet_ICF_17/bin/motif_databases/HUMAN/HOCOMOCOv9.meme


import os


    cmd = "tomtom {}/meme.txt {} -oc {} ".format(input_tomtom, db, output_tomtom)
    print(cmd)
    os.system(cmd)



    all_motif = filin1.readlines()
    known_motif = filin2.readlines()
    filin1.close()
    filin2.close()
    # recherche motifs connus ou non
    known_motif_c = [1, 3, 5]
    unknown_motif = [2, 4, 6]

    dico_motif_knwon_unknown_motif = {}
    dico_motif_knwon_unknown_motif["known_motif"] = known_motif_c
    dico_motif_knwon_unknown_motif["unknown_motif"] = unknown_motif
    #ecris dans un fichier la liste des motifs connus
    filout1 = open("../results/known_motif.txt","w")
    for elt in dico_motif_knwon_unknown_motif["known_motif"]:
        filout1.write(elt+"\n")
    filout1.close()


{'GCAAGTTG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GGTGAGAA': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GCTGCAGG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'TCTTGGGT': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GGGGTGAG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'ID': {'id_seq': {}, 'nom_motif': {}}, 'TGTCCAGG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}}
{'GCAAGTTG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GGTGAGAA': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GCTGCAGG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'TCTTGGGT': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'GGGGTGAG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}, 'ID': {'id_seq': {}, 'nom_motif': {}}, 'TGTCCAGG': {'id_seq': ['hg19_chr7_37484512_37484', 'hg19_chr1_57432060_57432', 'hg19_chr7_109600541_1096', 'hg19_chr7_135433303_1354', 'hg19_chr7_55141921_55142', 'hg19_chr1_181458789_1814', 'hg19_chr7_4751790_475189', 'hg19_chr7_55098846_55098'], 'nom_motif': {}}}
