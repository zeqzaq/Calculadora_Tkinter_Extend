import tkinter as tk
from tkinter import messagebox
from calculadora_IMC import CalculadoraIMC
from calculadora import CalculadoraBasica
from calculadora_edad import CalculadoraEdad
from calculadora_temp import CalculadoraTemp
from calculadora_salario import CalculadoraSalario
from calculadora_promedio import CalculadoraPromedio
from calculadora_monedas import CalculadoraMonedas
from calculadora_descuentos import CalculadoraDescuentos
from calculadora_clima import CalculadoraClima
from calculadora_combustible import CalculadoraCombustible
from calculadora_servicios import CalculadoraServicios

class MenuPrinci:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("500x600")
        self.root.configure(bg="#34495E")
        self.root.resizable(False, False)

        try:
            icono = tk.PhotoImage(file="img/icono.png")
            self.root.iconphoto(True, icono)
        except:
            pass

        tk.Label(root, text="Menú Principal", font=("Arial", 12, "italic"),
                 bg="#34495E", fg="#ECF0F1").pack(pady=20)

        tk.Button(root, text="Calculadora Básica", font=("Arial", 11, "bold"),
                  bg="#2980B9", fg="white", width=30, command=self.abrir_calculadora).pack(pady=10)

        tk.Button(root, text="Calculadora de Edad", font=("Arial", 11, "bold"),
                  bg="#27AE60", fg="white", width=30, command=self.abrir_calculadora_edad).pack(pady=10)
        
        tk.Button(root, text="Calculadora de Temperatura", font=("Arial", 11, "bold"),
                  bg="#8E44AD", fg="white", width=30, command=self.abrir_calculadora_temp).pack(pady=10)

        tk.Button(root, text="Calculadora de IMC", font=("Arial", 11, "bold"),
                  bg="#E74C3C", fg="white", width=30, command=self.abrir_calculadora_IMC).pack(pady=10)
        
        tk.Button(root, text="Calculadora de Salario", font=("Arial", 11, "bold"),
                  bg="#F39C12", fg="white", width=30, command=self.abrir_calculadora_salario).pack(pady=10)

        tk.Button(root, text="Calculadora de Promedio", font=("Arial", 11, "bold"),
                  bg="#1ABC9C", fg="white", width=30, command=self.abrir_calculadora_promedio).pack(pady=10)

        tk.Button(root, text="Conversor de Monedas", font=("Arial", 11, "bold"),
                  bg="#3498DB", fg="white", width=30, command=self.abrir_calculadora_monedas).pack(pady=10)

        tk.Button(root, text="Calculadora de Descuentos", font=("Arial", 11, "bold"),
                  bg="#E67E22", fg="white", width=30, command=self.abrir_calculadora_descuentos).pack(pady=10)

        tk.Button(root, text="Simulador del Clima", font=("Arial", 11, "bold"),
                  bg="#9B59B6", fg="white", width=30, command=self.abrir_calculadora_clima).pack(pady=10)

        tk.Button(root, text="Calculadora de Combustible", font=("Arial", 11, "bold"),
                  bg="#2ECC71", fg="white", width=30, command=self.abrir_calculadora_combustible).pack(pady=10)

        tk.Button(root, text="Calculadora de Servicios", font=("Arial", 11, "bold"),
                  bg="#E74C3C", fg="white", width=30, command=self.abrir_calculadora_servicios).pack(pady=10)

    def abrir_calculadora(self):
        calculadora_window = tk.Toplevel(self.root)
        CalculadoraBasica(calculadora_window)

    def abrir_calculadora_edad(self):
        edad_window = tk.Toplevel(self.root)
        CalculadoraEdad(edad_window)

    def abrir_calculadora_temp(self):
        temp_window = tk.Toplevel(self.root)
        CalculadoraTemp(temp_window)

    def abrir_calculadora_IMC(self):
        imc_window = tk.Toplevel(self.root)
        CalculadoraIMC(imc_window)

    def abrir_calculadora_salario(self):
        salario_window = tk.Toplevel(self.root)
        CalculadoraSalario(salario_window)

    def abrir_calculadora_promedio(self):
        promedio_window = tk.Toplevel(self.root)
        CalculadoraPromedio(promedio_window)

    def abrir_calculadora_monedas(self):
        monedas_window = tk.Toplevel(self.root)
        CalculadoraMonedas(monedas_window)

    def abrir_calculadora_descuentos(self):
        descuentos_window = tk.Toplevel(self.root)
        CalculadoraDescuentos(descuentos_window)

    def abrir_calculadora_clima(self):
        clima_window = tk.Toplevel(self.root)
        CalculadoraClima(clima_window)

    def abrir_calculadora_combustible(self):
        combustible_window = tk.Toplevel(self.root)
        CalculadoraCombustible(combustible_window)

    def abrir_calculadora_servicios(self):
        servicios_window = tk.Toplevel(self.root)
        CalculadoraServicios(servicios_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrinci(root)
    root.mainloop()
