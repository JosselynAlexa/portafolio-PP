:- dynamic estado/3.

estado(mono_piso, caja_esquina, banana_centro).

puede_agarrar :-
    estado(mono_sobre_caja, caja_centro, banana_centro).

mover(mono, piso, caja, centro).
mover(caja, esquina, centro).
subir(mono, caja).