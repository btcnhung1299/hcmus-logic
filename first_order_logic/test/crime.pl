criminal(x) :- american(x), weapon(y), sell(x, y, z), hostile(z).
sell(West, x, Nono) :- missile(x), own(Nono, x).
weapon(x) :- missile(x).
hostile(x) :- enemy(x, America).

own(Nono, B52).
missile(B52).
american(West).
enemy(Nono, America).
