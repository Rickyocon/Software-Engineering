import tkinter as tk
import scanning
import settings
import quarantine
import home

def update_main_frame(content):
    for widget in main_frame.winfo_children():
        widget.destroy()
    content_label = tk.Label(main_frame, text=content, bg='#202A44', fg='white', font='Helvetica 16 bold')
    content_label.pack(pady=20)

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Initialize main window
root = tk.Tk()
root.title("Zmeya Anti-Malware")
root.configure(bg='#202A44')

side_frame = tk.Frame(root, bg='#293B5A')
side_frame.pack(side='left', fill='y', padx=(0, 20))

btn_settings = tk.Button(side_frame, text="Settings", command=lambda: settings.display_settings(update_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_scanning = tk.Button(side_frame, text="Scanning", command=lambda: scanning.display_scanning(main_frame, update_main_frame, clear_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_quarantine = tk.Button(side_frame, text="Quarantine", command=lambda: quarantine.display_quarantine(update_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_home = tk.Button(side_frame, text="Home", command=lambda: home.display_home_content(main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')

btn_settings.pack(pady=10, padx=10)
btn_scanning.pack(pady=10, padx=10)
btn_quarantine.pack(pady=10, padx=10)
btn_home.pack(side='bottom', pady=(0, 10), padx=10)

main_frame = tk.Frame(root, bg='#202A44')
main_frame.pack(side='right', expand=True, fill='both')

home.display_home_content(main_frame)

root.mainloop()
