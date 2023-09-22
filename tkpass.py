"""
TKPASS GENERATOR - @everton-tenorio
"""
import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip


def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if not use_upper and not use_lower and not use_numbers and not use_symbols:
        password_var.set("Selecione pelo menos uma opção")
        return

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*(.)_-+=<,>?"

    if length < 8:
        password_var.set("Comprimento mínimo é 8")
    elif length > 100:
        password_var.set("Comprimento máximo é 100")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
        password_entry.config(width=length)  # Ajusta a largura do campo de texto


def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)


def update_length_value_label(event):
    length_value_label.config(text=str(int(length_var.get())))


# Criar janela principal
root = tk.Tk()
root.title("Tkpass Generator")

# Variáveis de controle
length_var = tk.DoubleVar()
length_var.set(8.0)
upper_var = tk.BooleanVar()
upper_var.set(True)
lower_var = tk.BooleanVar()
lower_var.set(True)
numbers_var = tk.BooleanVar()
numbers_var.set(True)
symbols_var = tk.BooleanVar()
symbols_var.set(False)
password_var = tk.StringVar()

# Frame de opções
options_frame = ttk.LabelFrame(root, text="Opções")
options_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Checkboxes
upper_checkbox = ttk.Checkbutton(options_frame, text="Letras maiúsculas", variable=upper_var)
lower_checkbox = ttk.Checkbutton(options_frame, text="Letras minúsculas", variable=lower_var)
numbers_checkbox = ttk.Checkbutton(options_frame, text="Números", variable=numbers_var)
symbols_checkbox = ttk.Checkbutton(options_frame, text="Símbolos", variable=symbols_var)
upper_checkbox.grid(row=0, column=0, sticky="w")
lower_checkbox.grid(row=1, column=0, sticky="w")
numbers_checkbox.grid(row=2, column=0, sticky="w")
symbols_checkbox.grid(row=3, column=0, sticky="w")

# Comprimento da senha
length_label = ttk.Label(options_frame, text="Comprimento:")
length_scale = ttk.Scale(options_frame, from_=8, to=100, orient="horizontal", variable=length_var, command=update_length_value_label)
length_scale.grid(row=4, column=0, columnspan=2, sticky="ew")

# Rótulo para exibir o valor do comprimento da senha
length_value_label = ttk.Label(options_frame, text=str(int(length_var.get())))
length_value_label.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# Botões
generate_button = ttk.Button(root, text="Gerar Senha", command=generate_password)
copy_button = ttk.Button(root, text="Copiar", command=copy_password)
generate_button.grid(row=1, column=0, padx=10, pady=10)
copy_button.grid(row=1, column=1, padx=10, pady=10)

# Campo de texto da senha
password_entry = ttk.Entry(root, textvariable=password_var, state="readonly")
password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Iniciar a janela
root.mainloop()
