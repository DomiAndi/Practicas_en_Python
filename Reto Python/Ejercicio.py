# Variables | Ingresar Datos.
numero_Inicial = int(input('Número Inicial: '))
numero_Final = int(input('Número Final: '))
numero_Final = + 1

c_Positivos = 0
c_Negativos = 0

for numero in range(numero_Inicial, numero_Final):
    if numero % 2 == 0:
        c_Positivos + 1
    else:
        c_Negativos += 1

print('Positivos: ', c_Positivos)
print('Negativos: ', c_Negativos)