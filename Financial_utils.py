## 1. Modularización y Funciones
precio_actual = float(input("Precio Actual: "))
precio_anterior = float(input("Precio Anterior: "))
def calculo_retorno(precio_actual: float,precio_anterior: float) -> float:
retorno = ((precio_actual - precio_anterior) / precio_anterior) * 100
print(f'El retorno es de:', retorno)
break

## 2. categorizar_volatilidad(desviacion_estandar):
def categorizar_volatilidad(desviacion_est):
if desviacion_est < 0.02:
    print("Baja")
elif desviacion_est >= 0.02 and desviacion_est <= 0.05:
    print("Media")
else:
    print("Alta")