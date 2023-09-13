import numpy as np
import matplotlib.pyplot as plt

def create_histogram():
    opcion = input("Desea ingresar los datos? (S/N): ")
    if opcion == "s":
        data = input("Ingrese los datos separados por comas: ")
        try:
            data = [int(x) for x in data.split(",")]
        except ValueError:
            print("Error: Los datos deben ser números separados por comas.")
            return create_histogram()
    

    elif opcion == "N":
        data = np.random.randint(0, 100, 50)
    else:
        print("Error: Opción no válida.")
        return create_histogram()
    
    intervalo = max(data) / len(data)
    plt.hist(data, bins=np.arange(0, max(data) + intervalo, intervalo))
    plt.show()

create_histogram()