# Corrección

01 --

El código 2 está mal la lógica, no funciona.
´´´
if wait == 0.2:
        wait = wait - 0.01
    elif wait == 0.05:
        wait = wait + 0.01
´´´
Solo va a restar o sumar uno cuando wait valga 0.2 y 0.05, no va a completar todo el rango.

El resto ok.

-----

Nota: (9)

