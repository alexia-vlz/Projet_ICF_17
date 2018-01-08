#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
cd meme_4.12.0
./configure --prefix=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt
make
make test
make install
export PATH=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme/bin:$PATH 
"""

# Projet ICF

# command model : meme-chip -oc results/meme-chip1 -db meme-chip/JASPAR_CORE_2014_vertebrates.meme meme-chip/Klf1.100.s
# command model : meme /home/avelasquez/Projet_ICF_17/data/genes_zbtb.fasta -nmotifs 50 -w 8 -oc results/results_testdna -dna -nsites 3

#meme /home/avelasquez/Projet_ICF_17/data/genes_zbtb.fasta -nmotifs 10 -w 8 -nsites 2 -oc results_testdna3 -dna
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
                       dest='dir_result_meme', required=True, help="Directory \
                       result name ")
    parser.add_argument('-ns', action="store", type=int, default=False,
                       dest='nb_site', required=False, help="Number of \
                       site by motif - default = 10")
    parser.add_argument('-db', action="store", type=str, default=False,
                       dest='database', required=True, help="Path of database motif")    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # ./source/projet_ICF.py -fa data/genes_zbtb.fasta -n 10 -w 8 -db bin/motif_databases/HUMAN/HOCOMOCOv9.meme -o results_testdna

     #./source/projet_ICF.py -fa data/genes_zbtb.fasta -n 40 -w 8 -db bin/motif_databases/HUMAN/HOCOMOCOv9.meme -o results_testdna3

    debut = time.time()
    args = initialization_argument()
    adress_abs = os.getcwd() #dans src
    # Create the repertory that will contains the results
    repertoire_meme = adress_abs+"/results/"+args.dir_result_meme
    #print repertoire_meme
    if not os.path.exists(repertoire_meme):
        os.system("mkdir "+repertoire_meme)
    #else:
    #    sys.exit("This repository"+repertoire_meme+" already exists!\n")

    # Selection de motifs si il est present dans 10% des sequences
    fasta = adress_abs+"/"+args.file_fasta
    nseq = step1.nb_seq_fasta(fasta)
    #print ("Nombre de seq fasta : {}, \nNombre de sites à trouver est de 10 pourcent donc doit etre present dans minimum {} seq \n".format(nseq, nseq/10))
    nb_site = nseq/10
    #print nb_site

    # MEME
    cmd_path = "export PATH=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme/bin:$PATH"
    #print cmd_path
    os.system(cmd_path)

    print ("Lancement de MEME\n")
    cmd_meme = "meme {} -nmotifs {} -w {} -nsites {} -oc {} -dna ".format(args.file_fasta, args.nb_motif, args.len_motif, nb_site, repertoire_meme)
    #print cmd_meme
    #os.system(cmd_meme)

    # TOMTOM
    print ("Lancement de TOMTOM\n")
    print ("Dossier meme: {}".format(repertoire_meme))
    print ("Dossier db: {}".format(args.database))
    path_tomtom = "results/output_tomtom"
    #step1.start_tomtom(repertoire_meme, args.database, path_tomtom)

    # Motif meme et identifiant de sequence
    print ("Recuperation des motifs de MEME\n")
    dico_id_motif_meme = step1.id_motifs_meme(repertoire_meme, repertoire_meme)

    # Motifs tomtom
    print ("Recuperation des motifs de TOMTOM\n")
    step1.parse_output_tomtom(path_tomtom)

    # Selection motif connu/pas connu
    print ("Differenciation des motifs connus/pas connus\n")
    step1.comparaison_meme_tomtom(dico_id_motif_meme, path_tomtom)

    fin = time.time()
    print "Temps execution du programme:\n"
    print " {} secondes soit {} minutes ".format(fin-debut, (fin-debut)/60)
