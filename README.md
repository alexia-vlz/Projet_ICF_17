# Projet long programmation Master 2 Bioinformatique  

Maladie ICF :
- rare 100 personnes au monde
- default / excess de méthylation épigenetique  

Objectif:
- trouver motifs de taille 5,6,8
- occurrence de 10%
- motifs connus ou non
- presence de CpG


# Input & Output

Input : fichier de séquences fasta  
Output: fichier indiquant pour chaque séquence, la position de début du motif,
	le motif, le contexte du motif (+/- 10nt), liste des identifiants de gènes
	(sinon mention "inconnu"), la presence de CG = 1 (sinon 0)


# Prérequi

### Mise en place structure
Creer la structure suivante de dossier:
/bin /data /source /results  

``` {}
cd Projet_ICF_17:
mkdir bin data source results
``` 

### Installation de MEME
``` {}
tar zxf meme_4.12.0.tar.gz 
cd meme_4.12.0
./configure --prefix=$HOME/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt --with-db=​motif_databases --with-gs=/usr/bin/gs
make
make test
make install
export PATH=$HOME/meme/bin:$PATH 
```
Plus de détails sur : http://meme-suite.org/doc/install.html?man_type=web

### Telecharger une base de donnée de motifs
Une base de donnée est fourni par MEME-TOOLS 'motif database' sur: http://meme-suite.org/doc/download.html?man_type=web  
Placer la base de donnée choisie dans le dossier /bin.


# Lancement du programme
``` {}
Dans le dossier meme/src:
$ chmod +x src/ 
```

``` {}
Dans le dossier Projet_ICF_17:

usage: projet_ICF.py [-h] -fa FILE_FASTA -n NB_MOTIF -w LEN_MOTIF -o
                     DIR_RESULT [-ns NB_SITE]

ICF projet long

optional arguments:
  -h, --help      show this help message and exit
  -fa FILE_FASTA  FASTA file sequences
  -n NB_MOTIF     Number of motifs to find
  -w LEN_MOTIF    Width of the motif - default = 6
  -o DIR_RESULT   Directory result name

```
