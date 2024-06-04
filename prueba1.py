
lista_inicial = [12, 34, 56, 61, 60, 78,5,60, 45]

def invertir_y_filtrar(lista):
    
    lista_invertida = lista[::-1]               # para invertir la lista usando rebanado de listas.
    res = []

    for numero in lista_invertida:
        
        str_numero = str(numero)             # convertir el número a una cadena para poder hacer cambios sobre sus dígitos
        nuevo_numero = ''
        
        for digito in str_numero:            # verificar cada dígito y construir el nuevo número
            if int(digito) < 6:              # si el digito es menor a 6 se conserva 
                nuevo_numero += digito
        
        nuevo_numero = int(nuevo_numero) if nuevo_numero else None # operador ternario, convierte a int si no es una cadena vacia
        
        if nuevo_numero is not None:         # agregar el nuevo número a la lista resultante solo si no es None
               # if nuevo_numero<100:
                    res.append(nuevo_numero)
    return res

lista_final = invertir_y_filtrar(lista_inicial)
print(lista_inicial,"-->",lista_final)