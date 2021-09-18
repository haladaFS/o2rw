#!/bin/bash

#	"<a href=\"
for file in src_subjects/*; do
	if [[ -f $file ]] && [[ -w $file ]]; then
		echo $file
		sed -i -- 's/<a href=\"/<a href=\"source_html\//g' "$file"
	fi
done


for file in src_topics/*; do
	if [[ -f $file ]] && [[ -w $file ]]; then
		echo $file
		sed -i -- 's/<a href=\"/<a href=\"source_html\//g' "$file"
	fi
done


