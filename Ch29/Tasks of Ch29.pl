/*task 29.01*/
capitalCity(paris).
capitalCity(berlin).
capitalCity(cairo).

/*task 29.03*/
male(carl).
female(nick).
parent(carl,nick).
father(F,C):- male(F), parent(F,C).

/*29.04*/
parent(Ken,Jack).
parent(Carl,Nick).
parent(Jack,Carl).

ancestor(A,B):- parent(A,B).
ancestor(A,B):- parent(A,X), ancestor(X,B).

/*29.05*/
factorial(0,1).
even(X):- 0 is mod(X,2).
odd(X) :- not(even(X)).

factorial(N,F) :-
	X is N - 1,
	factorial(X,Y),
	F is N*Y.

/*29.06*/
writeList([lenovo, apple, dell]).
writeList([H|T]):- writeList(H),n1,writeList(T).







