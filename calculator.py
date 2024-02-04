import tkinter as tk

def on_button_click(button_value):
    current_text = entry.get()
    
    if button_value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the current calculation
entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place the calculator buttons
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, width=5, height=2, 
        command=lambda b=button: on_button_click(b),
        font=('Arial', 14), bd=5, relief=tk.RAISED
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter main loop
root.mainloop()
