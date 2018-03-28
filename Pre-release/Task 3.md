#Ken Su

##Task 3

###3.1
```prolog
character(habib).
character_type(habib, explorer).
has_skill(habib, time_travel).
pet(habib, fish).
animal(fish).
skill(time_travel).
```

###3.2
```prolog
pet(X,Y) :-
	character(X),
	animal(Y).
```

###3.3

```prolog
character(carl).
character(nick).
character_type(carl,garbage_collector).
character_type(nick, politician).
has_skill(carl, bragging).
has_skill(nick, criticizing)
pet(carl,aepyornis).
pet(nick,amberjack).
animal(aepyornis).
animal(amberjack).
skill(bragging).
skill(criticizing).
```

###3.4

|true.|
|X = princess.|
|X = jim.|
|X = invisibility.|
|X = jim.|

###3.5
pet(jim,X).
has_skill(X,fly).
skill(X).
petofprincess(X) :- 
	pet(A,B), 
	character_type(A, princess).





	


