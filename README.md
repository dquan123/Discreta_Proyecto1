MM2015 - Desafío de programación 1: Lógica Proposicional
Autores: Diego Quan, Joel Nerio, Miguel Rosas, Arodi Chávez
Descripción
Este programa implementa un sistema para trabajar con lógica proposicional, permitiendo generar tablas de verdad, verificar tautologías, comprobar equivalencias lógicas y realizar inferencias.

-->Sintaxis soportada
    Algunos delos Operadores básicos que se implementaron en este programa son los siguientes:

        and - Conjunción lógica (∧)
        or - Disyunción lógica (∨)
        not - Negación lógica (¬)
        |implies| - Implicación lógica (→)
        |iff| - Bicondicional lógica (↔)


--> Variables
    Para las variables es necesario utilizar únicamente letras minúsculas (a, b, c, d, etc.).
    Por cierto es importante mencionar que se pueden usar paréntesis para agrupar expresiones.


--> Ejemplos de la sintaxis Valida para el uso correcto de este project.

    a and b
    a or b
    not a
    a |implies| b
    a |iff| b
    (a and b) or (c and not d)


--> Funciones implementadas

    1. Tabla de Verdad( tabla_verdad(expr: str) -> list[list[bool]] )
        a.Esta funcion como tal genera la tabla de verdad completa para una proposición dada.
        b. Ejemplo de uso: 
            Entrada: tabla_verdad('a and b')
            Salida: [[False, False, False], [False, True, False], [True, False, False], [True, True, True]]
    
    2.Verificar Tautologia( tautologia(expr: str) -> bool )
        a. Esta funcion determina si una proposición es una tautología (siempre verdadera).
        b.Ejemplo de uso:

            tautologia('(a and b) |implies| a')  # True
            tautologia('p |iff| q')              # False

    3. Verificar equivalencias( equivalentes(expr1: str, expr2: str) -> bool  )
        a. esta funcion comprueba si dos proposiciones son lógicamente equivalentes.
        b. Ejemplo de uso:
            equivalentes('not (a and b)', 'not a and not b')  # False (Ley de De Morgan incorrecta)
            equivalentes('p |implies| q', 'not p or q')       # True

    4. Realizar inferencia( inferencia(expr: str) -> list[list[bool]] )
        a. esta funcion encuentra todas las asignaciones de valores de verdad que satisfacen una igualdad dada.
        b. Tiene que tener el siguiente formato de entrada: 'proposición = 0' ó 'proposición = 1'
        c. Ejemplo de uso: 
            inferencia('a or b = 1')        # [[False, True], [True, False], [True, True]]
            inferencia('a |implies| b = 0') # [[True, False]]
            inferencia('a and not a = 1')   # [] (lista vacía - contradicción)




--> Ejecución del Programa
    a.Para la correcta ejecución de este programa se puede desde la termina correr el siguiente command "python D1.py"
    b. al correr el programa se mostrara un menu interactivo en el que se te presentaran algunas opciones como por ejemplo:

        --- MENÚ PRINCIPAL ---
        1. Tabla de verdad
        2. Verificar tautología  
        3. Verificar equivalencias
        4. Realizar inferencia
        5. Finalizar

--> Visualización de opciones Propias del Programa 

    1. Tabla de Verdad
        a. se mostrara en la terminal algo como esto:

            Seleccione una opción (1-5): 1
            Ingrese la proposición: a and b

            Tabla de verdad:
            [False, False, False]
            [False, True, False]
            [True, False, False]
            [True, True, True]
    
    2.Verificar tautología
        a. se mostrara en la terminal algo como esto:

            Seleccione una opción (1-5): 2
            Ingrese la proposición: a or not a
            Es tautología?: True

    3.Verificar equivalencias
        a. se mostrara en la terminal algo como esto:

            Seleccione una opción (1-5): 3
            Ingrese la primera proposición: p |implies| q
            Ingrese la segunda proposición: not p or q
            Son equivalentes?: True

    4.Realizar inferencia
        a. se mostrara en la terminal algo como esto:

            Seleccione una opción (1-5): 4
            Ingrese la proposición con formato 'expr = 0/1': a and b = 1
            Asignaciones que cumplen la condición:
            [True, True]


--> Restricciones (IMPORTANTE)

    1. Variables: Solo se aceptan variables con nombres de letras minúsculas (a-z)
    2. Formato de inferencia: Debe incluir exactamente un operador = seguido de 0 o 1
    3. Paréntesis: Se pueden usar para agrupar expresiones complejas
    4. Mayúsculas: No se aceptan variables con nombres que contengan mayúsculas, dígitos o símbolos especiales



--> Manejo de Errores

    Como tal este programa  incluye manejo de errores(segun Restricciones) para:

        1. Expresiones con sintaxis inválidas
        2. Variables con nombres incorrectos 
        3. Formato incorrecto en inferencias
        4. Errores de evaluación de expresiones