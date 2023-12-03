import tkinter as tk
from tkinter import Listbox, messagebox
import style
import os
from Zmeya_Backend.qOptions import delete
from Zmeya_Backend.core import customPath, lock, unlock, relock, peek

def display_quarantine(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    # Function to get quarantined files
    def get_quarantined_files():
        qPath = customPath("Zmeya_quarantine")  # Get quarantine path
        return os.listdir(qPath)

    quarantine_title = tk.Label(main_frame, text="Quarantine Management", **style.LABEL_STYLES)
    quarantine_title.pack(pady=style.PAD_Y)

    # Listbox to display quarantined files
    lb_quarantined_files = Listbox(main_frame)
    lb_quarantined_files.pack(pady=style.PAD_Y)

    # Populate listbox with quarantined files
    for file in get_quarantined_files():
        lb_quarantined_files.insert(tk.END, file)

    # Action buttons
    btn_decrypt = tk.Button(main_frame, text="Unlock", command=lambda: decrypt_file(lb_quarantined_files.get(tk.ACTIVE)), **style.BUTTON_STYLES)
    btn_relock = tk.Button(main_frame, text="Relock", command=lambda: relock_file(lb_quarantined_files.get(tk.ACTIVE)), **style.BUTTON_STYLES)
    btn_decrypt.pack(pady=style.PAD_Y)
    btn_relock.pack(pady=style.PAD_Y)

    # Functions for file actions
    def decrypt_file(file_name):
        pass

    def relock_file(file_name):
        pass

    
    def delete_quarantine():
        delete(None)  # Assuming None will use the default quarantine path
        quarantine_status_label.config(text="Most recent quarantine deleted.")
        main_frame.update_idletasks()

    # Button to delete the most recent quarantine folder
    btn_delete_recent = tk.Button(main_frame, text="Delete Quarantined file", command=delete_quarantine, **style.BUTTON_STYLES)
    btn_delete_recent.pack(pady=style.PAD_Y)

    quarantine_status_label = tk.Label(main_frame, text="", **style.LABEL_STYLES)
    quarantine_status_label.pack(pady=20)