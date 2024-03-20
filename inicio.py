print("Algebra y matematicas discretas")
print("Bienvenido al curso, este es el ejercicio de pivotaje parcial escalado")
print("Se definira una matriz de 4x4 y se realizara el pivoteo parcial escalado, por lo tanto se te solicitaran los datos de la matriz")
# Inicializamos la matriz
matriz = []
# Inicializamos el contador de cadenas válidas
contador = 0
while contador < 4:
    # Solicitamos al usuario que ingrese los números separados por comas
    numeros = input(f"Ingrese la cadena de números {contador+1} separados por el signo , :")
    # Verificamos que todos los caracteres sean dígitos o comas
    if all(caracter.isdigit() or caracter == ',' for caracter in numeros):
        # Verificamos que no haya más de cuatro números
        if numeros.count(',') < 4:
            # Convertimos la cadena de texto a una lista de enteros
            fila = list(map(int, numeros.split(',')))
            # Agregamos la fila a la matriz
            matriz.append(fila)
            print(f"Cadena {contador+1}: {numeros}")
            contador += 1
        else:
            print("La matriz no soporta la cantidad de datos ya que es de 4x4, por favor ingrese una cantidad válida.")
    else:
        print("Valores no numéricos o separador no reconocido, por favor digita solo números separados por el signo ,")
# Imprimimos la matriz
for fila in matriz:
    print(fila)
# Implementación del método de eliminación de Gauss con pivoteo parcial escalado
n = len(matriz)  # Obtener el tamaño de la matriz
for i in range(n):
    # Paso 1: Encontrar el pivote en la columna actual
    max_index = i
    max_value = abs(matriz[i][i])
    for k in range(i + 1, n):
        if abs(matriz[k][i]) > max_value:
            max_value = abs(matriz[k][i])
            max_index = k
    
    # Intercambiar filas si es necesario
    if max_index != i:
        matriz[i], matriz[max_index] = matriz[max_index], matriz[i]
        print(f"Intercambio de fila {i+1} con fila {max_index+1} (paso {i+1}):")
        for fila in matriz:
          print([round(elem, 2) for elem in fila]) 

    # Hacer ceros debajo del pivote en la columna actual
    pivot = matriz[i][i]
    for j in range(i + 1, n):
        factor = matriz[j][i] / pivot
        for k in range(i, n):
            matriz[j][k] -= factor * matriz[i][k]
    print(f"Paso {i+1}:")
    for fila in matriz:
          print([round(elem, 2) for elem in fila])  # Redondeamos los elementos de la fila a 2 decimales