/* Gender */
male(philip).
male(charles).
male(andrew).
male(william).
male(harry).
male(george).
male(louis).
male(archie).
male(mark).
male(timothy).
male(edward).
male(peter).
male(mike).
male(james).

female(elizabethII).
female(diana).
female(camilla).
female(sarah).
female(kate).
female(meghan).
female(eugenie).
female(beatrice).
female(charlotte).
female(anne).
female(sophie).
female(autumn).
female(zara).
female(louise).

/* Marital status
Note: marital status needs to be set for both partners.
*/
married(elizabethII, philip).
married(philip, elizabethII).
married(charles, camilla).
married(camilla, charles).
married(andrew, sarah).
married(sarah, andrew).
married(william, kate).
married(kate, william).
married(harry, meghan).
married(meghan, harry).
married(anne, timothy).
married(timothy, anne).
married(edward, sophie).
married(sophie, edward).
married(peter, autumn).
married(autumn, peter).
married(zara, mike).
married(mike, zara).

divorced(diana, charles).
divorced(charles, diana).
divorced(mark, anne).
divorced(anne, mark).

/* Family relationship
- Define from top to bottom, from left to right*/
parent(elizabethII, charles).
parent(philip, charles).
parent(elizabethII, andrew).
parent(philip, andrew).
parent(elizabethII, anne).
parent(philip, anne).
parent(elizabethII, edward).
parent(philip, edward).

parent(diana, william).
parent(charles, william).
parent(diana, harry).
parent(charles, harry).

parent(andrew, eugenie).
parent(sarah, eugenie).
parent(andrew, beatrice).
parent(sarah, beatrice).

parent(kate, george).
parent(william, george).
parent(kate, charlotte).
parent(william, charlotte).
parent(kate, louis).
parent(william, louis).
parent(harry, archie).
parent(meghan, archie).

parent(mark, peter).
parent(anne, peter).
parent(mark, zara).
parent(anne, zara).

parent(edward, louise).
parent(sophie, louise).
parent(edward, james).
parent(sophie, james).

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

sibling(Person1,Person2) :- father(Father, Person1), father(Father, Person2), mother(Mother, Person1), mother(Mother, Person2), Person1 \= Person2.
brother(Person,Sibling) :- sibling(Person, Sibling), male(Sibling).
sister(Person,Sibling) :- sibling(Person, Sibling), female(Sibling).

/* Aunt is mother's sister or father's sister or uncle's wife
- Uncle in this case can be interpreted as brother of parent
*/
/*OR operator: http://www.cse.unsw.edu.au/~billw/dictionaries/prolog/or.html*/
aunt(Person, NieceNephew) :- parent(Parent, NieceNephew),
    (sister(Parent, Person);(brother(Parent, Uncle), wife(Person, Uncle))).

uncle(Person, NieceNephew) :- parent(Parent, NieceNephew),
    (brother(Parent, Person);(sister(Parent, Aunt), husband(Person, Aunt))).

niece(Person, AuntUncle) :- female(Person),
    (aunt(AuntUncle, Person); uncle(AuntUncle, Person)).

nephew(Person, AuntUncle) :- male(Person),
    (aunt(AuntUncle, Person); uncle(AuntUncle, Person)).
