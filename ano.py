import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import platform

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

# --------- Tabs Setup ---------
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# --------- Tabs ---------
tab_links = ttk.Frame(notebook)
tab_calc = ttk.Frame(notebook)
tab_apps = ttk.Frame(notebook)
notebook.add(tab_links, text='Links')
notebook.add(tab_calc, text='Calculator')
notebook.add(tab_apps, text='Applications Installing')

# --------- Label ---------
hello_label = tk.Label(tab_links, text="Launcher", font=("Arial", 20))
hello_label.pack(pady=10)

# --------- Links Tab Widgets ---------
google_btn = tk.Button(tab_links, text="Google", command=open_google, width=20)
google_btn.pack(pady=5)
youtube_btn = tk.Button(tab_links, text="YouTube", command=open_youtube, width=20)
youtube_btn.pack(pady=5)
dpmdas_btn = tk.Button(tab_links, text="DPMDAS", command=open_dpmdas, width=20)
dpmdas_btn.pack(pady=5)

# --------- Calculator Tab Widgets ---------
calc_entry = tk.Entry(tab_calc, font=("Arial", 16), width=25, borderwidth=2, relief="groove")
calc_entry.pack(pady=10)

buttons_frame = tk.Frame(tab_calc)
buttons_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(buttons_frame, text=char, font=("Arial", 14), width=5, height=2)
        btn.grid(row=r, column=c, padx=3, pady=3)
        btn.bind("<Button-1>", click)

# --------- Applications Installing Tab Widgets ---------
apps_label = tk.Label(tab_apps, text="Applications Installing", font=("Arial", 20))
apps_label.pack(pady=10)
hello_label.pack(pady=10)

# --------- Installer Functions ---------
def install_chrome():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://www.google.com/chrome/"
    elif os_name == "Darwin":
        url = "https://www.google.com/chrome/"
    elif os_name == "Linux":
        url = "https://www.google.com/chrome/"
    else:
        url = "https://www.google.com/chrome/"
    webbrowser.open(url)

def install_discord():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://discord.com/download"
    elif os_name == "Darwin":
        url = "https://discord.com/download"
    elif os_name == "Linux":
        url = "https://discord.com/download"
    else:
        url = "https://discord.com/download"
    webbrowser.open(url)

def install_vscode():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://code.visualstudio.com/download"
    elif os_name == "Darwin":
        url = "https://code.visualstudio.com/download"
    elif os_name == "Linux":
        url = "https://code.visualstudio.com/download"
    else:
        url = "https://code.visualstudio.com/download"
    webbrowser.open(url)

# --------- Installer Buttons ---------
chrome_btn = tk.Button(tab_apps, text="Install Google Chrome", command=install_chrome, width=25)
chrome_btn.pack(pady=5)
discord_btn = tk.Button(tab_apps, text="Install Discord", command=install_discord, width=25)
discord_btn.pack(pady=5)
vscode_btn = tk.Button(tab_apps, text="Install Visual Studio Code", command=install_vscode, width=25)
vscode_btn.pack(pady=5)


# --------- Run the App ---------
root.mainloop()
