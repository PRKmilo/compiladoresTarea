import tkinter as tk
from tkinter import scrolledtext, filedialog
from lexer import tokenize
from parser import Parser

# Variable para almacenar el código cargado desde un archivo
code_from_file = ""

# Función para cargar el código desde un archivo
def cargar_codigo():
    global code_from_file
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            code_from_file = file.read()
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, code_from_file)

# Función para procesar el código ingresado
def ejecutar_codigo():
    code = input_text.get("1.0", tk.END)
    output_text.delete("1.0", tk.END)

    try:
        tokens = tokenize(code)
        output_text.insert(tk.END, "Tokens generados:\n")
        for token in tokens:
            output_text.insert(tk.END, f"{token}\n")
        parser = Parser(tokens)
        parser.parse()
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

# Crear la ventana principal
window = tk.Tk()
window.title("Intérprete de Código de Bicicletas")

# Crear el botón para cargar el código desde un archivo
load_button = tk.Button(window, text="Cargar Código", command=cargar_codigo)
load_button.pack(pady=5)

# Crear el campo de texto para ingresar el código
input_label = tk.Label(window, text="Ingresa el código:")
input_label.pack(pady=5)  # Añadir un poco de espacio

input_text = scrolledtext.ScrolledText(window, height=10, width=60)
input_text.pack(pady=5)

# Crear el botón para ejecutar el código
execute_button = tk.Button(window, text="Ejecutar", command=ejecutar_codigo)
execute_button.pack(pady=5)

# Crear el campo de texto para mostrar el output
output_label = tk.Label(window, text="Output:")
output_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(window, height=10, width=60)
output_text.pack(pady=5)

# Iniciar el loop principal de la interfaz
window.mainloop()


