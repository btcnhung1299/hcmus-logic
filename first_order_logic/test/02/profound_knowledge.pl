/* Gender */
male(prince_philip).
male(prince_charles).
male(prince_andrew).
male(prince_william).
male(prince_harry).
male(prince_george).
male(prince_louis).
male(archie_harrison).
male(mark_phillips).
male(timothy_laurence).
male(prince_edward).
male(peter_phillips).
male(mike_tindall).
male(james).

female(queen_elizabethII).
female(princess_diana).
female(camilla_parker_bowles).
female(sarah_ferguson).
female(kate_middleton).
female(meghan_markle).
female(princess_eugenie).
female(princess_beatrice).
female(princess_charlotte).
female(princess_anne).
female(sophie_rhys_jones).
female(autumn_phillips).
female(zara_tindall).
female(lady_louise).

/* Marital status
Note: marital status needs to be set for both partners.
*/
married(queen_elizabethII, prince_philip).
married(prince_philip,queen_elizabethII).
married(prince_charles, camilla_parker_bowles).
married(camilla_parker_bowles, prince_charles).
married(prince_andrew, sarah_ferguson).
married(sarah_ferguson, prince_andrew).
married(prince_william, kate_middleton).
married(kate_middleton, prince_william).
married(prince_harry, meghan_markle).
married(meghan_markle, prince_harry).
married(princess_anne, timothy_laurence).
married(timothy_laurence, princess_anne).
married(prince_edward, sophie_rhys_jones).
married(sophie_rhys_jones, prince_edward).
married(peter_phillips, autumn_phillips).
married(autumn_phillips, peter_phillips).
married(zara_tindall, mike_tindall).
married(mike_tindall, zara_tindall).

divorced(princess_diana, prince_charles).
divorced(prince_charles, princess_diana).
divorced(mark_phillips, princess_anne).
divorced(princess_anne, mark_phillips).

/* Family relationship
- Define from top to bottom, from left to right*/
parent(queen_elizabethII, prince_charles).
parent(prince_philip, prince_charles).
parent(queen_elizabethII, prince_andrew).
parent(prince_philip, prince_andrew).
parent(queen_elizabethII, princess_anne).
parent(prince_philip, princess_anne).
parent(queen_elizabethII, prince_edward).
parent(prince_philip, prince_edward).

parent(princess_diana, prince_william).
parent(prince_charles, prince_william).
parent(princess_diana, prince_harry).
parent(prince_charles, prince_harry).

parent(prince_andrew, princess_eugenie).
parent(sarah_ferguson, princess_eugenie).
parent(prince_andrew, princess_beatrice).
parent(sarah_ferguson, princess_beatrice).

parent(kate_middleton, prince_george).
parent(prince_william, prince_george).
parent(kate_middleton, princess_charlotte).
parent(prince_william, princess_charlotte).
parent(kate_middleton, prince_louis).
parent(prince_william, prince_louis).
parent(prince_harry, archie_harrison).
parent(meghan_markle, archie_harrison).

parent(mark_phillips, peter_phillips).
parent(princess_anne, peter_phillips).
parent(mark_phillips, zara_tindall).
parent(princess_anne, zara_tindall).

parent(prince_edward, lady_louise).
parent(sophie_rhys_jones, lady_louise).
parent(prince_edward, james).
parent(sophie_rhys_jones, james).

/* Rules */
father(Parent,Child) :- parent(Parent,Child), male(Parent).
mother(Parent,Child) :- parent(Parent,Child), female(Parent).

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

/* Aunt is mother's sister or father's sister or uncle's wife
- Uncle in this case can be interpreted as brother of parent
*/
/*OR operator: http://www.cse.unsw.edu.au/~billw/dictionaries/prolog/or.html*/
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), sister(Person, Parent).
aunt(Person, NieceNephew) :- female(Person), parent(Parent, NieceNephew), brother(Uncle, Parent), wife(Person, Uncle).

uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), brother(Person, Parent).
uncle(Person, NieceNephew) :- male(Person), parent(Parent, NieceNephew), sister(Aunt, Parent), husband(Person, Aunt).

niece(Person, AuntUncle) :- female(Person), aunt(AuntUncle, Person).
niece(Person, AuntUncle) :- female(Person), uncle(AuntUncle, Person).

nephew(Person, AuntUncle) :- male(Person), aunt(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), uncle(AuntUncle, Person).








