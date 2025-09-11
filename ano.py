import tkinter as tk
from tkinter import messagebox
import webbrowser

# --------- Link Functions ---------
def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com/@FIZIstyle")

def open_dpmdas():
    webbrowser.open("https://doprava.dpmdas.cz/")

# --------- Calculator Functions ---------
def click(event):
    current = calc_entry.get()
    button_text = event.widget["text"]

    if button_text == "=":
        try:
            result = eval(current)
            calc_entry.delete(0, tk.END)
            calc_entry.insert(tk.END, str(result))
        except:
            calc_entry.delete(0, tk.END)
            calc_entry.insert(tk.END, "Error")
    elif button_text == "C":
        calc_entry.delete(0, tk.END)
    else:
        calc_entry.insert(tk.END, button_text)

# --------- Main Window Setup ---------
root = tk.Tk()
root.title("Launcher Application")
root.geometry("800x550")
root.resizable(False, False)

# --------- Label ---------
hello_label = tk.Label(root, text="Launcher", font=("Arial", 20))
hello_label.pack(pady=10)

# --------- Link Buttons ---------
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Google", width=25, command=open_google).pack(pady=3)
tk.Button(button_frame, text="Cringe", width=25, command=open_youtube).pack(pady=3)
tk.Button(button_frame, text="doprava.dpmdas.cz", width=25, command=open_dpmdas).pack(pady=3)
tk.Button(button_frame, text="Close", width=25, command=root.destroy).pack(pady=10)

# --------- Calculator UI ---------
calc_label = tk.Label(root, text="Calculator", font=("Arial", 14, "bold"))
calc_label.pack(pady=5)

calc_entry = tk.Entry(root, font=("Arial", 16), justify='right', bd=5, relief=tk.RIDGE)
calc_entry.pack(padx=10, pady=5, fill=tk.X)

# Calculator buttons
btn_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

calc_frame = tk.Frame(root)
calc_frame.pack()

for row in btn_texts:
    row_frame = tk.Frame(calc_frame)
    row_frame.pack()
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, width=6, height=2, font=("Arial", 14))
        btn.pack(side=tk.LEFT, padx=3, pady=3)
        btn.bind("<Button-1>", click)

# --------- Run the App ---------
root.mainloop()
