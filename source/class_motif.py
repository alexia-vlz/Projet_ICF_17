#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os


def comparaison_motif(dico_meme, dico_tomtom):
    """
        Comparaison des motifs de MEME avec les motifs connu trouvé par TOMTOM.
        - dico_meme = clé: id seq, val: motif meme resulat brut
        - dico_tomtom = clé: motif tomtom, val: nom proteine connue
        Output : dictionnaire avec classification des motifs inconnu ou connu
        avec liste des noms de proteines connu
    """
    compt_motif = 0
    for key, val in dico_meme.items():
        for liste in val:
            # grande liste composé de sous listes
            compt_motif += 1
            compt = 0
            for key2, val2 in dico_tomtom.items():
                if liste[1].upper() == key2:
                    # evite ajout de liste des nom prot, mais chaque elmt \
                    # de liste dico-omtom ajouter par elmt dans 'liste'
                    for elmt in dico_tomtom[key2]:
                        liste.append(elmt)
                        # print key2
                        # print val
                if liste[1].upper() not in dico_tomtom.keys():
                    compt += 1
                    if compt == len(dico_tomtom):
                        liste.append("inconnu")
        # print val
    # print dico_tomtom
    print "Nombre total de motif trouvé: {}\n".format(compt_motif)
    return dico_meme


def look_CG(dico_meme):
    """
        Recherche si les motifs contiennent un CpG marqueur de methylation
        Output: dictionnaire contenant pour chaque séquence, le motifs,
        sa position, s'il est inconnu ou sa liste de proteine ou il est
        retrouvé, s'il posséde un dinucleaotide CG =1 sinon = 0.
    """
    compt_cg = 0
    for key, val in dico_meme.items():
        for subliste in val:
            # print subliste
            regex = re.compile("CG|cg")
            resultat = regex.search(subliste[1])
            if resultat:
                subliste.append("1")
                compt_cg += 1
                # print subliste
            else:
                subliste.append("0")
    print "Nombre de motifs avec un CG : {}\n".format(compt_cg)
    return dico_meme


def create_output(dico_info, directory):
    """
        Creation d un fichier sortie avec le nom de la sequence,
        la position start du motif, le motif, 10 nt avant/apres le motifs,
        identifiants des genes connus, prensence de CG avec un 1 sinon 0.
        a partir dun dictionnaire.
    """
    file_result = directory + "/" + "classification_motifs.txt"
    with open(file_result, "w") as fileout:
        fileout.write("Sequence_name" "\t" "start" "\t" "motif" "\t"
                      "around_motif" "\t" "IDgene" "\t" "CG" "\n")
        for key, val in dico_info.items():
            for subliste in val:
                tfs = subliste[2:-1]
                ligne = key + "\t" + subliste[0] + "\t" + subliste[1] + "\t"
                fileout.write(ligne)
                for tf in tfs:
                    fileout.write(tf + " ")
                fileout.write("\t" + subliste[-1] + "\n")
    return file_result


def stat(filename):
    print "Nombre total de motif inconnu: "
    cmd = " grep 'inconnu' {} | wc -l".format(filename)
    os.system(cmd)



def comparaison_meme_tomtom(dico_meme, output_tomtom):
    """
        Comparaison des motifs de MEME avec les motifs connu trouvé par TOMTOM.
        - dico_meme = clé: id seq, val: motif meme resulat brut
        - fichier info tomtom : nom motif connu humain, motif tomtom
        Output : fichier connu de motif(doublon a cause des diffrent
        nom de motif et des diffrenret nom de seq ayant le meme motif)
    """
    fileparse = output_tomtom+'/'+'tomtom_parse.txt'
    filetmp = output_tomtom+'/'+'tomtom_connu.txt'
    filetmp1 = output_tomtom+'/'+'tomtom_inconnu.txt'
    fileout = open(filetmp, "w")
    fileout1 = open(filetmp1, "w")
    with open(fileparse, "r") as fileintomtom:
        for ligne in fileintomtom:
            l = ligne.split()
            # l[0] nom prot , l[1]: motif
            for key, val in dico_meme.items():
                if l[1] == dico_meme[key]:
                    fileout.write(dico_meme[key]+' '+key+' '+l[0]+'\n')
                elif(l[1] not in dico_meme[key]):
                    fileout1.write(dico_meme[key]+' '+key+'\n')
    fileout.close()
    fileout1.close()