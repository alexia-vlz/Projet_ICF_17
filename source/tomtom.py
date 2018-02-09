#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from itertools import islice


def start_tomtom(input_resultmeme, dbfile, outputdir):
    """
        Lancement de TOMTOM, chercher dans les motifs meme
        s'il sont connus c-a-d dans la database choisi.
        tomtom results/results_testdna/meme.txt
        bin/motif_databases/HUMAN/HOCOMOCOv9.meme
    """
    cmd_tomtom = "tomtom {}/meme.txt {} -oc {} ".format(input_resultmeme,
                                                        dbfile, outputdir)
    # cmd_tomtom = "tomtom {}/meme.txt {} ".format(input_resultmeme, dbfile)
    os.system(cmd_tomtom)


# awk -F'[\t]' '{print $2,$8}' tomtom.txt
def parse_output_tomtom(output_tomtom):
    """
        Recuperation du nom de proteine(targetID) et du motif qui a été
        retrouvé dans la base de données > dans le fichier tomtom_parse.txt
    """
    sep = "-F'[\t]'"
    col = "'{print $2,$8}'"
    cmd2 = "awk {} {} {}/tomtom.txt > \
    {}/tomtom_parse.txt".format(sep, col, output_tomtom, output_tomtom)
    os.system(cmd2)


def create_dico_tomtom(path_parse_tomtom):
    fileparse_tomtom = path_parse_tomtom + "/" + "tomtom_parse.txt"
    with open(fileparse_tomtom, "r") as fileintomtom:
        dico_tomtom = {}
        for ligne in islice(fileintomtom, 1, None):
            lnomID = []
            l = ligne.split()
            nom_id = l[0]
            motif_known = l[1]
            if motif_known not in dico_tomtom.keys():
                dico_tomtom[motif_known] = lnomID
                dico_tomtom[motif_known].append(nom_id)
            if motif_known in dico_tomtom.keys():
                if nom_id not in dico_tomtom[motif_known]:
                    dico_tomtom[motif_known].append(nom_id)
        print "Nombre de motifs connus: {}\n".format(len(dico_tomtom))
    return dico_tomtom

