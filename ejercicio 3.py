
monedas_iniciales = [1,2,4,7]

def cambio_no_posible(monedas_lista):
   
    monedas_lista.sort()          # pista 1: ordenar las monedas en orden ascendente
    cambio = 0                    # cambio posible inicializado en 0
    
    for moneda in monedas_lista:  # recorrer los componentes de la modedas_lista
       
        if moneda > cambio + 1:   # si la moneda actual es mayor a la sumatoria de cambio +1, el siguiente numero no se puede hacer
            break                 # entonces aparece el primer numero que no se puede hacer
        else: 
         cambio += moneda         # sino, se puede seguir sumando al cambio acumulado
     
    return cambio + 1             # si se han revisado todas las monedas, el primer cambio que no se puede hacer es el acumulado más 1

primer_cambio_no_posible = cambio_no_posible(monedas_iniciales)
print(monedas_iniciales, "-->",primer_cambio_no_posible)
 