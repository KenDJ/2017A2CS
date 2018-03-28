/*coding bat recursion 1*/

/*factorial*/
even(X):- 0 is mod(X,2).
odd(X) :- not(even(X)).

factorial(0,1).
factorial(N,F) :-
	X is N - 1,
	factorial(X,Y),
	F is N*Y.


/*bunnyEars*/

bunnyEars(1,2).
bunnyEars(A,B) :-
	X is A - 1,
	bunnyEars(X,Y),
	B is Y*2.

/*fibonacci*/

fib(0,0).
fib(1,1).
fib(N,F) :-
	A is N - 1,
	B is N - 2,
	fib(A,C),
	fib(B,D),
	F is C + D.

/*length of list*/

len([],0).
len([_|T],L) :-
	len(T,X),
	L is X + 1.

mymember(I, [I|_]).
mymember(I, [_|T]) :-
	mymember(I,T).








