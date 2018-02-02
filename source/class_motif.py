#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

def comparaison_motif(dico_meme, dico_tomtom):
    for key, val in dico_meme.items():
        for key2, val2 in dico_tomtom.items():
            #print key
            #print dico_meme[key] #grande liste composé de sous listes
            #print val[0]
            #print val[0][1]
            #parcours la liste composée de listes (position, motif, seq)
            for i in range(0,len(val)):
                #print val[i] #une sous liste
                #print val[i][1] #2eme elmt dune sous liste
                motif_meme = val[i][1]
                motif_meme = motif_meme.upper()
                if motif_meme == key2:
                    print "meme: {}".format(motif_meme)
                    print "tomtom: {}".format(key2)
                    print dico_meme[key]
                    val[i].append(dico_tomtom[key2])
    print dico_meme
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