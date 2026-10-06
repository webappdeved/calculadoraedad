# Materia: Laboratorio de Programación (LPR)
# Archivo: CalculadoraEdad.py
# Resolución de la Actividad 1 - Entorno Python


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def es_fecha_valida(d, m, a):
    if a < 1900 or a > 2026:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > 31:
        return False
    if m in [4, 6, 9, 11] and d > 30:
        return False
    if m == 2:
        if es_bisiesto(a):
            if d > 29:
                return False
        else:
            if d > 28:
                return False
    return True


# Código principal
print("=====================================================")
print("  CALCULADORA DE EDAD - VERSION EN PYTHON")
print("=====================================================")

try:
    diaN = int(input("Ingrese Dia de nacimiento: "))
    mesN = int(input("Ingrese Mes de nacimiento: "))
    anioN = int(input("Ingrese Anio de nacimiento: "))

    diaA, mesA, anioA = 8, 7, 2026

    if not es_fecha_valida(diaN, mesN, anioN):
        print("[ERROR] La fecha ingresada no es valida.")
    else:
        edad = anioA - anioN

        # RESOLUCIÓN: Ajuste si aún no cumplió años en el año actual
        if mesA < mesN or (mesA == mesN and diaA < diaN):
            edad -= 1

        print(f"\n[SISTEMA] Fecha de hoy: {diaA}/{mesA}/{anioA}")
        print(f"[SISTEMA] Edad calculada: {edad} anos.")

except ValueError:
    print("[ERROR] Deben ingresar numeros enteros.")
