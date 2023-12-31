import tkinter as tk
from tkinter import Listbox, filedialog, Frame
import style
import os
from Zmeya_Backend.qOptions import delete
from Zmeya_Backend.core import customPath, unlock, relock

def display_quarantine(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    def get_quarantined_files(qPath):
        default_qPath = customPath("Zmeya_quarantine")
        valid_qPath = qPath if qPath and os.path.exists(qPath) else default_qPath
        return os.listdir(valid_qPath)

    quarantine_title = tk.Label(main_frame, text="Quarantine Management", **style.LABEL_STYLES)
    quarantine_title.pack(pady=style.PAD_Y)

    # Frame for quarantine path selection
    frame_quarantine_path = Frame(main_frame)
    frame_quarantine_path.pack(pady=style.PAD_Y)
    lbl_quarantine_path = tk.Label(frame_quarantine_path, text="Quarantine Folder Path:", **style.LABEL_STYLES)
    lbl_quarantine_path.pack(side=tk.LEFT)
    entry_quarantine_path = tk.Entry(frame_quarantine_path, **style.ENTRY_STYLES)
    entry_quarantine_path.insert(0, customPath("Zmeya_quarantine"))  # Default path
    entry_quarantine_path.pack(side=tk.LEFT)
    btn_browse_quarantine = tk.Button(frame_quarantine_path, text="Browse", command=lambda: browse_quarantine_path(entry_quarantine_path), **style.BUTTON_STYLES)
    btn_browse_quarantine.pack(side=tk.LEFT)

    def browse_quarantine_path(entry_widget):
        selected_path = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, selected_path)

    # Listbox to display quarantined files
    lb_quarantined_files = Listbox(main_frame)
    lb_quarantined_files.pack(pady=style.PAD_Y)

    # Button to refresh the list of quarantined files
    btn_refresh = tk.Button(main_frame, text="Refresh List", command=lambda: refresh_list(entry_quarantine_path.get(), lb_quarantined_files), **style.BUTTON_STYLES)
    btn_refresh.pack(pady=style.PAD_Y)

    def refresh_list(qPath, listbox):
        listbox.delete(0, tk.END)
        if qPath:  # Check if the path is not empty
            try:
                for file in get_quarantined_files(qPath):
                    listbox.insert(tk.END, file)
            except FileNotFoundError as e:
                quarantine_status_label.config(text=f"Error: {e}")
        else:
            quarantine_status_label.config(text="Please specify a quarantine path.")
        main_frame.update_idletasks()

    # Function to decrypt (unlock) a file
    def decrypt_file(file_name):
        if file_name:
            qPath = entry_quarantine_path.get()
            try:
                unlock(qPath, file_name)
                quarantine_status_label.config(text=f"File '{file_name}' decrypted.")
            except Exception as e:
                quarantine_status_label.config(text=f"Error decrypting file: {e}")
        else:
            quarantine_status_label.config(text="No file selected for decryption.")
        main_frame.update_idletasks()

    # Function to re-encrypt (relock) a file
    def relock_file(file_name):
        if file_name:
            qPath = entry_quarantine_path.get()
            try:
                relock(qPath, file_name)
                quarantine_status_label.config(text=f"File '{file_name}' re-encrypted.")
            except Exception as e:
                quarantine_status_label.config(text=f"Error re-encrypting file: {e}")
        else:
            quarantine_status_label.config(text="No file selected for re-encryption.")
        main_frame.update_idletasks()

    # Action buttons
    btn_decrypt = tk.Button(main_frame, text="Unlock", command=lambda: decrypt_file(lb_quarantined_files.get(tk.ACTIVE)), **style.BUTTON_STYLES)
    btn_relock = tk.Button(main_frame, text="Relock", command=lambda: relock_file(lb_quarantined_files.get(tk.ACTIVE)), **style.BUTTON_STYLES)
    btn_decrypt.pack(pady=style.PAD_Y)
    btn_relock.pack(pady=style.PAD_Y)

    def delete_quarantine():
        selected_qPath = entry_quarantine_path.get()
        if selected_qPath and os.path.exists(selected_qPath):
            # Call the delete function with the selected quarantine path
            delete(selected_qPath)
            quarantine_status_label.config(text="Quarantine folder deleted.")
        else:
            # If no path is selected or if the path doesn't exist, use the default path
            delete(None)  # This will use the default quarantine path
            quarantine_status_label.config(text="Most recent quarantine folder deleted.")
        main_frame.update_idletasks()
        refresh_list(entry_quarantine_path.get(), lb_quarantined_files)  # Refresh the list to reflect changes


    # Button to delete the most recent quarantine folder
    btn_delete_recent = tk.Button(main_frame, text="Delete Quarantined file", command=delete_quarantine, **style.BUTTON_STYLES)
    btn_delete_recent.pack(pady=style.PAD_Y)

    quarantine_status_label = tk.Label(main_frame, text="", **style.LABEL_STYLES)
    quarantine_status_label.pack(pady=20)

    # Initial population of the listbox
    refresh_list(entry_quarantine_path.get(), lb_quarantined_files)

