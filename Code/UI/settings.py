import tkinter as tk
import style
from Zmeya_Backend.ClamAV.signature_updates import freshClam

def display_settings(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    # Title Label
    title_label = tk.Label(main_frame, text="Settings", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Update Signatures Button
    btn_update_signatures = tk.Button(main_frame, text="Update Signatures", command=freshClam, **style.BUTTON_STYLES)
    btn_update_signatures.pack(pady=style.PAD_Y)

    pass

