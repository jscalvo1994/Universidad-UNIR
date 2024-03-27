print("Algebra y matematicas discretas")
print("Bienvenido al curso, este es el ejercicio de pivotaje parcial escalado")
print("Se definira una matriz de 4x4 y se realizara el pivoteo parcial escalado, por lo tanto se te solicitaran los datos de la matriz")
# Inicializamos la matriz
matriz = [] # Inicializamos la matriz vacía
# Inicializamos el contador de cadenas válidas
contador = 0 # Inicializamos el contador en 0
while contador < 4:
    # Solicitamos al usuario que ingrese los números separados por comas
    numeros = input(f"Ingrese la cadena de números {contador+1} separados por el signo , :") # Solicitamos al usuario que ingrese los números separados por comas
    # Verificamos que todos los caracteres sean dígitos o comas
    if all(caracter.isdigit() or caracter == ',' or caracter == '-'for caracter in numeros): # Verificamos que todos los caracteres sean dígitos o comas
        # Verificamos que no haya más de cuatro números
        if numeros.count(',') < 4:
            # Convertimos la cadena de texto a una lista de enteros
            fila = list(map(int, numeros.split(','))) # Convertimos la cadena a una lista de enteros
            # Agregamos la fila a la matriz
            matriz.append(fila)
            print(f"Cadena {contador+1}: {numeros}") # Imprimimos la cadena
            contador += 1 # Aumentamos el contador en 1
        else: # Si hay más de cuatro números
            print("La matriz no soporta la cantidad de datos ya que es de 4x4, por favor ingrese una cantidad válida.")
    else: # Si hay caracteres no numéricos o separadores no reconocidos
        print("Valores no numéricos o separador no reconocido, por favor digita solo números separados por el signo ,")
# Imprimimos la matriz
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
# Ordenamos las filas de la matriz en función del valor absoluto del primer elemento de cada fila
matriz.sort(key=lambda fila: abs(fila[0]), reverse=True)
print("Matriz ordenada de mayor a menor")
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
Str_matriz = [[str(elemento) for elemento in fila] for fila in matriz]
for fila in Str_matriz:
    print(fila) # Imprimimos cada fila de la matriz
print('inicio primer paso')
print('inicio primer paso')
# Tomamos el primer elemento de la primera fila
prim_elemento = matriz[0][0] if matriz[0][0] != 0 else 1
segu_elemento = matriz[1][0]
terc_elemento = matriz[2][0]
cuar_elemento= matriz[3][0]
Str_matriz[0] = [f"{elemento}/{prim_elemento}" if prim_elemento != 0 else "0" for elemento in matriz[0]]
# Iteramos sobre los elementos de Str_matriz[0]
for i in range(len(matriz[1])):
    Str_matriz[1][i] = f"{matriz[1][i]}-{segu_elemento}*({Str_matriz[0][i]})"
for i in range(len(matriz[1])):
    Str_matriz[2][i] = f"{matriz[2][i]}-{terc_elemento}*({Str_matriz[0][i]})"
for i in range(len(matriz[1])):
    Str_matriz[3][i] = f"{matriz[3][i]}-{cuar_elemento}*({Str_matriz[0][i]})"
matriz[0] = [elemento/prim_elemento if prim_elemento != 0 else 0 for elemento in matriz[0]]
# Iteramos sobre los elementos de Str_matriz[0]
for i in range(len(matriz[1])):
    matriz[1][i] = matriz[1][i]-segu_elemento*matriz[0][i]
for i in range(len(matriz[1])):
    matriz[2][i] = matriz[2][i]-terc_elemento*matriz[0][i]
for i in range(len(matriz[1])):
    matriz[3][i] = matriz[3][i]-cuar_elemento*matriz[0][i]
print('matriz detalle')
for fila in Str_matriz:
    print(fila) # Imprimimos cada fila de la matriz
# Iteramos sobre las filas de la matriz para limpiar los datos
for i in range(len(matriz)):
    # Verificamos si el primer elemento de la fila es '0.0'
    if matriz[i][0] == 0.0:
        # Si es '0.0', le asignamos el valor '0'
        matriz[i][0] = 0
        Str_matriz[i][0] = '0'
    else:
        # Si no es '0.0', no modificamos nada
        pass
print('matriz operada')
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
print('Fin del primer paso convertir los primeros elementos de la matriz en 0')
print('inicio segundo paso')

