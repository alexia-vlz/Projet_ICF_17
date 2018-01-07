# Projet long programmation Master 2 Bioinformatique  

Maladie ICF :
- rare 100 personnes au monde
- default / excess de méthylation épigenetique  

Objectif: 
- GC content
- find motif



# Installation de MEME
``` {}
cd meme_4.12.0
./configure --prefix=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt --with-db=​../motif_databases --with-gs=/usr/bin/gs
make
make test
make install
export PATH=$HOME/avelasquez/Projet_ICF_17/bin/meme_4.12.0/meme/bin:$PATH
```


# Lancement du programme
``` {}
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
