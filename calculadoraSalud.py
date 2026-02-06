# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (altura * altura)

print("Su IMC es:", imc)

if imc < 16:
    print("Estas en delgadez severa")
elif imc < 17:
    print("Estas en delgadez moderada")
elif imc < 18.5:
    print("Estas en delgadez aceptable")
elif imc < 25:
    print("Estas en peso normal")
elif imc < 30:
    print("Estas en sobrepeso")
elif imc < 35:
    print("Estas en obesidad tipo I")
elif imc < 40:
    print("Estas en obesidad tipo II")
elif imc < 50:
    print("Estas en obesidad tipo III (morbida)")
else:
    print("Estas en obesidad tipo IV (extrema)")

def calcaularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""

def calcular_calorias_a_delgazar(peso_actual, peso_objetivo, dias):
    """Calcula las calorías diarias segun el nivel de actividad y resta las calorias para adelgazar."""

if __name__ == "__main__":

    print("\nResultados:")
    print("IMC:", imc)
    print("Masa corporal:", masa)
    print("Calorias para adelgazar: ", calorias)
