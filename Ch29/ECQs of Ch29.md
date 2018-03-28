#Ken Su

## Ch29 ECQs

### 
1.a i 

```prolog
cityIn(london, uk).
```

### 
1.a ii

```prolog
iVisited(strasbourg).
```

### 
1.b

chile, argentuna.


### 
1.c 

```prolog
countriesIVisited(Country) IF cityIn(City, Country) AND iVisited(City).
```

### 
2.a i

Emma has license.


### 
2.a ii


```prolog
allowedToDrive(X, V)
	IF hasLicense(X) AND minimumAge(V, L)
		AND age(X, A)
		AND A >= L.
```

### 
2.b i

Who = jack



### 
2.b ii

false

### 
2.b iii

false



### 
2.c i

```prolog
qualifiedCarDrivers(T) IF qualifiedDriver(T, car).
```



### 
2.c ii
```prolog
partQualified(X)IF passedTheoryTest(X) AND NOT passedDrivingTest(X, _).
```

### 
2.d

Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A
as 17), clause 15 ( A >= L is false) result is false.