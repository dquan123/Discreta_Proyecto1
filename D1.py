"""
# MM2015 - Desafío de programación 1: Lógica proposicional
# Autores: Diego Quan, Joel Nerio, Miguel Rosas, Arodi Chávez

# NOTA:
# Debe utilizar letras minúsculas para los nombres de las variables, por ejemplo, a, b, c.
# Puede utilizar paréntesis para agrupar expresiones, como «a and (b or c)».

# Implemente las cuatro funciones siguientes:
# tabla_verdad, tautologia, equivalentes e inferencia

# Entrega:
# Deberá subir este archivo a la página del curso en Canvas.
"""


######## No modifique el siguiente bloque de código ########
# ********************** COMIENZO *******************************

from functools import partial
import re


class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q) :
    return not p or q

@Infix
def iff(p, q) :
    return (p |implies| q) and (q |implies| p)

# Debe utilizar esta función para extraer variables.
# Esta función toma una expresión como entrada y devuelve una lista ordenada de variables.
# NO modifique esta función.

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set


# ********************** FIN *******************************

# Función que crea las combinaciones para todas las variables de la tabla de verdad
def generar_combinaciones(n):
    combinaciones = []
    total = 2 ** n
    for i in range(total):
        fila = []
        for bit in range(n):
            # Bit más significativo primero
            valor = bool((i >> (n - bit - 1)) & 1)
            fila.append(valor)
        combinaciones.append(fila)
    return combinaciones



############## IMPLEMENTAR LAS SIGUIENTES FUNCIONES  ##############
############## No modificar las definiciones de las funciones ##############

# Función: tabla_verdad
# Esta función calcula una tabla de verdad para una expresión dada.
# Entrada: expresión.
# Salida: tabla de verdad como una lista de listas.

def tabla_verdad(expr):
    vars = extract_variables(expr)
    n = len(vars)
    table = []
    for combo in generar_combinaciones(n):
        contexto = {var: val for var, val in zip(vars, combo)}
        try:
            resultado = eval(expr, {"implies": implies, "iff": iff}, contexto)
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {e}")
        table.append(combo + [resultado])
    return table

# Función: tautologia
# Esta función determina si la expresión es una tautología, devuelve True;
# en caso contrario, devuelve False.
# Entrada: expresión.
# Salida: booleano.
def tautologia(expr):
    tabla = tabla_verdad(expr)
    
    # El último valor de cada fila es el resultado de la expresión
    for fila in tabla:
        if not fila[-1]:
            return False
    return True

# Función: equivalentes
# Esta función determina si expr1 es equivalente a expr2, devuelve True;
# en caso contrario, devuelve False.
# Entrada: expresión 1 y expresión 2.
# Salida: booleano.
def equivalentes(expr1, expr2):
    pass

# Función: inferencia
# Esta función determina los valores de verdad para una valuación de una proposición dada.
# Entrada: expresión.
# Salida: lista de listas.

def inferencia(expr):
    pass



##Función que contiene el menú de opciones
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Tabla de verdad")
        print("2. Verificar tautología")
        print("3. Verificar equivalencias")
        print("4. Realizar inferencia")
        print("5. Finalizar")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            expr = input("Ingrese la proposición: ").strip()
            try:
                tabla = tabla_verdad(expr)
                print("\nTabla de verdad:")
                for fila in tabla:
                    print(fila)
            except Exception as e:
                print("Error:", e)

        elif opcion == "2":
            expr = input("Ingrese la proposición: ").strip()
            try:
                print("Es tautología?:", tautologia(expr))
            except Exception as e:
                print("Error:", e)

        elif opcion == "3":
            expr1 = input("Ingrese la primera proposición: ").strip()
            expr2 = input("Ingrese la segunda proposición: ").strip()
            try:
                print("Son equivalentes?:", equivalentes(expr1, expr2))
            except Exception as e:
                print("Error:", e)

        elif opcion == "4":
            expr = input("Ingrese la proposición con formato 'expr = 0/1': ").strip()
            try:
                resultados = inferencia(expr)
                print("Asignaciones que cumplen la condición:")
                for fila in resultados:
                    print(fila)
            except Exception as e:
                print("Error:", e)

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
