#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
filout  = open("genes_zbtb.fasta", "w")

i = 0
with open("hypo_Zbtb_genes.fasta", "r") as filein:
    for ligne in filein:
        i= i +1
        if i <= 30:
            filout.write(ligne)
filout.close()
"""

# Projet ICF

# command model : meme-chip -oc results/meme-chip1 -db meme-chip/JASPAR_CORE_2014_vertebrates.meme meme-chip/Klf1.100.s
# command model : meme /home/avelasquez/Projet_ICF_17/data/genes_zbtb.fasta -nmotifs 50 -w 8 -oc results/results_testdna -dna -nsites 3


# Installation de MEME

#cd meme_4.12.0
#./configure --prefix=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt --with-db=​../motif_databases --with-gs=/usr/bin/gs
#make
#make test
#make install
#export PATH=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme/bin:$PATH 


import argparse
import time
import sys
import os
import re
sys.path.append('./source/')
import step1

# Initialisation des parametres
def initialization_argument():
    parser = argparse.ArgumentParser(description="ICF projet long")
    parser.add_argument('-fa', action="store", type=str,
                        dest='file_fasta', required=True, help="FASTA file sequences")
    parser.add_argument('-n', action="store", type=str,
                       dest='nb_motif', required=True, help="Number of \
                       motifs to find")
    parser.add_argument('-w', action="store", type=int, default=6,
                       dest='len_motif', required=True, help="Width of \
                       the motif - default = 6")
    parser.add_argument('-o', action="store", type=str, default="result_meme",
                       dest='dir_result', required=True, help="Directory \
                       result name ")
    #parser.add_argument('-ns', action="store", type=int, default=False,
    #                   dest='nb_site', required=False, help="Number of \
    #                   site by motif - default = 2")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # ./source/projet_ICF.py -fa data/genes_zbtb.fasta -n 40 -w 8 -o results_testdna
    debut = time.time()
    args = initialization_argument()
    adress_abs = os.getcwd() #dans src
    # Create the repertory that will contains the results
    repertoire = adress_abs+"/results/"+args.dir_result
    if not os.path.exists(repertoire):
        os.system("mkdir "+repertoire)
    else:
        sys.exit("This repository"+repertoire+" already exists!\n")

    # Selection de motifs si il est present dans 10% des sequences
    fasta = adress_abs+"/"+args.file_fasta
    nseq = step1.nb_seq_fasta(fasta)
    #print ("Nombre de seq fasta : {}, \nNombre de sites à trouver est de 10 pourcent donc doit etre present dans minimum {} seq \n".format(nseq, nseq/10))
    nb_site = nseq/10

    # Lancement de MEME
    cmd_meme = "meme {} -nmotifs {} -w {} -nsites {} -oc {} -dna ".format(args.file_fasta, args.nb_motif, args.len_motif, nb_site, args.dir_result)
    os.system(cmd_meme)

    # Etape 1: selection motif
