# Otevřená skripta

Otevřená skripta je sbírka systematicky tříděných poznámek s návazností na předměty přednášené na FS ČVUT. Do sbírky je možné libovolně přispívat a libovolně editovat stávající záznamy. Všechny texty pracují s formátem `.tex`.

### Jak to funguje?

Text je nahrán do repozitáře GitHubu ve formátu `.tex`, kde je možné rovněž stávající texty editovat. Následně je automaticky přeložen do formátu `.html` a podle hlavičky zařazen pod příslušný předmět a příslušné téma.

Texty jsou řazeny **podle předmětů**, přičemž u každého je uvedeno označení:
"📚" - téma v rámci daného předmětu zkoušenou látkou
"💡" - téma je nad rámec přednášené látky
"✍️" - příklad
text bez označení je prostou součástí předmětu.

Texty jsou řazeny **podle témat**, tedy oblasti, do které zapadají. U každého textu je pak uvedeno, do kterých předmětů zapadá *(PPI, MT, ČMSII,...)*.

### Jak přidat text?
Každý nahraný `.tex` soubor musí být vybaven následující hlavičkou na první 6 řádcích:

```
%[HLAVICKA SOUBORU]
%Název článku = "Bernoulliho rovnice"
%Zařazení = "Mechanika kontinua"
%Předměty = "MT", "PTHT"
%Zařazení = "zk", "zk"
%Autor = "Jan Student"
```
* Název článku:
Kompletní a vystihující název textu.

* Zařazení (tématické):
Téma, oblast, do které text zapadá.

| Seznam témat:          |
|------------------------|
| Matematika             |
| Mechanika kontinua     |
| Mechanika tuhých těles |
| Konstruování           |
| Ostatní                |

* Předměty:
Seznam předmětů, ve kterých je daná látka přednášena, či do kterých zapadá.

* Zařazení (v rámci předmětu):
Odpovídá zařazení tématu v rámci daného předmětu:
`"zk"` - téma je zkouškovou otázkou
`""` - téma je součástí předmětu
`"+"` - téma je doplňující k látce předmětu
`"př"` - jedná se o příklad

Pořadí tagů pro zařazení musí odpovídat pořadí uvedených předmětů.

##### Poznámky

##### TODO:

