import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
 
    # Check what complexity the user wants
    complexity = ''
    if var_upper.get():
        complexity += string.ascii_uppercase
    if var_lower.get():
        complexity += string.ascii_lowercase
    if var_digits.get():
        complexity += string.digits
    if var_special.get():
        complexity += string.punctuation

    # If no complexity selected, show error
    if not complexity:
        messagebox.showwarning("Warning", "Select at least one option for password complexity!")
        return

    # Generate password
    password = ''.join(random.choice(complexity) for i in range(length))

    # Display generated password
    result_label.config(text=f"Generated Password: {password}")

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg= "lightblue")
# Set window size
root.geometry("400x300")

# Length of password
tk.Label(root, text="Password Length:",bg="lightblue").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Password complexity options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters",bg="lightblue", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters",bg="lightblue", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Include Digits",bg="lightblue", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters",bg="lightblue", variable=var_special).pack(anchor='w')

# Generate button
generate_btn = tk.Button(root, text="Generate Password",bg="lightblue",fg="black", command=generate_password)
generate_btn.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
# Run the Tkinter event loop
root.mainloop()