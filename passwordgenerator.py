import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        # Get the input length and other options from the user
        length = int(length_entry.get())
        include_lowercase = lowercase_var.get()
        include_uppercase = uppercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()
        num_options = int(num_options_var.get())
        
        # Build the character pool based on user selection
        char_pool = ""
        if include_lowercase:
            char_pool += string.ascii_lowercase
        if include_uppercase:
            char_pool += string.ascii_uppercase
        if include_digits:
            char_pool += string.digits
        if include_special:
            char_pool += string.punctuation
        
        if not char_pool:
            messagebox.showwarning("Selection Error", "Please select at least one character type!")
            return

        if length < 1:
            messagebox.showwarning("Input Error", "Password length must be at least 1.")
            return

        # Generate the password(s)
        password_display.delete(1.0, tk.END)  # Clear previous results
        for _ in range(num_options):
            password = ''.join(random.choice(char_pool) for _ in range(length))
            password_display.insert(tk.END, password + "\n")
    
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid inputs for length and options.")

# Create the main window
root = tk.Tk()
root.title("SHUBHAMSZEE Password Generator")
root.geometry("500x600")
root.config(bg="#ecf0f1")

# Title label
title_label = tk.Label(root, text="SHUBHAMSZEE Password Generator", font=("Arial", 22, "bold"), bg="#ecf0f1", fg="#2c3e50")
title_label.pack(pady=15)

# Length label and entry
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 14), bg="#ecf0f1")
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 14), width=10)
length_entry.pack(pady=5)

# Character type selection checkboxes
char_type_label = tk.Label(root, text="Select Character Types:", font=("Arial", 14), bg="#ecf0f1")
char_type_label.pack(pady=5)

# Variables for checkboxes
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Add checkboxes
checkbox_frame = tk.Frame(root, bg="#ecf0f1")
checkbox_frame.pack(pady=5)

tk.Checkbutton(checkbox_frame, text="Lowercase Letters", variable=lowercase_var, font=("Arial", 12), bg="#ecf0f1").pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Uppercase Letters", variable=uppercase_var, font=("Arial", 12), bg="#ecf0f1").pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Digits", variable=digits_var, font=("Arial", 12), bg="#ecf0f1").pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_var, font=("Arial", 12), bg="#ecf0f1").pack(anchor='w')

# Number of password options
num_options_label = tk.Label(root, text="How many password options?", font=("Arial", 14), bg="#ecf0f1")
num_options_label.pack(pady=5)

num_options_var = tk.StringVar(value="1")
num_options_dropdown = tk.OptionMenu(root, num_options_var, "1", "2", "3")
num_options_dropdown.config(font=("Arial", 12), width=5)
num_options_dropdown.pack(pady=5)

# Generate button with valid color code
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#27ae60", fg="white", command=generate_password)
generate_button.pack(pady=15)

# Display generated passwords
password_display_label = tk.Label(root, text="Generated Password(s):", font=("Arial", 14), bg="#ecf0f1")
password_display_label.pack(pady=5)

password_display = tk.Text(root, font=("Arial", 14), height=6, width=40)
password_display.pack(pady=5)

# Footer label
footer_label = tk.Label(root, text="Powered by SHUBHAMSZEE", font=("Arial", 12, "italic"), bg="#ecf0f1", fg="#34495e")
footer_label.pack(pady=20)

# Start the GUI
root.mainloop()


