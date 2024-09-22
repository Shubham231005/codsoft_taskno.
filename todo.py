import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="lightblue")

title_label = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=10)

task_entry_frame = tk.Frame(root)
task_entry_frame.pack(pady=10)

task_entry = tk.Entry(task_entry_frame, font=("Arial", 14), width=25)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(task_entry_frame, text="Add Task", font=("Arial", 12), command=add_task, bg="green", fg="white")
add_button.pack(side=tk.LEFT)

task_listbox_frame = tk.Frame(root)
task_listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(task_listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(task_listbox_frame, font=("Arial", 14), height=10, width=30, yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT)

scrollbar.config(command=task_listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

remove_button = tk.Button(button_frame, text="Remove Task", font=("Arial", 12), command=remove_task, bg="red", fg="white")
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), command=clear_tasks, bg="orange", fg="white")
clear_button.pack(side=tk.LEFT, padx=10)

footer_label = tk.Label(root, text="Stay Productive!", font=("Arial", 12, "italic"), bg="lightblue", fg="darkblue")
footer_label.pack(pady=20)
root.mainloop()
