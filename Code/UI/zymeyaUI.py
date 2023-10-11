import tkinter as tk
from tkinter import messagebox

# Function to display settings page
def display_settings():
    update_main_frame("Settings will be displayed here")

# Function to display scanning options page
def display_scanning():
    update_main_frame("Choose a scan option:")
    # Buttons for different scanning options with a temporary popup on click
    btn_quick_scan = tk.Button(main_frame, text="Quick Scan", command=show_temp_popup, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=show_temp_popup, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=show_temp_popup, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_quick_scan.pack(pady=10, padx=10)
    btn_schedule_scan.pack(pady=10, padx=10)
    btn_custom_scan.pack(pady=10, padx=10)

# Function to display options page
def display_options():
    update_main_frame("Options will be configured here")

# Function to display quarantine page
def display_quarantine():
    update_main_frame("Quarantine will be managed here")

# Function to display home page with logo and welcome message
def display_home():
    for widget in main_frame.winfo_children():
        widget.destroy()
    logo = tk.PhotoImage(file='Code/UI/zmeya.gif')
    logo_label = tk.Label(main_frame, image=logo, bg='#202A44')
    logo_label.image = logo # Keep a reference to prevent garbage collection
    welcome_label = tk.Label(main_frame, text="Welcome to Zmeya", bg='#202A44', fg='white', font='Helvetica 16 bold')
    logo_label.pack(pady=(60, 20))
    welcome_label.pack(pady=20)

# Temporary function to show a popup message
def show_temp_popup():
    messagebox.showinfo("Information", "Temp")

# Function to update main frame's content
def update_main_frame(content):
    for widget in main_frame.winfo_children():
        widget.destroy()
    if content:
        tk.Label(main_frame, text=content, bg='#202A44', fg='white', font='Helvetica 12 bold').pack(pady=20)

# Main application window
root = tk.Tk()
root.title("Zmeya Anti-Malware")
root.configure(bg='#202A44')

# Frame for navigation buttons
side_frame = tk.Frame(root, bg='#293B5A')
side_frame.pack(side='left', fill='y', padx=(0, 20))

# Navigation buttons to switch between pages
btn_settings = tk.Button(side_frame, text="Settings", command=display_settings, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_scanning = tk.Button(side_frame, text="Scanning", command=display_scanning, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_options = tk.Button(side_frame, text="Options", command=display_options, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_quarantine = tk.Button(side_frame, text="Quarantine", command=display_quarantine, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_home = tk.Button(side_frame, text="Home", command=display_home, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')

# Packing navigation buttons to the side frame
btn_settings.pack(pady=10, padx=10)
btn_scanning.pack(pady=10, padx=10)
btn_options.pack(pady=10, padx=10)
btn_quarantine.pack(pady=10, padx=10)
btn_home.pack(side='bottom', pady=(0, 10), padx=10)

# Main content frame
main_frame = tk.Frame(root, bg='#202A44')
main_frame.pack(side='right', expand=True, fill='both')

# Logo and welcome message labels
logo = tk.PhotoImage(file='Code/UI/zmeya.gif')
logo_label = tk.Label(main_frame, image=logo, bg='#202A44')
welcome_label = tk.Label(main_frame, text="Welcome to Zmeya", bg='#202A44', fg='white', font='Helvetica 16 bold')

# Displaying logo and welcome message at startup
logo_label.pack(pady=(60, 20))
welcome_label.pack(pady=20)

# Starting the main application loop
root.mainloop()
