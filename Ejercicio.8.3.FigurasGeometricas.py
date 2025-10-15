import tkinter as tk
from tkinter import messagebox

#FUNCIONES DE CALCULO
import math

def calcular_cilindro(radio, altura):
    volumen = math.pi * radio**2 * altura
    superficie = 2 * math.pi * radio * (radio + altura)
    return volumen, superficie

def calcular_esfera(radio):
    volumen = (4/3) * math.pi * radio**3
    superficie = 4 * math.pi * radio**2
    return volumen, superficie

def calcular_piramide(base, altura, apotema):
    volumen = (1/3) * base**2 * altura
    superficie = base**2 + 2 * base * apotema
    return volumen, superficie


#INTERFAZ PARA CADA FIGURA
def ventana_cilindro():
    sub = tk.Toplevel()
    sub.title("Cilindro")
    sub.config(bg="#E3F2FD")
    sub.geometry("300x280")

    tk.Label(sub, text="Radio (cm):", bg="#E3F2FD", font=("Arial", 11)).pack(pady=5)
    radio = tk.Entry(sub)
    radio.pack()

    tk.Label(sub, text="Altura (cm):", bg="#E3F2FD", font=("Arial", 11)).pack(pady=5)
    altura = tk.Entry(sub)
    altura.pack()

    resultado = tk.Label(sub, text="", bg="#E3F2FD", font=("Arial", 11))
    resultado.pack(pady=10)

    def calcular():
        try:
            r = float(radio.get())
            h = float(altura.get())
            v, s = calcular_cilindro(r, h)
            resultado.config(text=f"Volumen (cm³): {v:.2f}\nSuperficie (cm²): {s:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")

    tk.Button(sub, text="Calcular", bg="#BBDEFB", font=("Arial", 11, "bold"), command=calcular).pack(pady=5)


def ventana_esfera():
    sub = tk.Toplevel()
    sub.title("Esfera")
    sub.config(bg="#E8F5E9")
    sub.geometry("300x260")

    tk.Label(sub, text="Radio (cm):", bg="#E8F5E9", font=("Arial", 11)).pack(pady=5)
    radio = tk.Entry(sub)
    radio.pack()

    resultado = tk.Label(sub, text="", bg="#E8F5E9", font=("Arial", 11))
    resultado.pack(pady=10)

    def calcular():
        try:
            r = float(radio.get())
            v, s = calcular_esfera(r)
            resultado.config(text=f"Volumen (cm³): {v:.2f}\nSuperficie (cm²): {s:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")

    tk.Button(sub, text="Calcular", bg="#C8E6C9", font=("Arial", 11, "bold"), command=calcular).pack(pady=5)


def ventana_piramide():
    sub = tk.Toplevel()
    sub.title("Pirámide")
    sub.config(bg="#FFF3E0")
    sub.geometry("300x300")

    tk.Label(sub, text="Base (cm):", bg="#FFF3E0", font=("Arial", 11)).pack(pady=5)
    base = tk.Entry(sub)
    base.pack()

    tk.Label(sub, text="Altura (cm):", bg="#FFF3E0", font=("Arial", 11)).pack(pady=5)
    altura = tk.Entry(sub)
    altura.pack()

    tk.Label(sub, text="Apotema (cm):", bg="#FFF3E0", font=("Arial", 11)).pack(pady=5)
    apotema = tk.Entry(sub)
    apotema.pack()

    resultado = tk.Label(sub, text="", bg="#FFF3E0", font=("Arial", 11))
    resultado.pack(pady=10)

    def calcular():
        try:
            b = float(base.get())
            h = float(altura.get())
            a = float(apotema.get())
            v, s = calcular_piramide(b, h, a)
            resultado.config(text=f"Volumen (cm³): {v:.2f}\nSuperficie (cm²): {s:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")

    tk.Button(sub, text="Calcular", bg="#FFE0B2", font=("Arial", 11, "bold"), command=calcular).pack(pady=5)


#VENTANA PRINCIPAL
root = tk.Tk()
root.title("Figuras")
root.geometry("350x150")
root.config(bg="#F3E5F5")

tk.Label(root, text="Seleccione una figura:", bg="#F3E5F5", font=("Arial", 12, "bold")).pack(pady=10)

frame = tk.Frame(root, bg="#F3E5F5")
frame.pack()

tk.Button(frame, text="Cilindro", bg="#BBDEFB", font=("Arial", 11, "bold"), width=10, command=ventana_cilindro).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Esfera", bg="#C8E6C9", font=("Arial", 11, "bold"), width=10, command=ventana_esfera).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Pirámide", bg="#FFE0B2", font=("Arial", 11, "bold"), width=10, command=ventana_piramide).grid(row=0, column=2, padx=5)

root.mainloop()