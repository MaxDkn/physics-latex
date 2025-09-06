#!/bin/bash

CHAPDIR="chapitre-0-example"
FILE="main.tex"
OUTPUTDIR="pdf"
OUTPUTNAME="$CHAPDIR.pdf"

mkdir -p "$OUTPUTDIR"

pdflatex "$CHAPDIR/$FILE"
pdflatex "$CHAPDIR/$FILE"


mv main.pdf "$OUTPUTDIR/$OUTPUTNAME"

rm -f *.aux *.log *.toc
echo "Compilation terminée : $OUTPUTDIR/$OUTPUTNAME"
