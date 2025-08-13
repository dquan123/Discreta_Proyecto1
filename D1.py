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
    """Soporte de operadores infijos para implies e iff."""
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q):
    """Implica: p → q es equivalente a (¬p) ∨ q."""
    return not p or q

@Infix
def iff(p, q):
    """Doble implicación: p ↔ q es (p → q) ∧ (q → p)."""
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
    """
        Genera todas las combinaciones booleanas para n variables en orden binario convencional.

        Parámetros
        ————
        n: int
            Cantidad de variables proposicionales.

        Retorna
        ————
        list[list[bool]]
            Lista de filas, donde cada fila es una asignación [v1, v2, ..., vn] con valores True/False.
            El orden es MSB primero: 00...0, 00...1, ..., 11...1.
    """
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
def tabla_verdad(expr):
    """
        Genera la tabla de verdad de una expresión proposicional.

        Parámetros
        ----------
        expr : str
            Expresión en términos de variables a–z y operadores (not, and, or, |implies|, |iff|).

        Retorna
        -------
        list[list[bool]]
            Si hay n variables, cada fila tiene n + 1 elementos:
            los n primeros son la asignación a las variables (en orden ascendente),
            y el último es el valor de la fórmula bajo dicha asignación.

        Lanza
        -----
        ValueError
            Si la expresión no se puede evaluar (p. ej., sintaxis inválida o variable no permitida).
    """
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
def tautologia(expr):
    """
        Determina si una expresión es tautología (siempre verdadera).

        Parámetros
        ----------
        expr : str
            Expresión proposicional.

        Retorna
        -------
        bool
            True si todas las valuaciones producen True; False en caso contrario.

        Lanza
        -----
        ValueError
            Si la expresión no se puede evaluar.
    """
    tabla = tabla_verdad(expr)
    
    # El último valor de cada fila es el resultado de la expresión
    for fila in tabla:
        if not fila[-1]:
            return False
    return True

# Función: equivalentes
def equivalentes(expr1, expr2):
    """
        Verifica equivalencia lógica entre dos expresiones.

        Parámetros
        ----------
        expr1 : str
            Primera expresión.
        expr2 : str
            Segunda expresión.

        Retorna
        -------
        bool
            True si ambas expresiones tienen el mismo valor para todas las asignaciones
            de sus variables; False en caso contrario. Si las variables no coinciden exactamente,
            retorna False.

        Lanza
        -----
        ValueError
            Si alguna expresión no se puede evaluar.
    """
    # Extraer y comparar conjuntos de variables
    vars1 = extract_variables(expr1)
    vars2 = extract_variables(expr2)
    # Si no tienen exactamente las mismas variables, no se consideran equivalentes
    if vars1 != vars2:
        return False
    vars = vars1
    n = len(vars)
    for combo in generar_combinaciones(n):
        contexto = {var: val for var, val in zip(vars, combo)}
        try:
            r1 = bool(eval(expr1, {"implies": implies, "iff": iff}, contexto))
            r2 = bool(eval(expr2, {"implies": implies, "iff": iff}, contexto))
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {e}")
        if r1 != r2:
            return False
    return True




#función de inferencia.
def inferencia(expr):
    """
        Obtiene las asignaciones que satisfacen una igualdad de verdad.

        Formato de entrada: "<proposición> = <0|1>"

        Parámetros
        ----------
        expr : str
            Proposición seguida de '=', y al final 0 (falso) o 1 (verdadero).

        Retorna
        -------
        list[list[bool]]
            Lista de asignaciones (cada una con n valores True/False) que cumplen la igualdad.
            Si ninguna la cumple, retorna [].

        Lanza
        -----
        ValueError
            Si no hay exactamente un '=', si el valor esperado no es 0/1,
            o si la expresión es inválida.
    """
    # Verificar formato
    if "=" not in expr:
        raise ValueError("La proposición debe contener '=' seguido de 0 o 1.")
    izquierda, derecha = expr.split("=")
    izquierda = izquierda.strip()
    derecha = derecha.strip()

    # Validar valor esperado
    if derecha not in ("0", "1"):
        raise ValueError("El valor a la derecha de '=' debe ser 0 o 1.")

    valor_esperado = True if derecha == "1" else False

    # Obtener variables de la parte izquierda
    vars = extract_variables(izquierda)
    n = len(vars)
    resultados = []

    # Probar todas las combinaciones posibles
    for combo in generar_combinaciones(n):
        contexto = {var: val for var, val in zip(vars, combo)}
        try:
            resultado = bool(eval(izquierda, {"implies": implies, "iff": iff}, contexto))
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {e}")

        # Guardar las que cumplen la igualdad
        if resultado == valor_esperado:
            resultados.append(combo)

    return resultados
    



def menu():
    """
       Despliega el menú principal y coordina las operaciones interactivas del programa.
    """
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
