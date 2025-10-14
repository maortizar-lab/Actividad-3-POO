import tkinter as tk
from tkinter import messagebox
import statistics

#Función para validar solo números
def validar_numero(texto):
    # Permite vacío (para borrar) o números decimales
    if texto == "" or texto.replace(".", "", 1).isdigit():
        return True
    return False

#Función para calcular resultados
def calcular():
    try:
        # Convertir entradas a flotantes (solo las no vacías)
        notas = [float(entry.get()) for entry in entradas if entry.get() != ""]
        if len(notas) < 1:
            messagebox.showerror("Error", "Debe ingresar al menos una nota.")
            return
        
        # Cálculos estadísticos
        promedio = sum(notas) / len(notas)
        desviacion = statistics.pstdev(notas)
        mayor = max(notas)
        menor = min(notas)
        
        # Mostrar resultados
        resultado_texto.set(
            f"Promedio: {promedio:.2f}\n"
            f"Desviación estándar: {desviacion:.2f}\n"
            f"Nota mayor: {mayor}\n"
            f"Nota menor: {menor}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese solo números válidos.")

#Función para borrar todo
def borrar():
    for entry in entradas:
        entry.delete(0, tk.END)
    resultado_texto.set("")

#Ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Notas (solo números)")
ventana.geometry("350x400")
ventana.config(bg="#EAF2F8")

validar = ventana.register(validar_numero)

entradas = []
for i in range(5):
    tk.Label(ventana, text=f"Nota {i+1}:", bg="#EAF2F8", font=("Arial", 11, "bold")).pack()
    entry = tk.Entry(ventana, justify="center", validate="key", validatecommand=(validar, "%P"))
    entry.pack(pady=3)
    entradas.append(entry)

#Botones
frame_botones = tk.Frame(ventana, bg="#EAF2F8")
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Calcular", bg="#5DADE2", fg="white",
          width=10, command=calcular).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Borrar", bg="#AAB7B8",
          width=10, command=borrar).grid(row=0, column=1, padx=5)

#Resultados
resultado_texto = tk.StringVar()
tk.Label(ventana, textvariable=resultado_texto, bg="#EAF2F8", justify="left",
         font=("Arial", 11)).pack(pady=15)

ventana.mainloop()
