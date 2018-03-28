/* facts */
dog(andy).
turtle(nick).
son(carl).
dog(jack).
dog(simon).
father(ken).

/* rules */

enemies(D1,D2) :- dog(D1) , turtle(D2).
sonOfFather(carl, ken).
sonOfFather(ken, nick).
sonOfFather(simon, ken).
sonOfFather(jack, ken).
sonOfFather(andy, ken).
grandparent(G,S) :- 
	sonOfFather(G,P), 
	sonOfFather(P,S).

brothers(A,B) :- 
	sonOfFather(A,C), 
	sonOfFather(B,C),
	not(A=B).

sister(X,Y) :-
	female(X),
	parent(Z,X),
	parent(Z,Y).


son(X,Y) :-
	male(X),
	parent(X,Y).

daughter(X,Y) :-
	female(X),
	parent(X,Y).

married(X,Y):-
	parent(X,Z),
	parent(Y,Z).

ingredient(tagine, aubergine, 250).
ingredient(tagine, tomato, 100).
ingredient(stew, beef, 400).
ingredient(stew, potato, 600).

