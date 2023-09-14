import numpy as np
import matplotlib.pyplot as plt

def create_histogram():
    opcion = input("Desea ingresar los datos? (S/N): ") #imprime(1)asigna(1)
    if opcion == "S":                                    #compara(1)
        data = input("Ingrese los datos separados por comas: ") #imprime(1)asigna(1)
        try:           #compara(1)
            data = [int(x) for x in data.split(",")]     ·#asigna(1)convertidor(1)*for(N)* compara(1)divide(1) 4n
        except ValueError:                                #excepcion(1)
            print("Error: Los datos deben ser números separados por comas.")#imprime(1)
            return create_histogram()                      #return(1) devuelve(1)
    

    elif opcion == "N":                                    #compara(1)
        data = np.random.randint(0, 100, 50)                #repeticviones(N)en este caso 50
    else:                                                    #sino(1)
        print("Error: Opción no válida.")                    #imprime(1)     
        return create_histogram()                            #return(1)creeate(1)
    
    intervalo = max(data) / len(data)                        #asigna(1)pidevalormax(1)pidelongitud(1)divide(1)
    plt.hist(data, bins=np.arange(0, max(data) + intervalo, intervalo)) #llama a la funcion
    plt.show()

create_histogram() 
