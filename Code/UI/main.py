import tkinter as tk
import scanning
import settings
import quarantine
import home
import style
from PIL import Image, ImageTk #pillow for images


# Initialize main window
root = tk.Tk()
root.title("Zmeya Anti-Malware")
root.configure(bg=style.BACKGROUND_COLOR) #uncommented it to fix the issue with bg colors under logo/txt

# Loading images as png. 
home_button_image_png = Image.open('Code/UI/assets/Home.png')
scanning_button_image_png = Image.open("Code/UI/assets/Scanning.png")
quarantine_button_image_png = Image.open('Code/UI/assets/Quarantine.png')
settings_button_image_png = Image.open('Code/UI/assets/Settings.png')

# Convert PNG images for tkinter
home_button_image = ImageTk.PhotoImage(home_button_image_png)
scanning_button_image = ImageTk.PhotoImage(scanning_button_image_png)
quarantine_button_image = ImageTk.PhotoImage(quarantine_button_image_png)
settings_button_image = ImageTk.PhotoImage(settings_button_image_png)


def update_main_frame(content):
    for widget in main_frame.winfo_children():
        widget.destroy()
    content_label = tk.Label(main_frame, text=content, **style.LABEL_STYLES)
    content_label.pack(pady=20)

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

side_frame = tk.Frame(root, bg=style.SIDE_FRAME_COLOR)
side_frame.pack(side='left', fill='y', padx=style.PAD_X)

#attempting using tk.Button - transparent bg becomes white while running the program
"""
#creating buttons using the images we uploaded
btn_settings = tk.Button(
    side_frame, 
    image=settings_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    activebackground=style.SIDE_FRAME_COLOR,
    highlightthickness=0,
    command=lambda: settings.display_settings(update_main_frame)
)

btn_scanning = tk.Button(
    side_frame, 
    image=scanning_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    activebackground=style.SIDE_FRAME_COLOR,
    highlightthickness=0,
    command=lambda: scanning.display_scanning(main_frame, update_main_frame, clear_main_frame)
)

btn_quarantine = tk.Button(
    side_frame, 
    image=quarantine_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    activebackground=style.SIDE_FRAME_COLOR,
    highlightthickness=0,
    command=lambda: quarantine.display_quarantine(update_main_frame)
)

btn_home = tk.Button(
    side_frame, 
    image=home_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    activebackground=style.SIDE_FRAME_COLOR,
    highlightthickness=0,
    command=lambda: home.display_home_content(main_frame)
)
"""


# Creating buttons using the images we uploaded
# Using Label widget and binding a click event
'''Using a tk.Label with images ensures better transparency
 handling than tk.Button. By binding a click event to the label, 
 we make it act like a button without losing image quality.
 
 after running worked well, however the "transparent" territory  acts as a button too'''


btn_settings = tk.Label(
    side_frame,
    image=settings_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    highlightthickness=0
)
btn_settings.bind("<Button-1>", lambda event: settings.display_settings(update_main_frame))

btn_scanning = tk.Label(
    side_frame,
    image=scanning_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    highlightthickness=0
)
btn_scanning.bind("<Button-1>", lambda event: scanning.display_scanning(main_frame, update_main_frame, clear_main_frame))

btn_quarantine = tk.Label(
    side_frame,
    image=quarantine_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    highlightthickness=0
)
btn_quarantine.bind("<Button-1>", lambda event: quarantine.display_quarantine(update_main_frame))

btn_home = tk.Label(
    side_frame,
    image=home_button_image,
    relief=tk.FLAT,
    borderwidth=0,
    bg=style.SIDE_FRAME_COLOR,
    highlightthickness=0
)
btn_home.bind("<Button-1>", lambda event: home.display_home_content(main_frame))

btn_settings.pack(pady=10)
btn_scanning.pack(pady=10)
btn_quarantine.pack(pady=10)
btn_home.pack(side='bottom', pady=10)

main_frame = tk.Frame(root, bg=style.BACKGROUND_COLOR) # set background color for mainframe here too to ensure consistency
main_frame.pack(side='right', expand=True, fill='both')

home.display_home_content(main_frame)

root.mainloop()