# Tomamos el segundo elemento de la segunda fila
segu_elemento = matriz[1][1] if matriz[1][1] != 0 else 1
terc_elemento = matriz[2][1]
cuar_elemento= matriz[3][1]
Str_matriz[1] = [f"{elemento}/{segu_elemento}" if segu_elemento != 0 else "0" for elemento in matriz[1]]
# Iteramos sobre los elementos de Str_matriz[1]
for i in range(len(matriz[1])):
    Str_matriz[2][i] = f"{matriz[2][i]}-{terc_elemento}*({Str_matriz[1][i]})"
for i in range(len(matriz[1])):
    Str_matriz[3][i] = f"{matriz[3][i]}-{cuar_elemento}*({Str_matriz[1][i]})"
matriz[1] = [elemento/segu_elemento if segu_elemento != 0 else 0 for elemento in matriz[1]]
# Iteramos sobre los elementos de Str_matriz[1]
for i in range(len(matriz[1])):
    matriz[2][i] = matriz[2][i]-terc_elemento*matriz[1][i]
for i in range(len(matriz[1])):
    matriz[3][i] = matriz[3][i]-cuar_elemento*matriz[1][i]
print('matriz detalle')
for fila in Str_matriz:
    print(fila) # Imprimimos cada fila de la matriz
# Iteramos sobre las filas de la matriz para limpiar los datos
for i in range(len(matriz)):
    # Verificamos si el segundo elemento de la fila es '0.0'
    if matriz[i][1] == 0.0:
        # Si es '0.0', le asignamos el valor '0'
        matriz[i][1] = 0
        Str_matriz[i][1] = '0'
    else:
        # Si no es '0.0', no modificamos nada
        pass
print('matriz operada')
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
print('Fin del segundo paso convertir los segundos elementos de la matriz en 0')
print('inicio tercer paso')

# Tomamos el tercer elemento de la tercera fila
terc_elemento = matriz[2][2] if matriz[2][2] != 0 else 1
cuar_elemento= matriz[3][2]
Str_matriz[2] = [f"{elemento}/{terc_elemento}" if terc_elemento != 0 else "0" for elemento in matriz[2]]
# Iteramos sobre los elementos de Str_matriz[2]
for i in range(len(matriz[1])):
    Str_matriz[3][i] = f"{matriz[3][i]}-{cuar_elemento}*({Str_matriz[2][i]})"
matriz[2] = [elemento/terc_elemento if terc_elemento != 0 else 0 for elemento in matriz[2]]
# Iteramos sobre los elementos de Str_matriz[2]
for i in range(len(matriz[1])):
    matriz[3][i] = matriz[3][i]-cuar_elemento*matriz[2][i]
print('matriz detalle')
for fila in Str_matriz:
    print(fila) # Imprimimos cada fila de la matriz
# Iteramos sobre las filas de la matriz para limpiar los datos
for i in range(len(matriz)):
    # Verificamos si el tercer elemento de la fila es '0.0'
    if matriz[i][2] == 0.0:
        # Si es '0.0', le asignamos el valor '0'
        matriz[i][2] = 0
        Str_matriz[i][2] = '0'
    else:
        # Si no es '0.0', no modificamos nada
        pass
print('matriz operada')
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
print('Fin del tercer paso convertir los terceros elementos de la matriz en 0')
print('inicio cuarto paso')

# Tomamos el cuarto elemento de la cuarta fila
cuar_elemento= matriz[3][3] if matriz[3][3] != 0 else 1
Str_matriz[3] = [f"{elemento}/{cuar_elemento}" if cuar_elemento != 0 else "0" for elemento in matriz[3]]
matriz[3] = [elemento/cuar_elemento if cuar_elemento != 0 else 0 for elemento in matriz[3]]
print('matriz detalle')
for fila in Str_matriz:
    print(fila) # Imprimimos cada fila de la matriz
# Iteramos sobre las filas de la matriz para limpiar los datos
for i in range(len(matriz)):
    # Verificamos si el cuarto elemento de la fila es '0.0'
    if matriz[i][3] == 0.0:
        # Si es '0.0', le asignamos el valor '0'
        matriz[i][3] = 0
        Str_matriz[i][3] = '0'
    else:
        # Si no es '0.0', no modificamos nada
        pass
print('matriz operada')
for fila in matriz:
    print(fila) # Imprimimos cada fila de la matriz
print('Fin del cuarto paso convertir los cuartos elementos de la matriz en 0')

