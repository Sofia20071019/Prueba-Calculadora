# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""
    return peso / (altura * altura)

def calcular_TMB(peso, altura, edad, sexo):
    """Calcula la Tasa Basal Metabólica (TMB)"""

def calcular_porcentaje_masa_corporal(peso, altura_cm):
     """Calcular el porcentaje de la masa corporal."""

def calcular_calorias_a_delgazar(peso_actual, peso_objetivo, dias):
    """Calcula las calorías diarias segun el nivel de actividad y resta las calorias para adelgazar."""

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificacion_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def factor_actividad(nivel):
    if nivel == 1:
        return 1.2
    elif nivel == 2:
        return 1.375
    elif nivel == 3:
        return 1.55
    elif nivel == 4:
        return 1.725
    else:
        return 1.9

# Programa principal
if __name__ == "__main__":
    print("Calculardora")
    print("\nNivel de actividad física:")
    print("1. Sedentario")
    print("2. Ligero")
    print("3. Moderado")
    print("4. Activo")
    print("5. Muy activo")
    nivel = int(input("Seleccione una opción (1-5): "))

    print("\nResultados:")
    print("IMC:", round(imc, 2))
    print("Clasificación:", clasificacion_imc(imc))
    print("TMB:", round(tmb, 2))
    print(f"Calorías diarias recomendadas para adelgazar: {calcular_calorias_a_delgazar:.2f} kcal")
