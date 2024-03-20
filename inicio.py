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
    print(fila) # Imprimimos cada fila de la matriz
# Implementación del método de eliminación de Gauss con pivoteo parcial escalado
n = len(matriz)  # Obtener el tamaño de la matriz
for i in range(n): # Iterar sobre cada fila
    # Paso 1: Encontrar el pivote en la columna actual
    max_index = i # Índice de la fila con el pivote más grande
    max_value = abs(matriz[i][i]) # Valor del pivote más grande
    for k in range(i + 1, n): # Iterar sobre las filas debajo del pivote
        if abs(matriz[k][i]) > max_value: # Si encontramos un pivote más grande
            max_value = abs(matriz[k][i]) # Actualizar el valor del pivote más grande
            max_index = k # Actualizar el índice del pivote más grande       
    # Intercambiar filas si es necesario
    if max_index != i: # Si el pivote más grande no está en la fila actual
        matriz[i], matriz[max_index] = matriz[max_index], matriz[i] # Intercambiar las filas
        print(f"Intercambio de fila {i+1} con fila {max_index+1} (paso {i+1}):") # Imprimir el paso
        for fila in matriz: # Imprimir la matriz
            print([round(elem, 2) for elem in fila]) # Redondeamos los elementos de la fila a 2 decimales
    # Hacer ceros debajo del pivote en la columna actual
    pivot = matriz[i][i] # Obtener el valor del pivote
    for j in range(i + 1, n): # Iterar sobre las filas debajo del pivote
        factor = matriz[j][i] / pivot # Calcular el factor por el cual se va a multiplicar la fila
        for k in range(i, n): # Iterar sobre las columnas de la fila
            matriz[j][k] -= factor * matriz[i][k] # Restar el producto del factor por el pivote y la fila superior
    print(f"Paso {i+1}:") # Imprimir el paso
    for fila in matriz:
          print([round(elem, 2) for elem in fila])  # Redondeamos los elementos de la fila a 2 decimales