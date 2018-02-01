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
        Fonction qui recupere les motifs de meme, sa position et le nom de la sequence fasta
        et les stock dans un dictionnaire clé:id seq, val: positions + seq contenant le motif meme
        et 10 pb avant et apres le motif. 
    """
    fmotif = dir_motif+"/"+"lignes_motif_meme2.txt"
    cmd = "sed -n '/P-value/,/--------------------------------------------------------------------------------/p' {}/meme.txt > {}".format(filememe, fmotif)
    os.system(cmd)
    dicomeme = {}
    with open(fmotif, "r") as filein:
        for ligne in filein:
            ltuple = []
            if (ligne[0:3] != "Sequence") or (ligne[0:3] != "---"):         
                regex = re.compile("(.+[^ ]) +([0-9]+) +(.+) ([ATGC|atgc]+) ([ATGC|atgc]+) ([ATGC|atgc]+)")
                resultat = regex.search(ligne)
                if resultat:
                    seqjoin = resultat.group(4) + resultat.group(5) + resultat.group(6)
                    l = resultat.group(1) + " " + resultat.group(2) + " " + seqjoin
                    tu = (resultat.group(2), resultat.group(5), seqjoin)
                    if resultat.group(1) not in dicomeme.keys():
                        dicomeme[resultat.group(1)] = ltuple
                        dicomeme[resultat.group(1)].append(tu)
                    if resultat.group(1) in dicomeme.keys():
                        if tu not in dicomeme[resultat.group(1)]:
                            dicomeme[resultat.group(1)].append(tu)
        print dicomeme
    return dicomeme


def id_motifs_meme(filememe, dir_motif):
    """
        Fonction qui recupere les motifs de meme et le nom de la sequence fasta
        et les stock dans un dictionnaire clé:id seq, val: motif meme
    """
    fmotif = dir_motif+"/"+"lignes_motif_meme.txt"
    cmd = "grep -A2 '^BL' {}/meme.txt > {}".format(filememe, fmotif)
    os.system(cmd)
    lmotif_meme = []
    dico_meme = {}
    with open(fmotif, "r") as fileinmeme:
        for ligne in fileinmeme:
            lmotifdico= []
            if (ligne[0:3] != "BL") or (ligne[0:3] != "--"):
                regex = re.compile("(.+) \(.+\) ([ATGC]+)")
                resultat = regex.search(ligne)
                if resultat:
                    #group 1 = id seq et group 2 = motif mem
                    if resultat.group(2) not in lmotif_meme:
                        lmotif_meme.append(resultat.group(2))
                        if resultat.group(1) not in dico_meme.keys():
                            #dico_meme[resultat.group(1)] = resultat.group(2)
                            dico_meme[resultat.group(1)] =  lmotifdico
                        if resultat.group(1) in dico_meme.keys():
                            if resultat.group(2) not in lmotifdico:
                                dico_meme[resultat.group(1)].append(resultat.group(2))

        print dico_meme
        print "length l : {}".format(len(lmotif_meme))
        print "length dico: {}".format(len(dico_meme))
    return dico_meme




def comparaison_meme_tomtom(dico_meme, output_tomtom):
    """
        Comparaison des motifs de MEME avec les motifs connu trouvé par TOMTOM.
        - dico_meme = clé: id seq, val: motif meme resulat brut
        - fichier info tomtom : nom motif connu humain, motif tomtom
        Output : fichier connu de motif(doublon a cause des diffrent nom de motif
        et des diffrenret nom de seq ayant le meme motif)
    """
    fileparse = output_tomtom+'/'+'tomtom_parse.txt'
    filetmp = output_tomtom+'/'+'tomtom_connu.txt'
    filetmp1 = output_tomtom+'/'+'tomtom_inconnu.txt'
    fileout = open(filetmp, "w")
    fileout1 = open(filetmp1, "w")
    with open(fileparse,"r") as fileintomtom:
        for ligne in fileintomtom:
            l = ligne.split()
            #l[0] nom prot, l[1]: motif
            for key, val in dico_meme.items():
                if l[1] ==  dico_meme[key]:
                    fileout.write(dico_meme[key]+' '+key+' '+l[0]+'\n')
                elif(l[1] not in dico_meme[key]):
                    fileout1.write(dico_meme[key]+' '+key+'\n')
    fileout.close()
    fileout1.close()





#def comparaison_meme_tomtom(dico_meme, output_tomtom):
    """
        Comparaison des motifs de MEME avec les motifs connu trouvé par TOMTOM.
        - dico_meme = clé: id seq, val: motif meme resulat brut
        - fichier info tomtom : nom motif connu humain, motif tomtom
        Veut faire un dico, clé1=motif, val= deux clés "id_seq", "nommotif",
        val de "id_seq" = liste de tout les id ayant le meme motif
        val de "nom_motif" = liste de tous les nom de motif ayant le mm motif
    """
    """
    fileparse = output_tomtom+'/'+'tomtom_parse.txt'
    filetmp = output_tomtom+'/'+'tomtom_connu.txt'
    filetmp1 = output_tomtom+'/'+'tomtom_inconnu.txt'
    fileout = open(filetmp, "w")
    fileout1 = open(filetmp, "w")
    with open(fileparse,"r") as fileintomtom:
        new_dico = {}
        liste_id = []
        liste_nom = []
        for ligne in fileintomtom:
            l = ligne.split()
            for key, val in dico_meme.items():
                if l[1] not in new_dico.keys():
                    new_dico[l[1]] = {}
                if "id_seq" not in new_dico[l[1]].keys():
                    new_dico[l[1]]["id_seq"] = {}
                if "nom_motif" not in new_dico[l[1]].keys():
                    new_dico[l[1]]["nom_motif"] = {}

        for key, val in dico_meme.items():
            for key2, val2 in new_dico.items():
                #print "dico key : {}".format(dico_meme[key])
                print val
                print "dico key : {}".format(new_dico[val])
                if val in new_dico.keys():
                    if key not in liste_id:
                        liste_id.append(key)
                new_dico[val]["id_seq"] = liste_id
            else:
                    print "pas dans le dico connu"
                    continue
            print new_dico

                    #if "nom_motif" not in new_dico[l[1]].keys():
                    #    new_dico[l[1]]["nom_motif"] = liste_nom.append(l[0])

"""



if __name__ == '__main__':
    list_motif = store_motifs_meme("/home/avelasquez/Projet_ICF_17/results/results_test/meme.txt")