# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""
    return peso / (altura * altura)

def clasificarIMC(imc):
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    elif imc < 50:
        return "Obesidad tipo III (morbida)"
    else:
        return "Obesidad tipo IV (extrema)"

def calcular_TMB(peso, altura, edad, sexo):
    """Calcula la Tasa Basal Metabólica (TMB)"""

    altura_cm = altura * 100
    if sexo.lower() == 'hombre':
        TMB = 88.362 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * edad)
    elif sexo.lower() == 'mujer':
        TMB = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * edad)
    else:
        print("Sexo no reconocido. Use 'hombre' o 'mujer'.")
        TMB = 0

    return TMB

def calcular_porcentaje_masa_corporal(peso, altura_cm):
     """Calcular el porcentaje de la masa corporal."""

def calcular_calorias_a_delgazar(peso_actual, peso_objetivo, dias):
    """Calcula las calorías diarias segun el nivel de actividad y resta las calorias para adelgazar."""

# Programa principal
if __name__ == "__main__":

    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))

    imc = calcularIMC(peso, altura)

    print("\nResultados:")
    print("IMC:", round(imc, 2))
    print("Clasificación:", clasificarIMC(imc))

    edad = int(input("Ingrese su edad en años: "))
    sexo = input("Ingrese su sexo (hombre/mujer): ")

    tmb = calcular_TMB(peso, altura, edad, sexo)

    print("\nResultados:")
    print("TMB:", round(tmb, 2))
