import subprocess
from tkinter import messagebox


# Excute freshclam.exe
def freshClam():
    try:
        subprocess.run(["freshclam.exe"])
        messagebox.showinfo("Virus database updated successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror(f"Signature update failed with error: {e}")