import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_var.get()

    # Ensure at least one character type is selected
    if not (use_lowercase or use_uppercase or use_digits or use_special_chars):
        messagebox.showwarning("Input Error", "Select at least one character type.")
        return

    char_set = ''
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkbuttons for character types
lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_check.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_check.pack(pady=5)

digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5)

special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password entry
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
