# Calculadora de salud

def calcularIMC(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""
    return peso / (altura * altura)

def calcular_TMB(peso, altura, edad, sexo):
    """Calcula la Tasa Basal Metabólica (TMB)"""

def calcular_porcentaje_masa_corporal(peso, altura_cm):
     """Calcular el porcentaje de la masa corporal."""
     altura_m = altura_cm / 100
     imc = peso / (altura_m ** 2)
      
     return imc

def calcular_calorias_a_delgazar(peso_actual, peso_objetivo, dias):
    """Calcula las calorías diarias segun el nivel de actividad y resta las calorias para adelgazar."""

# Programa principal
if __name__ == "__main__":

    resultado = calcular_porcentaje_masa_corporal(peso, altura_cm)
    print(f"Tu índice de masa corporal es: {resultado:.2f}")

    print("\nResultados:")
    print("IMC:", round(imc, 2))
    print("Clasificación:", clasificarIMC(imc))
    print("TMB:", round(tmb, 2))
