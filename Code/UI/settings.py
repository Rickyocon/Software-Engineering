import tkinter as tk
import subprocess
import style
from themes import themes

def display_settings(main_frame, update_main_frame, clear_main_frame, apply_theme):
    clear_main_frame()

    # Title Label
    title_label = tk.Label(main_frame, text="Settings", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Update Signatures Function
    def update_signatures():
        try:
            subprocess.run(["freshclam.exe"], check=True)
            update_main_frame("Signature update successful.")
        except subprocess.CalledProcessError as e:
            update_main_frame(f"Signature update failed: {str(e)}")

    # Update Signatures Button
    btn_update_signatures = tk.Button(main_frame, text="Update Signatures", command=update_signatures, **style.BUTTON_STYLES)
    btn_update_signatures.pack(pady=style.PAD_Y)

    # Theme Selection Label
    theme_label = tk.Label(main_frame, text="Change Theme:", **style.LABEL_STYLES)
    theme_label.pack(pady=style.PAD_Y)

    # Theme Selection Drop Down
    theme_var = tk.StringVar(main_frame)
    theme_var.set("Select Theme")  # Default value
    theme_dropdown = tk.OptionMenu(main_frame, theme_var, *themes.keys())
    theme_dropdown.pack(pady=style.PAD_Y)

    # Submit Button for theme change
    def submit_theme():
        chosen_theme = theme_var.get()
        if chosen_theme != "Select Theme":
            apply_theme(chosen_theme)
            update_main_frame(f"Theme changed to {chosen_theme}")

    submit_btn = tk.Button(main_frame, text="Submit", command=submit_theme, **style.BUTTON_STYLES)
    submit_btn.pack(pady=style.PAD_Y)

