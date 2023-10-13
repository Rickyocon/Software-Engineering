import tkinter as tk
import style

def display_home_content(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
    logo = tk.PhotoImage(file='Code/UI/assets/Zmeya.png')  # Ensure path is correct
    logo_label = tk.Label(main_frame, image=logo, bg=style.BACKGROUND_COLOR)
    welcome_label = tk.Label(main_frame, text="Welcome to Zmeya", **style.LABEL_STYLES)

    logo_label.image = logo  # Keep a reference to prevent garbage collection
    logo_label.pack(pady=(60, 20))
    welcome_label.pack(pady=20)
