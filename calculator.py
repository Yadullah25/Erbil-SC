import tkinter as tk

# Function to update the expression in the entry widget
def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

# Function to evaluate the expression and update the entry widget
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Professional Calculator")

# Create an entry widget to display the expression
entry = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons and their layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), 
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=3, command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=3, command=clear)
    else:
        button = tk.Button(root, text=text, width=10, height=3, command=lambda txt=text: click(txt))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()
