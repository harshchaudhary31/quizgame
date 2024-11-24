import tkinter as tk
from tkinter import messagebox
import os

# Functions for task management
def add_task():
    task = task_entry.get()
    if not task.strip():
        messagebox.showerror("Input Error", "Task cannot be empty!")
        return
    tasks.append({"task": task.strip(), "completed": False})
    task_entry.delete(0, tk.END)
    update_task_list()
    messagebox.showinfo("Success", "Task added successfully!")

def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        task_list.insert(tk.END, f"{i}. {task['task']} [{status}]")

def mark_completed():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Selection Error", "Please select a task to mark as completed.")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    update_task_list()
    messagebox.showinfo("Success", "Task marked as completed!")

def save_tasks(filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [
            {"task": line.split(",")[0], "completed": line.split(",")[1].strip() == "True"}
            for line in file.readlines()
        ]

# Initialize tasks
tasks = load_tasks()

# Create main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")

# Task Entry
tk.Label(window, text="Enter a Task:", font=("Arial", 12)).pack(pady=10)
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=5)

# Add Task Button
tk.Button(window, text="Add Task", command=add_task, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

# Task List
tk.Label(window, text="Tasks:", font=("Arial", 12)).pack(pady=10)
task_list = tk.Listbox(window, width=50, height=15, font=("Arial", 10))
task_list.pack(pady=5)

# Mark Completed Button
tk.Button(window, text="Mark Completed", command=mark_completed, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

# Save Tasks Button
tk.Button(window, text="Save Tasks", command=save_tasks, font=("Arial", 12), bg="orange", fg="white").pack(pady=10)

# Load initial data
update_task_list()

# Run the application
window.mainloop()
