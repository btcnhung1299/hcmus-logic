/* Gender */
male(prince_philip).
male(prince_andrew).
male(prince_edward).

female(queen_elizabethII).
female(princess_anne).
female(princess_eugenie).
female(princess_beatrice).

/* Marital status
Note: marital status needs to be set for both partners.
*/
married(queen_elizabethII, prince_philip).

/* Family relationship
- Define from top to bottom, from left to right*/
parent(queen_elizabethII, prince_andrew).
parent(prince_philip, prince_andrew).
parent(queen_elizabethII, princess_anne).
parent(prince_philip, princess_anne).
parent(queen_elizabethII, prince_edward).
parent(prince_philip, prince_edward).

parent(prince_andrew, princess_eugenie).
parent(prince_andrew, princess_beatrice).


/* Rules */
father(Parent, Child) :- parent(Parent, Child), male(Parent).
mother(Parent, Child) :- parent(Parent, Child), female(Parent).

sibling(Person1, Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2).
sibling(Person1, Person2) :- sibling(Person2, Person1).
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).

aunt(Person, NieceNephew) :- parent(Parent, NieceNephew), sister(Person, Parent).
niece(Person, Aunt) :- female(Person), aunt(Aunt, Person).
