#!/bin/bash

rm index.html
rm index_subjects.html

cat "src_core/header.html" >> index.html
cat "src_core/header.html" >> index_subjects.html

cat "src_core/sort.html" >> index.html
cat "src_core/sort.html" >> index_subjects.html

#cat "src_core/articles_topics.html" >> index.html
#cat "src_core/articles_subjects.html" >> index_subjects.html

echo "<div id="needtowrap">" >> index.html
echo "<div id="needtowrap">" >> index_subjects.html

#source topics
echo "<h3 class="unnumbered">Matematika</h3>" >> index.html
cat "src_topics/math.html" >> index.html

echo "<h3 class="unnumbered">Klasická mechanika</h3>" >> index.html
cat "src_topics/mechclassical.html" >> index.html

echo "<h3 class="unnumbered">Mechanika kontinua</h3>" >> index.html
cat "src_topics/mechcontinuum.html" >> index.html

echo "<h3 class="unnumbered">Konstruování</h3>" >> index.html
cat "src_topics/construction.html" >> index.html

echo "<h3 class="unnumbered">Ostatní</h3>" >> index.html
cat "src_topics/other.html" >> index.html

#source subjects
for subjects in src_subjects/*; do
	SUBJECTHTML=${subjects}
	SUBJECT=${subjects%.html}
	SUBJECT=${SUBJECT##*/}

	echo "<h3 class="unnumbered">${SUBJECT}</h3>" >> index_subjects.html
	cat $SUBJECTHTML >> index_subjects.html
done

echo "</div>" >> index.html
echo "</div>" >> index_subjects.html

cat "src_core/comments.html" >> index.html
cat "src_core/comments.html" >> index_subjects.html

cat "src_core/footer.html" >> index.html
cat "src_core/footer.html" >> index_subjects.html
