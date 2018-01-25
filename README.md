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

Input : fichier fasta de séquence  
Output: fichiers connus et inconnus

# Mise en place strucuture
Creer la structure suivante de dossier:
/bin /data /source /results  

``` {}
cd projet_long
mkdir bin data source results
``` 

# Installation de MEME
``` {}
tar zxf meme_4.12.0.tar.gz 
cd meme_4.12.0
./configure --prefix=$HOME/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt --with-db=​motif_databases --with-gs=/usr/bin/gs
make
make test
make install
export PATH=$HOME/meme/bin:$PATH 
```


# Lancement du programme

``` {}
Dans le dossier meme/src:
$ chmod +x src/

Si error: meme ou tomtom commande non trouvé retaper cette commande
$ export PATH=$HOME/meme/bin:$PATH  

usage: projet_ICF.py [-h] -fa FILE_FASTA -n NB_MOTIF -w LEN_MOTIF -o
                     DIR_RESULT [-ns NB_SITE]

ICF projet long

optional arguments:
  -h, --help      show this help message and exit
  -fa FILE_FASTA  FASTA file sequences
  -n NB_MOTIF     Number of motifs to find
  -w LEN_MOTIF    Width of the motif - default = 6
  -o DIR_RESULT   Directory result name
  -ns NB_SITE     Number of site by motif - default = 2
```
