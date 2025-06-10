# Función de ordenamiento usando Quicksort
def quick_sort(lista):
    # Si la lista es vacía o con un solo elemento retorna la lista
    if len(lista) <= 1:
        return lista
    else:
        # Selección del primer elemento como pivote
        pivote = lista[0]
        # Sublistas de elementos menores o iguales y mayores al pivote (ignorando mayúsculas/minúsculas)
        menores = [x for x in lista[1:] if x.lower() <= pivote.lower()]
        mayores = [x for x in lista[1:] if x.lower() > pivote.lower()]
        # Recursión para ordenar las sublistas
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Función de búsqueda usando Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    # Mientras el rango sea válido
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        # Comparaciones ignorando mayúsculas/minúsculas
        if lista[medio].lower() == objetivo.lower():
            return medio
        elif lista[medio].lower() < objetivo.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    # Si no se encuentra el elemento
    return -1

# Programa principal
# Solicita la lista de palabras al usuario
entrada = input("Ingresa una lista de palabras separadas por comas: ")
# Divide las palabras y elimina espacios extras
lista_usuario = [palabra.strip() for palabra in entrada.split(',')]

# Solicita al usuario la palabra a buscar
palabra_a_buscar = input("Ingresa la palabra a buscar: ")

# Ordena la lista llamando a la función quick_sort
lista_ordenada = quick_sort(lista_usuario)
# Se muestra la lista ordenada
print("Lista ordenada:", lista_ordenada)

# Busca la palabra en la lista ordenada, llamando a la función busqueda_binaria
indice = busqueda_binaria(lista_ordenada, palabra_a_buscar)

# Muestra el resultado
if indice != -1:
    print(f"La palabra '{palabra_a_buscar}' fue encontrada en la posición {indice}.")
else:
    print(f"La palabra '{palabra_a_buscar}' no está en la lista.")
