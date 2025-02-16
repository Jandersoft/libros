
==========
Ejercicios
==========

-----------------------
 *Tema 0:* Introducción
-----------------------

Repaso
======

1. Escribe una función que reciba dos listas y devuelva una lista con
   los productos de los elementos de esas listas.

   .. hint:: Itera sobre los índices y accede con ``operador []``

   `Solución <product.py.txt>`__

#. Escribe la función anterior, sin utilizar el
   ``operador []``
   
   .. hint:: Utiliza la función ``zip ()``

   .. hint:: Recuerda que en un bucle ``for`` se pueden
      desempaquetar tuplas: `` for a, b in ...``

   `Solución <product2.py.txt>`__

#. Compara el rendimiento de esta función con el de la solución con
   corchetes. ¿Cual de las dos es más rápida?
   
   .. hint:: Utilizar ``%timeit`` de *IPython*

   `Solución <product3.py.txt>`__

#. Escribe una función que reciba una frase y
   devuelva *un a pareja* de un `bool` indicando si la frase es
   palíndromo, y un diccionario que asocie a cada palabra de la frase si
   ella misma es palíndromo o no.

   .. hint:: Un palíndromo es una frase o una palabra que es
      igual leída hacia adelante o hacia atrás.

   .. hint:: Realizar la comprobación de si una secuencia es simétrica
      cualesquiera que sea el tipo de sus contenidos en una función a
      parte.

   `Solución <palindromo.py.txt>`__

Módulos y documentación
=======================

#. Crea un paquete `palin` que contenga la función del ejercicio
   anterior, con un módulo `liga.util` que contenga la función del
   ejercicio 2. Si no has hecho las funciones anteriores aún, haz una
   implementación vacía que haga::

      raise NotImplemented

   .. hint:: Recuerda que las funciones de un paquetes hay que
      ponerlas en el módulo especial ``__init__`` dentro del paquete.

   `Solución <palin.tar.gz>`__

#. Documenta las funciones anteriores. Comprueba el resultado con
   ``pydoc`` y desde la consola.

   `Solución <palin.tar.gz>`__

#. Escribe una función ``may_raise (objeto)`` que recibe como parámetro
   cualquier entidad del lenguaje devuelva ``True`` si devuelve
   excepciones o ``False`` si no basándose heurísticamente en lo que
   dice su documentación.

   .. hint:: Recuerda que puedes acceder a la documentación de un
      objeto a través de ``__doc__``.
   
   .. hint:: Puedes probar heurísticamente simplemente buscando la
      cadena ``:raise`` o ``@raise`` en el texto de la documentación.

   `Solución <mayraise.py.txt>`__

