import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    full_name = name_entry.get()
    dob = dob_entry.get()
    if len(full_name.split()) < 1 or len(dob) != 8:
        messagebox.showerror("Error", "Please enter a valid name and date of birth (DDMMYYYY format)")
        return
    dob_digits = ''.join(filter(str.isdigit, dob))
    random_digits = random.sample(dob_digits, 2) 
    
  
    name_parts = full_name.split()
    long_name = ''.join([name for name in name_parts if len(name) >= 6])
    if len(long_name) < 6:
        messagebox.showerror("Error", "Your name must contain at least one part with 6 or more letters.")
        return
    name_part = long_name[:6]  
    special_char = random.choice(['@', '$'])
    password = f"{name_part}{special_char}{''.join(random_digits)}"
    if len(password) < 9:
        password += random.choice(dob_digits)
    result_label.config(text=f"Generated Password: {password}")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="lightblue")
title_label = tk.Label(root, text="Custom Password Generator", font=("Arial", 16), bg="lightblue", pady=10)
title_label.pack()
name_label = tk.Label(root, text="Enter Full Name:", font=("Arial", 12), bg="lightblue")
name_label.pack()
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)
dob_label = tk.Label(root, text="Enter Date of Birth (DDMMYYYY):", font=("Arial", 12), bg="lightblue")
dob_label.pack()
dob_entry = tk.Entry(root, width=30, font=("Arial", 12))
dob_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password, bg="green", fg="white")
generate_button.pack(pady=15)
result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue", fg="darkblue")
result_label.pack(pady=5)
root.mainloop()

