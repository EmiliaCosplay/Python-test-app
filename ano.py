import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import platform
import urllib.request
import urllib.error
import os
import subprocess
from pathlib import Path

# --------- Theme Configuration ---------
THEMES = {
    'light': {
        'bg': '#ffffff',
        'fg': '#000000',
        'button_bg': '#e8e8e8',
        'button_fg': '#000000',
        'entry_bg': '#ffffff',
        'entry_fg': '#000000',
        'label_bg': '#ffffff',
        'label_fg': '#000000'
    },
    'dark': {
        'bg': '#1e1e1e',
        'fg': '#ffffff',
        'button_bg': '#2d2d2d',
        'button_fg': '#ffffff',
        'entry_bg': '#3e3e3e',
        'entry_fg': '#ffffff',
        'label_bg': '#1e1e1e',
        'label_fg': '#ffffff'
    }
}

current_theme = 'light'
widget_list = []  # Keep track of all widgets for theme updates

# --------- Theme Functions ---------
def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = THEMES[theme_name]
    
    # Apply to root and tabs
    root.configure(bg=theme['bg'])
    
    # Apply to all tracked widgets
    for widget, widget_type in widget_list:
        if widget_type == 'button':
            widget.configure(bg=theme['button_bg'], fg=theme['button_fg'])
        elif widget_type == 'entry':
            widget.configure(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'])
        elif widget_type == 'label':
            widget.configure(bg=theme['label_bg'], fg=theme['label_fg'])
        elif widget_type == 'frame':
            widget.configure(bg=theme['bg'])
    
    # Update special colored buttons with light text
    for widget, widget_type in widget_list:
        if widget_type == 'special_button' and current_theme == 'dark':
            widget.configure(fg='#ffffff')
        elif widget_type == 'special_button' and current_theme == 'light':
            widget.configure(fg='#ffffff')

def register_widget(widget, widget_type):
    """Register a widget for theme management"""
    widget_list.append((widget, widget_type))
def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

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
root.configure(bg=THEMES['light']['bg'])

# --------- Theme Switcher Frame ---------
theme_frame = tk.Frame(root, bg=THEMES['light']['bg'])
theme_frame.pack(fill='x', padx=10, pady=10)

light_theme_btn = tk.Button(theme_frame, text="☀️ Light Mode", command=lambda: apply_theme('light'), 
                             bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'], width=15)
light_theme_btn.pack(side='left', padx=5)
register_widget(light_theme_btn, 'button')

dark_theme_btn = tk.Button(theme_frame, text="🌙 Dark Mode", command=lambda: apply_theme('dark'),
                            bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'], width=15)
dark_theme_btn.pack(side='left', padx=5)
register_widget(dark_theme_btn, 'button')

register_widget(theme_frame, 'frame')

# --------- Tabs Setup ---------
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# --------- Tabs ---------
tab_links = tk.Frame(notebook, bg=THEMES['light']['bg'])
tab_calc = tk.Frame(notebook, bg=THEMES['light']['bg'])
tab_apps = tk.Frame(notebook, bg=THEMES['light']['bg'])
register_widget(tab_links, 'frame')
register_widget(tab_calc, 'frame')
register_widget(tab_apps, 'frame')
notebook.add(tab_links, text='Links')
notebook.add(tab_calc, text='Calculator')
notebook.add(tab_apps, text='Applications Installing')

# --------- Label ---------
hello_label = tk.Label(tab_links, text="Launcher", font=("Arial", 20), 
                       bg=THEMES['light']['label_bg'], fg=THEMES['light']['label_fg'])
hello_label.pack(pady=10)
register_widget(hello_label, 'label')

# --------- Links Tab Widgets ---------
google_btn = tk.Button(tab_links, text="Google", command=open_google, width=20,
                       bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
google_btn.pack(pady=5)
register_widget(google_btn, 'button')

youtube_btn = tk.Button(tab_links, text="YouTube", command=open_youtube, width=20,
                        bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
youtube_btn.pack(pady=5)
register_widget(youtube_btn, 'button')

dpmdas_btn = tk.Button(tab_links, text="DPMDAS", command=open_dpmdas, width=20,
                       bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
dpmdas_btn.pack(pady=5)
register_widget(dpmdas_btn, 'button')

# --------- Calculator Tab Widgets ---------
calc_entry = tk.Entry(tab_calc, font=("Arial", 16), width=25, borderwidth=2, relief="groove",
                      bg=THEMES['light']['entry_bg'], fg=THEMES['light']['entry_fg'], insertbackground=THEMES['light']['fg'])
calc_entry.pack(pady=10)
register_widget(calc_entry, 'entry')

buttons_frame = tk.Frame(tab_calc, bg=THEMES['light']['bg'])
buttons_frame.pack()
register_widget(buttons_frame, 'frame')

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(buttons_frame, text=char, font=("Arial", 14), width=5, height=2,
                       bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
        btn.grid(row=r, column=c, padx=3, pady=3)
        btn.bind("<Button-1>", click)
        register_widget(btn, 'button')

# --------- Applications Installing Tab Widgets ---------
apps_label = tk.Label(tab_apps, text="Applications Installing", font=("Arial", 20),
                      bg=THEMES['light']['label_bg'], fg=THEMES['light']['label_fg'])
apps_label.pack(pady=10)
register_widget(apps_label, 'label')

# Create a scrollable frame for app buttons
canvas = tk.Canvas(tab_apps, highlightthickness=0, bg=THEMES['light']['bg'])
scrollbar = ttk.Scrollbar(tab_apps, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=THEMES['light']['bg'])
register_widget(canvas, 'frame')
register_widget(scrollable_frame, 'frame')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --------- Installer Functions ---------
def download_file(url, filename):
    """Download a file and show progress"""
    try:
        downloads_folder = os.path.join(str(Path.home()), "Downloads")
        os.makedirs(downloads_folder, exist_ok=True)
        filepath = os.path.join(downloads_folder, filename)
        
        def download_with_progress(url, filepath):
            urllib.request.urlretrieve(url, filepath)
            return filepath
        
        filepath = download_with_progress(url, filepath)
        messagebox.showinfo("Download Complete", f"Downloaded: {filename}\nLocation: {filepath}")
        return filepath
    except Exception as e:
        messagebox.showerror("Download Error", f"Failed to download: {str(e)}")
        return None

def install_chrome():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://dl.google.com/chrome/install/googlechromestandaloneenterprise64.exe"
        filename = "GoogleChrome.exe"
    elif os_name == "Darwin":
        url = "https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg"
        filename = "GoogleChrome.dmg"
    elif os_name == "Linux":
        messagebox.showinfo("Chrome Install", "For Linux, use your package manager:\nsudo apt install google-chrome-stable")
        return
    else:
        url = "https://dl.google.com/chrome/install/googlechromestandaloneenterprise64.exe"
        filename = "GoogleChrome.exe"
    
    download_file(url, filename)

def install_discord():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
        filename = "Discord.exe"
    elif os_name == "Darwin":
        url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=osx&arch=x64"
        filename = "Discord.dmg"
    elif os_name == "Linux":
        messagebox.showinfo("Discord Install", "For Linux, use your package manager:\nsudo apt install discord")
        return
    else:
        url = "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64"
        filename = "Discord.exe"
    
    download_file(url, filename)

def install_vscode():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://code.visualstudio.com/sha/download?builds=stable&os=win32-x64&user_agent=continuous"
        filename = "VSCode.exe"
    elif os_name == "Darwin":
        url = "https://code.visualstudio.com/sha/download?builds=stable&os=darwin&user_agent=continuous"
        filename = "VSCode.zip"
    elif os_name == "Linux":
        url = "https://code.visualstudio.com/sha/download?builds=stable&os=linux-x64&user_agent=continuous"
        filename = "VSCode.tar.gz"
    else:
        url = "https://code.visualstudio.com/sha/download?builds=stable&os=win32-x64&user_agent=continuous"
        filename = "VSCode.exe"
    
    download_file(url, filename)

# --------- Game Launchers ---------
def install_steam():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe"
        filename = "SteamSetup.exe"
    elif os_name == "Darwin":
        url = "https://steamcdn-a.akamaihd.net/client/installer/steam.dmg"
        filename = "Steam.dmg"
    elif os_name == "Linux":
        messagebox.showinfo("Steam Install", "For Linux, use your package manager:\nsudo apt install steam")
        return
    else:
        url = "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe"
        filename = "SteamSetup.exe"
    
    download_file(url, filename)

def install_epic_games():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.exe"
        filename = "EpicGamesLauncher.exe"
    elif os_name == "Darwin":
        messagebox.showinfo("Epic Games", "Epic Games Launcher is not available on macOS")
        return
    elif os_name == "Linux":
        messagebox.showinfo("Epic Games", "Epic Games Launcher is not available on Linux")
        return
    else:
        url = "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.exe"
        filename = "EpicGamesLauncher.exe"
    
    download_file(url, filename)

def install_gog_galaxy():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://cdn.gog.com/open/galaxy/client/2.0.45.86/GOG%20Galaxy%202.0%20Setup.exe"
        filename = "GOGGalaxy.exe"
    elif os_name == "Darwin":
        messagebox.showinfo("GOG Galaxy", "GOG Galaxy is not available on macOS")
        return
    elif os_name == "Linux":
        messagebox.showinfo("GOG Galaxy", "GOG Galaxy is not available on Linux")
        return
    else:
        url = "https://cdn.gog.com/open/galaxy/client/2.0.45.86/GOG%20Galaxy%202.0%20Setup.exe"
        filename = "GOGGalaxy.exe"
    
    download_file(url, filename)

# --------- Utilities ---------
def install_powertoys():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://github.com/microsoft/PowerToys/releases/download/v0.81.1/PowerToysSetup-0.81.1-x64.exe"
        filename = "PowerToys.exe"
    else:
        messagebox.showinfo("PowerToys", "PowerToys is only available for Windows")
        return
    
    download_file(url, filename)

def install_7zip():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://7-zip.org/a/7z2407-x64.exe"
        filename = "7Zip.exe"
    elif os_name == "Darwin":
        messagebox.showinfo("7-Zip Install", "For macOS, use Homebrew:\nbrew install 7zip")
        return
    elif os_name == "Linux":
        messagebox.showinfo("7-Zip Install", "For Linux, use your package manager:\nsudo apt install p7zip-full")
        return
    else:
        url = "https://7-zip.org/a/7z2407-x64.exe"
        filename = "7Zip.exe"
    
    download_file(url, filename)

def install_vlc():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://get.videolan.org/vlc/last/win64/vlc-3.0.20-win64.exe"
        filename = "VLC.exe"
    elif os_name == "Darwin":
        url = "https://get.videolan.org/vlc/last/macosx/vlc-3.0.20.dmg"
        filename = "VLC.dmg"
    elif os_name == "Linux":
        messagebox.showinfo("VLC Install", "For Linux, use your package manager:\nsudo apt install vlc")
        return
    else:
        url = "https://get.videolan.org/vlc/last/win64/vlc-3.0.20-win64.exe"
        filename = "VLC.exe"
    
    download_file(url, filename)

def install_notepadpp():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.9/npp.8.6.9.Installer.x64.exe"
        filename = "Notepad++.exe"
    elif os_name == "Darwin":
        messagebox.showinfo("Notepad++", "For macOS, consider using: Sublime Text, Visual Studio Code, or Atom")
        return
    elif os_name == "Linux":
        messagebox.showinfo("Notepad++", "For Linux, use your package manager:\nsudo apt install notepadqq")
        return
    else:
        url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.9/npp.8.6.9.Installer.x64.exe"
        filename = "Notepad++.exe"
    
    download_file(url, filename)

def install_git():
    os_name = platform.system()
    if os_name == "Windows":
        url = "https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe"
        filename = "Git.exe"
    elif os_name == "Darwin":
        url = "https://sourceforge.net/projects/git-osx-installer/files/git-2.42.0-intel-universal-mavericks.dmg/download"
        filename = "Git.dmg"
    elif os_name == "Linux":
        messagebox.showinfo("Git Install", "For Linux, use your package manager:\nsudo apt install git")
        return
    else:
        url = "https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe"
        filename = "Git.exe"
    
    download_file(url, filename)

# --------- Installer Buttons ---------
chrome_btn = tk.Button(scrollable_frame, text="Install Google Chrome", command=install_chrome, width=20,
                       bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
chrome_btn.grid(row=0, column=0, padx=5, pady=5)
register_widget(chrome_btn, 'button')

discord_btn = tk.Button(scrollable_frame, text="Install Discord", command=install_discord, width=20,
                        bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
discord_btn.grid(row=0, column=1, padx=5, pady=5)
register_widget(discord_btn, 'button')

vscode_btn = tk.Button(scrollable_frame, text="Install Visual Studio Code", command=install_vscode, width=20,
                       bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
vscode_btn.grid(row=0, column=2, padx=5, pady=5)
register_widget(vscode_btn, 'button')

# Game Launchers
steam_btn = tk.Button(scrollable_frame, text="Install Steam", command=install_steam, width=20, bg="#1b2838", fg="#ffffff")
steam_btn.grid(row=1, column=0, padx=5, pady=5)
register_widget(steam_btn, 'special_button')

epic_btn = tk.Button(scrollable_frame, text="Install Epic Games", command=install_epic_games, width=20, bg="#2a2a2a", fg="#ffffff")
epic_btn.grid(row=1, column=1, padx=5, pady=5)
register_widget(epic_btn, 'special_button')

gog_btn = tk.Button(scrollable_frame, text="Install GOG Galaxy", command=install_gog_galaxy, width=20, bg="#323232", fg="#ffffff")
gog_btn.grid(row=1, column=2, padx=5, pady=5)
register_widget(gog_btn, 'special_button')

# Utilities
powertoys_btn = tk.Button(scrollable_frame, text="Install PowerToys", command=install_powertoys, width=20, bg="#0078d4", fg="#ffffff")
powertoys_btn.grid(row=2, column=0, padx=5, pady=5)
register_widget(powertoys_btn, 'special_button')

sevenzip_btn = tk.Button(scrollable_frame, text="Install 7-Zip", command=install_7zip, width=20,
                         bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
sevenzip_btn.grid(row=2, column=1, padx=5, pady=5)
register_widget(sevenzip_btn, 'button')

vlc_btn = tk.Button(scrollable_frame, text="Install VLC", command=install_vlc, width=20, bg="#ff8c00", fg="#ffffff")
vlc_btn.grid(row=2, column=2, padx=5, pady=5)
register_widget(vlc_btn, 'special_button')

notepad_btn = tk.Button(scrollable_frame, text="Install Notepad++", command=install_notepadpp, width=20,
                        bg=THEMES['light']['button_bg'], fg=THEMES['light']['button_fg'])
notepad_btn.grid(row=3, column=0, padx=5, pady=5)
register_widget(notepad_btn, 'button')

git_btn = tk.Button(scrollable_frame, text="Install Git", command=install_git, width=20, bg="#f05033", fg="#ffffff")
git_btn.grid(row=3, column=1, padx=5, pady=5)
register_widget(git_btn, 'special_button')


# --------- Run the App ---------
root.mainloop()
