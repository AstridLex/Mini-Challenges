def orden_numeros():
    numeros_usuarios = input("Ingrese varios números separados por comas: ")
    lista_numeros = [float(numero.strip()) for numero in numeros_usuarios.split(",")]
    numeros_ordenados = sorted(lista_numeros)
    return numeros_ordenados

numeros_ordenados = orden_numeros()

print("Lista ordenada en orden ascendente:")
print(numeros_ordenados)
