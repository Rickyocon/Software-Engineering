import tkinter as tk
from tkinter import filedialog
from tkcalendar import DateEntry
import sys
import os
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Zmeya_Backend.core import customScan, fullScan, run_scheduler
import subprocess
import scanning
import settings
import quarantine
import home
import style

def apply_theme(theme_name):
    global root, side_frame, main_frame
    style.current_theme = theme_name
    style.update_styles()

    root.configure(bg=style.BACKGROUND_COLOR)
    side_frame.configure(bg=style.SIDE_FRAME_COLOR)
    main_frame.configure(bg=style.BACKGROUND_COLOR)
    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(style.LABEL_STYLES)
        elif isinstance(widget, tk.Button):
            widget.config(style.BUTTON_STYLES)
        elif isinstance(widget, tk.Entry):
            widget.config(style.ENTRY_STYLES)
        elif isinstance(widget, tk.Frame):
            widget.config(style.FRAME_STYLES)
        elif isinstance(widget, tk.Text):
            widget.config(style.TEXT_STYLES)
        elif isinstance(widget, tk.Checkbutton):
            widget.config(style.CHECKBUTTON_STYLES)
        elif isinstance(widget, tk.Radiobutton):
            widget.config(style.RADIOBUTTON_STYLES)
        elif isinstance(widget, tk.Listbox):
            widget.config(style.LISTBOX_STYLES)
        elif isinstance(widget, tk.Scrollbar):
            widget.config(style.SCROLLBAR_STYLES)

    # Additionally, if you have widgets in side_frame, update them as well
    for widget in side_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(style.LABEL_STYLES)
        elif isinstance(widget, tk.Button):
            widget.config(style.BUTTON_STYLES)
        elif isinstance(widget, tk.Entry):
            widget.config(style.ENTRY_STYLES)
        elif isinstance(widget, tk.Frame):
            widget.config(style.FRAME_STYLES)
        elif isinstance(widget, tk.Text):
            widget.config(style.TEXT_STYLES)
        elif isinstance(widget, tk.Checkbutton):
            widget.config(style.CHECKBUTTON_STYLES)
        elif isinstance(widget, tk.Radiobutton):
            widget.config(style.RADIOBUTTON_STYLES)
        elif isinstance(widget, tk.Listbox):
            widget.config(style.LISTBOX_STYLES)
        elif isinstance(widget, tk.Scrollbar):
            widget.config(style.SCROLLBAR_STYLES)

        
        side_frame.configure(bg=style.SIDE_FRAME_COLOR)
        home.display_home_content(main_frame)


    def update_main_frame(content):
        for widget in main_frame.winfo_children():
            widget.destroy()
        content_label = tk.Label(main_frame, text=content, **style.LABEL_STYLES)
        content_label.pack(pady=20)

    def clear_main_frame():
        for widget in main_frame.winfo_children():
            widget.destroy()

    def create_side_buttons():
        global btn_settings, btn_scanning, btn_quarantine, btn_home

        btn_settings = tk.Button(side_frame, text="Settings", command=lambda: settings.display_settings(main_frame, update_main_frame, clear_main_frame, apply_theme), **style.BUTTON_STYLES)
        btn_scanning = tk.Button(side_frame, text="Scanning", command=lambda: scanning.display_scanning(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
        btn_quarantine = tk.Button(side_frame, text="Quarantine", command=lambda: quarantine.display_quarantine(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
        btn_home = tk.Button(side_frame, text="Home", command=lambda: home.display_home_content(main_frame), **style.BUTTON_STYLES)

        btn_settings.pack(pady=style.PAD_Y, padx=style.PAD_X)
        btn_scanning.pack(pady=style.PAD_Y, padx=style.PAD_X)
        btn_quarantine.pack(pady=style.PAD_Y, padx=style.PAD_X)
        btn_home.pack(side='bottom', pady=(0, 10), padx=style.PAD_X)


    # Initialize and pack side and main frames
    side_frame = tk.Frame(root, bg=style.SIDE_FRAME_COLOR)
    side_frame.pack(side='left', fill='y')

    main_frame = tk.Frame(root, bg=style.BACKGROUND_COLOR)
    main_frame.pack(side='right', expand=True, fill='both')

    # Populate side frame with buttons
    create_side_buttons()
    home.display_home_content(main_frame)
    root.mainloop()

    def main():
        root = tk.Tk()
        root.title("Zmeya Anti-Malware")
        apply_theme('default')

        side_frame = tk.Frame(root, bg=style.SIDE_FRAME_COLOR)
        side_frame.pack(side='left', fill='y')

        main_frame = tk.Frame(root, bg=style.BACKGROUND_COLOR)
        main_frame.pack(side='right', expand=True, fill='both')

        create_side_buttons(side_frame, main_frame)
        home.display_home_content(main_frame)

        root.mainloop()

    if __name__ == "__main__":
        main()