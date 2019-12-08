child(X, molly_weasley).
X = fred_weasley ;
X = percy_weasley ;
X = ron_weasley ;
X = george_weasley ;
X = ginny_weasley ;
X = bill_weasley.

wife(hermione_granger, harry_potter).
false.

boyfriend(X, victoire_weasley).
X = teddy_lupin.

girlfriend(roxanne_weasley, teddy_lupin).
false.

son(X, audrey_weasley).
false.

aunt(X, dominique_weasley).
X = audrey_weasley ;
X = ginny_weasley ;
X = hermione_granger ;
X = angelina_johnson.

uncle(X, lily_luna_potter).
X = percy_weasley ;
X = ron_weasley ;
X = george_weasley ;
X = fred_weasley ;
X = bill_weasley.

grandchild(X, arthur_weasley).
X = lily_luna_potter ;
X = dominique_weasley ;
X = molly_weasley_ii ;
X = james_sirius_potter ;
X = louis_weasley ;
X = roxanne_weasley ;
X = fred_weasley_ii ;
X = victoire_weasley ;
X = lucy_weasley ;
X = rose_weasley ;
X = hugo_weasley ;
X = albus_severus_potter.

grandson(james_sirius_potter, X).
X = james_potter ;
X = arthur_weasley ;
X = molly_weasley ;
X = lily_potter.

granddaughter(lucy_weasley, james_potter).
false.

daughter(X, fleur_delacour).
X = victoire_weasley ;
X = dominique_weasley.

father(X, hugo_weasley).
X = ron_weasley.

mother(molly_weasley, molly_weasley_ii).
false.

husband(X, nymphadora_tonks).
X = remus_lupin.

brother(X, scorpius_malfoy).
false.

sister(rose_weasley, hugo_weasley).
true.

sibling(X, albus_severus_potter).
X = lily_luna_potter ;
X = james_sirius_potter.

grandfather(X, louis_weasley).
X = arthur_weasley.

grandmother(X, fred_weasley_ii).
X = molly_weasley.

grandparent(X, james_sirius_potter).
X = james_potter ;
X = arthur_weasley ;
X = molly_weasley ;
X = lily_potter.

niece(X, angelina_johnson).
X = victoire_weasley ;
X = lily_luna_potter ;
X = dominique_weasley ;
X = lucy_weasley ;
X = rose_weasley ;
X = molly_weasley_ii.

nephew(X, fred_weasley).
X = james_sirius_potter ;
X = louis_weasley ;
X = hugo_weasley ;
X = fred_weasley_ii ;
X = albus_severus_potter.

nephew(X, percy_weasley).
X = james_sirius_potter ;
X = louis_weasley ;
X = hugo_weasley ;
X = fred_weasley_ii ;
X = albus_severus_potter.

