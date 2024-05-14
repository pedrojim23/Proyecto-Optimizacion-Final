import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

def iniciar_busqueda(conjunto_str, objetivo_str):
    conjunto = list(map(int, conjunto_str.split()))
    objetivo = int(objetivo_str)
    
    def backtrack(subconjunto, index, suma_actual, historial_sumas, text_box):
        historial_sumas.append(suma_actual)
        plt.plot(historial_sumas, marker='o', linestyle='-')
        plt.xlabel('Pasos')
        plt.ylabel('Suma Actual')
        plt.title('Búsqueda de Subconjuntos')
        plt.grid(True)
        
        # Mostrar la salida en una ventana de texto en el gráfico
        text_box.set_text("Explorando: {}\nSuma actual: {}\nComparación: {}".format(subconjunto, suma_actual, "igual" if suma_actual == objetivo else "mayor" if suma_actual > objetivo else "menor"))

        plt.pause(0.5)  # Pausa para mostrar el gráfico

        if suma_actual == objetivo:
            print("Solución encontrada:", subconjunto)
            plt.show()  # Mostrar la ventana de Matplotlib al encontrar la solución
            return True
        if suma_actual > objetivo or index >= len(conjunto):
            return False

        # Animación
        if backtrack(subconjunto + [conjunto[index]], index + 1, suma_actual + conjunto[index], historial_sumas, text_box):
            return True
        if backtrack(subconjunto, index + 1, suma_actual, historial_sumas, text_box):
            return True
        return False

    print("Iniciando búsqueda de subconjuntos...")
    
    fig, ax = plt.subplots()
    text_box = ax.text(0.02, 0.85, "", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
    
    if not backtrack([], 0, 0, [], text_box):
        print("No se encontraron subconjuntos cuya suma sea igual al valor objetivo.")
    
    text_box.remove()  # Remover la ventana de texto al finalizar

def ingresar_numeros():
    ventana = Tk()
    ventana.title("Ingresar números del conjunto y valor objetivo")
    
    label_conjunto = Label(ventana, text="Ingrese los números del conjunto separados por espacios:")
    label_conjunto.pack()
    entry_conjunto = Entry(ventana, width=50)
    entry_conjunto.pack()

    label_objetivo = Label(ventana, text="Ingrese el valor objetivo:")
    label_objetivo.pack()
    entry_objetivo = Entry(ventana)
    entry_objetivo.pack()

    button_buscar = Button(ventana, text="Iniciar Búsqueda", command=lambda: iniciar_busqueda(entry_conjunto.get(), entry_objetivo.get()))
    button_buscar.pack()

    ventana.mainloop()

# Ejemplo de uso
ingresar_numeros()
