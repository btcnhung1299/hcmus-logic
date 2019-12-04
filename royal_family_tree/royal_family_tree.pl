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

/* Marital status */
married(elizabethII, philip).
married(charles, camilla).
married(andrew, sarah).
married(william, kate).
married(harry, meghan).
married(anne, timothy).
married(edward, sophie).
married(peter, autumn).
married(zara, mike).

divorced(diana, charles).
divorced(mark, anne).

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

aunt(Person, NieceNephew) :-
    sister(Person, Mother), mother(Mother, NieceNephew);
    sister(Person, Father), father(Father, NieceNephew).












