import tkinter as tk
from tkinter import ttk
    # Themed Tk (Ttk) is a newer family of Tk widgets that provide a much 
    # better appearance on different platforms than many of the classic Tk widgets. 
from PIL import Image, ImageTk  # Pillow library to edit the image

# Functions to open different windows

def open_manual_scan():
    manual_scan_window = tk.Toplevel(startup)
    manual_scan_window.title("Manual Scan")
    ttk.Label(manual_scan_window, text="Manual Scan page").pack(padx=20, pady=20)

def open_scan_scheduler():
    scan_scheduler_window = tk.Toplevel(startup)
    scan_scheduler_window.title("Schedule Scan ")
    ttk.Label(scan_scheduler_window, text="Schedule Scan page").pack(padx=20, pady=20)

def open_settings():
    settings_window = tk.Toplevel(startup)
    settings_window.title("Settings")
    ttk.Label(settings_window, text="Settings page.").pack(padx=20, pady=20)

# Create the startup screen
startup = tk.Tk()  # Startup(root) window
startup.configure(bg='#FEF3E0') # Set the background color
startup.title("Zmeya") # The title of the Startup window 
start_label = tk.Label(startup, text="Hello, welcome to Zmeya!", bg="#FEF3E0", fg="#D35400", font=("Arial", 25))
start_label.grid(row=0, column=1, pady=20)
startup.geometry("800x600")  # Width x Height

# Place the Zmeya logo

def zmeya_img_bg(img_path, new_bg):
    # Change the background of the image
    img = Image.open(img_path)
    img = img.convert("RGBA") # Convert the image to  the "RGBA" mode
    new_img = Image.new("RGBA", img.size, new_bg + (255,))
    new_img.paste(img, (0, 0), img)
    return new_img

def border_remove(img_path, new_bg, border_size):
    # Remove the border of the image if needed
    img = zmeya_img_bg(img_path, new_bg)
    width, height = img.size
    left = border_size
    right = width - border_size
    top = border_size
    bottom = height - border_size
    new_img = img.crop((left, top, right, bottom))
    return new_img

# Final image after changing the background and size.
bg_color = (254, 243, 224)
img = border_remove("Zmeya.png", bg_color, 10)   
zmeya_img = ImageTk.PhotoImage(img)  

# Upload the image directly if nothing need to be modified
# zmeya_img = tk.PhotoImage(file="images/zmeya.gif")

zmeya_label = tk.Label(startup, image=zmeya_img, bg='#FEF3E0', padx=0, pady=0) # Display the zmeya image
zmeya_label.image = zmeya_img # Keep a reference
zmeya_label.grid(row=1, column=1)

# Buttons for Manual Scan, Schedule Scan and Settings
button_style = ttk.Style()
# print(button_style.theme_use())
button_style.configure("Custom.TButton", foreground="#D35400", font=("Arial", 15))
manual_scan_btn = ttk.Button(startup, text="Manual Scan", style="Custom.TButton", command=open_manual_scan, width=20)
scan_scheduler_btn = ttk.Button(startup, text="Schedule Scan",style="Custom.TButton", command=open_scan_scheduler, width=20)
settings_btn = ttk.Button(startup, text="Settings", style="Custom.TButton", command=open_settings, width=20)

# Position the buttons
manual_scan_btn.grid(row=2, column=0, padx=10, pady=10)
scan_scheduler_btn.grid(row=2, column=1, padx=10, pady=10)
settings_btn.grid(row=2, column=2, padx=10, pady=10)

# Start the main loop
startup.mainloop()
