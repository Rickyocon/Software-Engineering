import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import scanning
import settings
import quarantine
import home
import style

def update_main_frame(content):
    for widget in main_frame.winfo_children():
        widget.destroy()
    content_label = tk.Label(main_frame, text=content, **style.LABEL_STYLES)
    content_label.pack(pady=20)

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Initialize main window
root = tk.Tk()
root.title("Zmeya Anti-Malware")
root.configure(bg=style.BACKGROUND_COLOR)

side_frame = tk.Frame(root, bg=style.SIDE_FRAME_COLOR)
side_frame.pack(side='left', fill='y', padx=style.PAD_X)

btn_settings = tk.Button(side_frame, text="Settings", command=lambda: settings.display_settings(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
btn_scanning = tk.Button(side_frame, text="Scanning", command=lambda: scanning.display_scanning(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
btn_quarantine = tk.Button(side_frame, text="Quarantine", command=lambda: quarantine.display_quarantine(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
btn_home = tk.Button(side_frame, text="Home", command=lambda: home.display_home_content(main_frame), **style.BUTTON_STYLES)

btn_settings.pack(pady=style.PAD_Y, padx=style.PAD_X)
btn_scanning.pack(pady=style.PAD_Y, padx=style.PAD_X)
btn_quarantine.pack(pady=style.PAD_Y, padx=style.PAD_X)
btn_home.pack(side='bottom', pady=(0, 10), padx=style.PAD_X)

main_frame = tk.Frame(root, bg=style.BACKGROUND_COLOR)
main_frame.pack(side='right', expand=True, fill='both')

home.display_home_content(main_frame)

root.mainloop()

