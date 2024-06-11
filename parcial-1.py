# Primer Parcial Algoritmos y Estructuras de Datos

# 1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos. 




# 1)

def listar_inversa(lista):
    if len(lista) == 0 :
        return (0)
    else:
        print(lista[-1])
        return(listar_inversa(lista[:-1]))


lista_numero = [1, 2, 3, 4, 5]
print(listar_inversa(lista_numero))


