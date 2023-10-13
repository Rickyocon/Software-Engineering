import tkinter as tk

def display_scanning(main_frame, update_main_frame, clear_main_frame):
    switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", bg='#202A44', fg='white', font='Helvetica 16 bold')
    scan_page_title.pack(pady=20)

    btn_quick_scan = tk.Button(main_frame, text="Quick Scan", command=lambda: display_quick_scan_options(update_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(update_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(update_main_frame), bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    
    btn_quick_scan.pack(pady=10, padx=10)
    btn_schedule_scan.pack(pady=10, padx=10)
    btn_custom_scan.pack(pady=10, padx=10)

def display_quick_scan_options(update_main_frame):
    update_main_frame("Quick Scan options will be displayed here")

def display_schedule_scan_options(update_main_frame):
    update_main_frame("Schedule Scan options will be displayed here")

def display_custom_scan_options(update_main_frame):
    update_main_frame("Custom Drive Scan options will be displayed here")
