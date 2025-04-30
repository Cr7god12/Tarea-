import tkinter as tk
from tkinter import messagebox

class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0 

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias = dias_anticipacion
        self.precio = 50.0 if dias_anticipacion >= 10 else 60.0

class Galeria(Platea): 
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero, dias_anticipacion)
        self.precio = 25.0 if dias_anticipacion >= 10 else 30.0

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")

        self.tipo_boleto = tk.StringVar()
        self.numero = tk.StringVar()
        self.dias = tk.StringVar()

        titulo = tk.Label(root, text="Teatro Municipal", font=("Arial", 16))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Datos del Boleto:").grid(row=1, column=0, sticky="w", padx=10)

        tk.Radiobutton(root, text="Palco", variable=self.tipo_boleto, value="Palco").grid(row=2, column=0, sticky="w", padx=20)
        tk.Radiobutton(root, text="Platea", variable=self.tipo_boleto, value="Platea").grid(row=3, column=0, sticky="w", padx=20)
        tk.Radiobutton(root, text="Galería", variable=self.tipo_boleto, value="Galeria").grid(row=4, column=0, sticky="w", padx=20)

        tk.Label(root, text="Número de boleto:").grid(row=2, column=1, sticky="e", padx=10)
        tk.Entry(root, textvariable=self.numero).grid(row=2, column=2, padx=10)

        tk.Label(root, text="Días de anticipación:").grid(row=3, column=1, sticky="e", padx=10)
        tk.Entry(root, textvariable=self.dias).grid(row=3, column=2, padx=10)

        tk.Button(root, text="Vender", command=self.vender_boleto).grid(row=5, column=0, pady=10)
        tk.Button(root, text="Salir", command=root.quit).grid(row=5, column=1, pady=10)

        self.info_label = tk.Label(root, text="Información: ", font=("Arial", 12))
        self.info_label.grid(row=6, column=0, columnspan=3, pady=10)

    def vender_boleto(self):
        tipo = self.tipo_boleto.get()
        num_texto = self.numero.get()
        dias_texto = self.dias.get()
        if not tipo:
            messagebox.showerror("Error", "Seleccione el tipo de boleto.")
            return
        if not num_texto.isdigit():
            messagebox.showerror("Error", "Ingrese un número de boleto válido.")
            return
        numero = int(num_texto)
        if tipo in ["Platea", "Galeria"]:
            if not dias_texto.isdigit():
                messagebox.showerror("Error", "Ingrese los días de anticipación.")
                return
            dias = int(dias_texto)
        if tipo == "Palco":
            boleto = Palco(numero)
        elif tipo == "Platea":
            boleto = Platea(numero, dias)
        elif tipo == "Galeria":
            boleto = Galeria(numero, dias)
        else:
            messagebox.showerror("Error", "Tipo de boleto no válido.")
            return
        self.info_label.config(text="Información: " + str(boleto))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
