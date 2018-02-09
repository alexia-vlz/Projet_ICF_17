#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import time
import sys
import os
import re
sys.path.append('./source/')
import meme
import tomtom
import class_motif


# Initialisation des parametres
def initialization_argument():
    parser = argparse.ArgumentParser(description="ICF projet long")
    parser.add_argument('-fa', action="store", type=str,
                        dest='file_fasta', required=True, help="FASTA file \
                        sequences")
    parser.add_argument('-n', action="store", type=str,
                        dest='nb_motif', required=True, help="Number of \
                        motifs to find")
    parser.add_argument('-w', action="store", type=int, default=6,
                        dest='len_motif', required=True, help="Width of \
                        the motif - default = 6")
    parser.add_argument('-o', action="store", type=str, default="result_meme",
                        dest='dir_result_meme', required=True, help="Directory \
                        result name")
    parser.add_argument('-db', action="store", type=str, default=False,
                        dest='database', required=True, help="Path of \
                        database motif")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # ./source/projet_ICF.py -fa data/genes_zbtb.fasta -n 10 -w 8 -db bin/motif_databases/HUMAN/HOCOMOCOv9.meme -o results_testdna900
    debut = time.time()
    args = initialization_argument()
    adress_abs = os.getcwd()
    # Create the repertory that will contains the results
    repertoire_meme = adress_abs+"/results/"+args.dir_result_meme
    # print repertoire_meme
    if not os.path.exists(repertoire_meme):
        os.system("mkdir "+repertoire_meme)
    #else:
    #    sys.exit("This repository"+repertoire_meme+" already exists!\n")

    # Fixation du nombre d occurence minimal fixe a 10%
    fasta = adress_abs+"/"+args.file_fasta
    nseq = meme.nb_seq_fasta(fasta)
    nb_site = nseq/10

    # MEME
    print "\033[34mLancement de MEME\033[0m\n"
    cmd_meme = "meme {} -nmotifs {} -w {} -minsites {} -oc {} \
                -dna ".format(args.file_fasta, args.nb_motif,
                              args.len_motif, nb_site, repertoire_meme)
    # os.system(cmd_meme)

    # Motif meme et identifiant de sequence
    print "\033[34mRecuperation des motifs de MEME\033[0m\n"
    dico_id_motif_meme = meme.parse_motifs_meme(repertoire_meme,
                                                repertoire_meme)

    # TOMTOM
    print "\033[34mLancement de TOMTOM\033[0m\n"
    path_tomtom = repertoire_meme + "/" + "output_tomtom"
    print "Chemin result tomtom: {}".format(path_tomtom)
    # tomtom.start_tomtom(repertoire_meme, args.database, path_tomtom)
    
    # Motifs tomtom
    print "\033[34mRecuperation des motifs de TOMTOM\033[0m\n"
    # tomtom.parse_output_tomtom(path_tomtom)
    dico_idprot_motif_tomtom = tomtom.create_dico_tomtom(path_tomtom)

    # Identifiaction motif connu/pas connu dans result de Meme
    print "\033[34mDifferenciation des motifs connus/pas connus\033[0m\n"
    dico_known_or_not = class_motif.comparaison_motif(dico_id_motif_meme,
                                                    dico_idprot_motif_tomtom)
    print"\033[34mDifferenciation des motifs avec CG\033[0m\n"
    dico_known_CG = class_motif.look_CG(dico_known_or_not)
    print "\033[34mEcriture du fichier resultat\033[0m\n"
    class_motif.create_output(dico_known_CG, repertoire_meme)
    print "Resultat creer dans le repertoire : \
           \n {} \n".format(repertoire_meme)

    fin = time.time()
    print "Temps execution du programme:\n"
    print "{} secondes soit {} minutes ".format(fin-debut, (fin-debut)/60)
