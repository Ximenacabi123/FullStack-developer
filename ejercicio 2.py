import numpy as np
# lista inicial
numeros_iniciales = [-9,-5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7,8,9]

def ordenar_cuadrados(num):
    
    array1 = np.array(num)                          #convertir la lista a un array de numpy
    cuadrados = np.square(array1)                   #calcular los cuadrados de los números en el array
    rango = (cuadrados >= 0) & (cuadrados <= 66)    #definir rango [0, 66]
    array_rango = cuadrados[rango]
                                                      
    def ordenar_menor_mayor(array):                 #ordenar de menor a mayor

        for i in range(1, len(array)):              #recorre por posiciones el array = array_rango  
            valor_actual = array[i]
            posicion = i
            
            while posicion > 0 and array[posicion - 1] > valor_actual: #mover los elementos mayores que valor_actual una posición hacia adelante
            #       1      > 0 and    21               > 15      
                array[posicion] = array[posicion - 1]
                posicion -= 1
            
            array[posicion] = valor_actual           #colocar el valor_actual en su posición nueva
        return array
    
    ordenado = ordenar_menor_mayor(array_rango)
    return ordenado

#llamar funcion principal e imprimir
array_final = ordenar_cuadrados(numeros_iniciales)
print(array_final)