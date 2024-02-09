import tkinter as tk
import csv

def calculate_tax():
    income = float(income_entry.get())
    tax = income * 0.19  # Calcula el impuesto como el 19% del ingreso
    tax_entry.delete(0, tk.END)
    tax_entry.insert(tk.END, tax)

def save_data():
    name = name_entry.get()
    last_name = last_name_entry.get()
    rut = rut_entry.get()
    gender = gender_var.get()
    income = income_entry.get()
    tax = tax_entry.get()

    with open('tax_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, last_name, rut, gender, income, tax])

window = tk.Tk()
window.title("Calculadora de Impuestos")

# Nombre
name_label = tk.Label(window, text="Nombre:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Apellido
last_name_label = tk.Label(window, text="Apellido:")
last_name_label.pack()
last_name_entry = tk.Entry(window)
last_name_entry.pack()

# RUT
rut_label = tk.Label(window, text="RUT:")
rut_label.pack()
rut_entry = tk.Entry(window)
rut_entry.pack()

# Sexo
gender_label = tk.Label(window, text="Sexo:")
gender_label.pack()
gender_var = tk.StringVar()
gender_radio_male = tk.Radiobutton(window, text="Masculino", variable=gender_var, value="Masculino")
gender_radio_male.pack()
gender_radio_female = tk.Radiobutton(window, text="Femenino", variable=gender_var, value="Femenino")
gender_radio_female.pack()

# Ingreso
income_label = tk.Label(window, text="Ingreso:")
income_label.pack()
income_entry = tk.Entry(window)
income_entry.pack()

# Impuesto
tax_label = tk.Label(window, text="Impuesto:")
tax_label.pack()
tax_entry = tk.Entry(window)
tax_entry.pack()

# Botón de cálculo de impuesto
calculate_button = tk.Button(window, text="Calcular Impuesto", command=calculate_tax)
calculate_button.pack()

# Botón de guardado de datos
save_button = tk.Button(window, text="Guardar Datos", command=save_data)
save_button.pack()

window.mainloop()