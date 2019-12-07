/* Facts */
/* 1st generation */
male(prince_philip).
female(queen_elizabethII).
married(queen_elizabethII, prince_philip).

male(prince_charles).
male(prince_andrew).
male(prince_edward).
female(princess_anne).

parent(queen_elizabethII, prince_charles).
parent(prince_philip, prince_charles).
parent(queen_elizabethII, prince_andrew).
parent(prince_philip, prince_andrew).
parent(queen_elizabethII, princess_anne).
parent(prince_philip, princess_anne).
parent(queen_elizabethII, prince_edward).
parent(prince_philip, prince_edward).

/* 2nd generation */
female(sarah_ferguson).
married(prince_andrew, sarah_ferguson).

female(princess_eugenie).
female(princess_beatrice).
parent(prince_andrew, princess_eugenie).
parent(sarah_ferguson, princess_eugenie).
parent(prince_andrew, princess_beatrice).
parent(sarah_ferguson, princess_beatrice).

female(princess_diana).
married(prince_charles, princess_diana).

male(price_william).
male(price_harry).
parent(princess_diana, prince_william).
parent(prince_charles, prince_william).
parent(princess_diana, prince_harry).
parent(prince_charles, prince_harry).
divorced(princess_diana, prince_charles).

female(kate_middleton).
married(prince_william, kate_middleton).

/* Rules */
married(Person1, Person2) :- married(Person2, Person1).
husband(Person, Wife) :- married(Person, Wife), male(Person).
wife(Person, Husband) :- married(Person, Husband), female(Person).

father(Parent, Child) :- parent(Parent, Child), male(Parent).
mother(Parent, Child) :- parent(Parent, Child), female(Parent).
child(Child, Parent) :- parent(Parent, Child).
son(Child, Parent) :- child(Child, Parent), male(Child).
daughter(Child, Parent) :- child(Child, Parent), female(Child).

sibling(Person1, Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2).
sibling(Person1, Person2) :- sibling(Person2, Person1).
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).

aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), sister(Person, Parent).
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), brother(Uncle, Parent), wife(Person, Uncle).
uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), brother(Person, Parent).
uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), sister(Aunt, Parent), husband(Person, Aunt).

niece(Person, AuntUncle) :- female(Person), aunt(AuntUncle, Person).
niece(Person, AuntUncle) :- female(Person), uncle(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), aunt(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), uncle(AuntUncle, Person).
