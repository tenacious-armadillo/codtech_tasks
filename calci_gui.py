import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create and place widgets
label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

operation_var = tk.StringVar(value='+')
frame_operations = tk.Frame(root)
frame_operations.pack()

radio_add = tk.Radiobutton(frame_operations, text="Addition (+)", variable=operation_var, value='+')
radio_add.pack(side=tk.LEFT)

radio_subtract = tk.Radiobutton(frame_operations, text="Subtraction (-)", variable=operation_var, value='-')
radio_subtract.pack(side=tk.LEFT)

radio_multiply = tk.Radiobutton(frame_operations, text="Multiplication (*)", variable=operation_var, value='*')
radio_multiply.pack(side=tk.LEFT)

radio_divide = tk.Radiobutton(frame_operations, text="Division (/)", variable=operation_var, value='/')
radio_divide.pack(side=tk.LEFT)

button_calculate = tk.Button(root, text="Calculate", command=perform_operation)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

# Start the main event loop
root.mainloop()
