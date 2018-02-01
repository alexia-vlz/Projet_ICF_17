#! /usr/bin/env python
# -*- coding: utf-8 -*-


def start_tomtom(input_resultmeme, dbfile, outputdir):
    """
        Lancement de TOMTOM, chercher dans les motifs meme
        s'il sont connus c-a-d dans la database choisi.
        tomtom results/results_testdna/meme.txt bin/motif_databases/HUMAN/HOCOMOCOv9.meme
    """
    #cmd1 = "mkdir results/results_tomtom"
    #os.system(cmd1)
    cmd_tomtom = "tomtom {}/meme.txt {} -oc {} ".format(input_resultmeme, dbfile, outputdir)
    #cmd_tomtom = "tomtom {}/meme.txt {} ".format(input_resultmeme, dbfile)
    os.system(cmd_tomtom)


#awk -F'[\t]' '{print $2,$8}' tomtom.txt
def parse_output_tomtom(output_tomtom):
	"""
		Recuperation du nom de proteine(targetID) et du motif qui a été retrouvé dans la base 
		de données > dans une fichier tomtom_parse.
	"""
    sep = "-F'[\t]'"
    col = "'{print $2,$8}'"
    cmd2 = "awk {} {} {}/tomtom.txt > {}/tomtom_parse.txt".format(sep, col, output_tomtom, output_tomtom)
    #print cmd2
    os.system(cmd2)



if __name__ == '__main__':
	list_motif = store_motifs_meme("/home/avelasquez/Projet_ICF_17/results/results_test/meme.txt")