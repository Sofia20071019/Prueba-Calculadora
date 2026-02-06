# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el IMC"""
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

# Programa principal
if __name__ == "__main__":

    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))

    imc = calcularIMC(peso, altura)

    print("\nResultados:")
    print("IMC:", round(imc, 2))
    print("Clasificación:", clasificarIMC(imc))