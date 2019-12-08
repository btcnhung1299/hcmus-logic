/*Gender*/
male(james_potter).
male(harry_potter).
male(james_sirius_potter).
male(albus_severus_potter).
male(draco_malfoy).
male(scorpius_malfoy).
male(arthur_weasley).
male(ron_weasley).
male(hugo_weasley).
male(george_weasley).
male(fred_weasley).
male(fred_weasley_ii).
male(percy_weasley).
male(bill_weasley).
male(louis_weasley).
male(remus_lupin).
male(teddy_lupin).

female(lily_potter).
female(ginny_weasley).
female(lily_luna_potter).
female(astoria_greengrass).
female(molly_weasley).
female(hermione_granger).
female(rose_weasley).
female(angelina_johnson).
female(roxanne_weasley).
female(nymphadora_tonks).
female(audrey_weasley).
female(molly_weasley_ii).
female(lucy_weasley).
female(fleur_delacour).
female(victoire_weasley).
female(dominique_weasley).

parent(lily_potter, harry_potter).
parent(james_potter, harry_potter).
parent(harry_potter, james_sirius_potter).
parent(ginny_weasley, james_sirius_potter).
parent(harry_potter, lily_luna_potter).
parent(ginny_weasley, lily_luna_potter).
parent(harry_potter, albus_severus_potter).
parent(ginny_weasley, albus_severus_potter).

parent(draco_malfoy, scorpius_malfoy).
parent(astoria_greengrass, scorpius_malfoy).

parent(remus_lupin, teddy_lupin).
parent(nymphadora_tonks, teddy_lupin).

parent(molly_weasley, ginny_weasley).
parent(arthur_weasley, ginny_weasley).
parent(molly_weasley, ron_weasley).
parent(arthur_weasley, ron_weasley).
parent(molly_weasley, george_weasley).
parent(arthur_weasley, george_weasley).
parent(molly_weasley, fred_weasley).
parent(arthur_weasley, fred_weasley).
parent(molly_weasley, percy_weasley).
parent(arthur_weasley, percy_weasley).
parent(molly_weasley, bill_weasley).
parent(arthur_weasley, bill_weasley).

parent(ron_weasley, rose_weasley).
parent(hermione_granger, rose_weasley).
parent(ron_weasley, hugo_weasley).
parent(hermione_granger, hugo_weasley).

parent(george_weasley, fred_weasley_ii).
parent(angelina_johnson, fred_weasley_ii).
parent(george_weasley, roxanne_weasley).
parent(angelina_johnson, roxanne_weasley).

parent(percy_weasley, molly_weasley_ii).
parent(audrey_weasley, molly_weasley_ii).
parent(percy_weasley, lucy_weasley).
parent(audrey_weasley, lucy_weasley).

parent(bill_weasley, victoire_weasley).
parent(fleur_delacour, victoire_weasley).
parent(bill_weasley, louis_weasley).
parent(fleur_delacour, louis_weasley).
parent(bill_weasley, dominique_weasley).
parent(fleur_delacour, dominique_weasley).

/*Marital status*/
married(lily_potter, james_potter).
married(james_potter, lily_potter).
married(harry_potter, ginny_weasley).
married(ginny_weasley, harry_potter).
married(draco_malfoy, astoria_greengrass).
married(astoria_greengrass, draco_malfoy).
married(molly_weasley, arthur_weasley).
married(arthur_weasley, molly_weasley).
married(ron_weasley, hermione_granger).
married(hermione_granger, ron_weasley).
married(george_weasley, angelina_johnson).
married(angelina_johnson, george_weasley).
married(percy_weasley, audrey_weasley).
married(audrey_weasley, percy_weasley).
married(bill_weasley, fleur_delacour).
married(fleur_delacour, bill_weasley).
married(remus_lupin, nymphadora_tonks).
married(nymphadora_tonks, remus_lupin).

dating(teddy_lupin, victoire_weasley).
dating(victoire_weasley, teddy_lupin).

/* Rules */
father(Parent,Child) :- parent(Parent,Child), male(Parent).
mother(Parent,Child) :- parent(Parent,Child), female(Parent).

boyfriend(Person, Girlfriend) :- dating(Person, Girlfriend), male(Person).
girlfriend(Person, Boyfriend) :- dating(Person, Boyfriend), female(Person).

husband(Person,Wife) :- married(Person,Wife), male(Person).
wife(Person,Husband) :- married(Person,Husband), female(Person).

child(Child,Parent) :- parent(Parent,Child).
son(Child,Parent) :- child(Child,Parent), male(Child).
daughter(Child,Parent) :- child(Child,Parent), female(Child).

grandparent(GP,GC) :- parent(GP,Parent), parent(Parent,GC).
grandmother(GM,GC) :- grandparent(GM,GC), female(GM).
grandfather(GF,GC) :- grandparent(GF,GC), male(GF).

grandchild(GC,GP) :- grandparent(GP,GC).
grandson(GS,GP) :- grandchild(GS,GP),male(GS).
granddaughter(GD,GP) :- grandchild(GD,GP), female(GD).

sibling(Person1,Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2).
sibling(Person1,Person2) :- sibling(Person2, Person1).
brother(Person,Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person,Sibling) :- sibling(Person, Sibling), female(Person).

aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), sister(Person, Parent).
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), brother(Uncle, Parent), wife(Person, Uncle).

uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), brother(Person, Parent).
uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), sister(Aunt, Parent), husband(Person, Aunt).

niece(Person, AuntUncle) :- female(Person), aunt(AuntUncle, Person).
niece(Person, AuntUncle) :- female(Person), uncle(AuntUncle, Person).

nephew(Person, AuntUncle) :- male(Person), aunt(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), uncle(AuntUncle, Person).

