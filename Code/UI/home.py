import tkinter as tk
import style
import os 


def display_home_content(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    # Getting the directory of the current script file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Correcting the path to the image
    logo_path = os.path.join(script_dir, 'assets', 'Zmeya.png')
    logo = tk.PhotoImage(file=logo_path)
    #logo = tk.PhotoImage(file='UI/assets/Zmeya.png')
    logo_label = tk.Label(main_frame, image=logo, bg=style.BACKGROUND_COLOR)
    welcome_label = tk.Label(main_frame, text="Welcome to Zmeya", **style.LABEL_STYLES)

    # Information section
    info_frame = tk.Frame(main_frame, bg=style.BACKGROUND_COLOR)  # Create a frame to hold info labels
    
    # Packing UI elements
    logo_label.image = logo  # Keep a reference to prevent garbage collection
    logo_label.pack(pady=(60, 20))
    welcome_label.pack(pady=20)
    
    # Packing information section
    info_frame.pack(pady=20, fill='x')

    
