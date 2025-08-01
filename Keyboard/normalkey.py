import tkinter as tk
def on_key_click(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + key)
def on_backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])
def on_clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Virtual Keyboard")
entry = tk.Entry(root, font=('Arial', 20), width=30, borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=15, pady=10)
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
    ['Clear', 'Space']
]
row_num = 1
for row in keys:
    col_num = 0
    for key in row:
        if key == 'Backspace':
            button = tk.Button(root, text=key, width=5, height=2, font=('Arial', 12), command=on_backspace, bg='black', fg='white')
        elif key == 'Clear':
            button = tk.Button(root, text=key, width=5, height=2, font=('Arial', 12), command=on_clear, bg='black', fg='white')
        elif key == 'Space':
            button = tk.Button(root, text="Space", width=20, height=2, font=('Arial', 12), command=lambda: on_key_click(" "), bg='black', fg='white')
        elif key == 'Enter':
            button = tk.Button(root, text=key, width=5, height=2, font=('Arial', 12), command=lambda: on_key_click("\n"), bg='black', fg='white')
        elif key == 'Shift':
            button = tk.Button(root, text=key, width=5, height=2, font=('Arial', 12), bg='black', fg='white')
        else:
            button = tk.Button(root, text=key, width=5, height=2, font=('Arial', 12), command=lambda k=key: on_key_click(k), bg='black', fg='white')
        button.grid(row=row_num, column=col_num, padx=3, pady=3)
        col_num += 1
    row_num += 1
root.mainloop()
