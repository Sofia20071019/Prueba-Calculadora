# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""
    return peso / (altura * altura)

def calcular_masa_corporal(peso, altura):
    """Calcula la masa corporal utilizando la fórmula: masa = peso / (altura ** 2)"""

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


def calcular_calorias_a_delgazar(peso_actual, peso_objetivo, dias):
    """Calcula las calorías diarias segun el nivel de actividad y resta las calorias para adelgazar."""

if __name__ == "__main__":

    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    sexo = input("Ingrese su sexo (hombre/mujer): ")

    imc = calcularIMC(peso, altura)
    tmb = calcular_TMB(peso, altura, edad, sexo)

    print("\nResultados:")
    print("IMC:", round(imc, 2))
    print("TMB:", round(tmb, 2))