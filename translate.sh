#!/bin/bash

for file in source_tex/*; do
	NAMETEX=${file}
	NAME=${file%.tex}
	NAMEHTML="${NAME}.html"

	echo $NAMETEX
	echo $NAME
	echo $NAMEHTML

	pandoc -s $NAMETEX -o $NAMEHTML --mathjax --metadata title=" "

	mv $NAMEHTML source_html/
done
