padre(juan, maria).
padre(juan, pedro).
madre(ana, maria).
madre(ana, pedro).

hermano(X,Y) :-
    padre(P,X),
    padre(P,Y),
    X \= Y.

animal(perro).
animal(gato).
animal(pajaro).

vuela(pajaro).

mamifero(X) :-
    animal(X),
    X \= pajaro.

par(X) :-
    0 is X mod 2.

impar(X) :-
    1 is X mod 2.