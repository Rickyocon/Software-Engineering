import os
import shutil
import tkinter as tk
from tkinter import messagebox
from core import path_format, customPath

def quarantine_options(lPath,qPath):
    root = tk.Tk()
    root.title("Quarantine Options")

    if qPath:
        qPath = path_format(qPath)
    else:
        qfolder = "Zmeya_quarantine"
        qPath = customPath(qfolder)

    def delete():
        qFolders = [os.path.join(qPath, folder) for folder in os.listdir(qPath) if os.path.isdir(os.path.join(qPath, folder))]
        if qFolders:
            target_qFolder = max(qFolders, key=os.path.getctime)
            shutil.rmtree(target_qFolder)
            messagebox.showinfo("Infected files were deleted successfully!")
        else:
            messagebox.showinfo("Nothing to delete.")
    def whitelist():
        # Implement logic to move the file to the whitelist
        # You may want to move the most recent folder or specific files

        # Example: Move the entire quarantine folder to the whitelist
        whitelist_path = "/path/to/whitelist"
        if not os.path.exists(whitelist_path):
            os.makedirs(whitelist_path, exist_ok=True)

        shutil.move(qPath, os.path.join(whitelist_path, os.path.basename(qPath)))
        messagebox.showinfo("File(s) marked as safe.")

    def cancel():
        root.destroy()

    virus_count = virus_count(lPath)
    if virus_count > 0:
        tk.Label(root, text="Quarantine Options").pack()

        btn_delete = tk.Button(root, text="Delete", command=delete)
        btn_delete.pack()

        btn_mark_safe = tk.Button(root, text="Mark as Safe", command=whitelist)
        btn_mark_safe.pack()

        btn_exit = tk.Button(root, text="Cancel", command=cancel)
        btn_exit.pack()

    else:
        messagebox.showinfo("Scan finished! No viruses found.")

    root.mainloop()

