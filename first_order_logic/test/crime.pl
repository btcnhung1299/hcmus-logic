Criminal(x) :- American(x), Weapon(y), Sell(x, y, z), Hostile(z).
Sell(West, x, Nono) :- Missile(x), Own(Nono, x).
Weapon(x) :- Missile(x).
Hostile(x) :- Enemy(x, America).

Own(Nono, B52).
Missile(B52).
American(West).
Enemy(Nono, America).
