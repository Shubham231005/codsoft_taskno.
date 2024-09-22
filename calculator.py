import tkinter as tk

# Function to update expression in the entry box
def update_expression(symbol):
    current_text = entry.get()
    new_text = current_text + str(symbol)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result of the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Use eval() for simple expression evaluation
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to delete the last character
def delete_last():
    current_text = entry.get()
    new_text = current_text[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

# Function to toggle window maximization
def toggle_maximize():
    if root.state() == 'zoomed':
        root.state('normal')  # Unmaximize
    else:
        root.state('zoomed')  # Maximize

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Enable window resizing
root.resizable(True, True)

# Create the entry box to display the expression and result
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=5)

# Button layout: text, row, column, colspan
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons and add them to the window
for (text, row, column) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                        bg="#6ca6cd", command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                        command=lambda t=text: update_expression(t))
    btn.grid(row=row, column=column, padx=5, pady=5)

# Special buttons for Clear and Delete
clear_btn = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), bg="#ff6347", command=clear)
clear_btn.grid(row=5, column=0, padx=5, pady=5)

delete_btn = tk.Button(root, text="Del", width=5, height=2, font=("Arial", 18), bg="#ff6347", command=delete_last)
delete_btn.grid(row=5, column=1, padx=5, pady=5)

# Add maximize toggle button
maximize_btn = tk.Button(root, text="Maximize", width=11, height=2, font=("Arial", 18), bg="#4682b4", command=toggle_maximize)
maximize_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
