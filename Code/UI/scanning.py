import tkinter as tk
import style
from Zmeya_Backend.ClamAV.custom_scan import CustomScan


def display_scanning(main_frame, update_main_frame, clear_main_frame):
    switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", **style.LABEL_STYLES)
    scan_page_title.pack(pady=20)

    btn_full_scan = tk.Button(main_frame, text="Full Scan", command=lambda: display_full_scan_options(update_main_frame), **style.BUTTON_STYLES)
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(update_main_frame), **style.BUTTON_STYLES)
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(update_main_frame), **style.BUTTON_STYLES)
    
    btn_full_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_schedule_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_custom_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)

def display_full_scan_options(update_main_frame):
    update_main_frame("Full Scan options will be displayed here")

def display_schedule_scan_options(update_main_frame):
    update_main_frame("Schedule Scan options will be displayed here")

def display_custom_scan_options(update_main_frame):
    def display_scanning(main_frame, update_main_frame, clear_main_frame):
        switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

    def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
        clear_main_frame()
        scan_page_title = tk.Label(main_frame, text="Scan Options", **style.LABEL_STYLES)
        scan_page_title.pack(pady=20)

        btn_full_scan = tk.Button(main_frame, text="Full Scan", command=lambda: display_full_scan_options(update_main_frame), **style.BUTTON_STYLES)
        btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(update_main_frame), **style.BUTTON_STYLES)
        btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(update_main_frame), **style.BUTTON_STYLES)
        
        btn_full_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
        btn_schedule_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
        btn_custom_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)

    def display_full_scan_options(update_main_frame):
        update_main_frame("Full Scan options will be displayed here")

    def display_schedule_scan_options(update_main_frame):
        update_main_frame("Schedule Scan options will be displayed here")

    def display_custom_scan_options(update_main_frame):
        # Call the backend function to perform a custom scan
        CustomScan(path_to_file, path_to_logs, path_to_quarantine)
        update_main_frame("Custom Drive Scan options will be displayed here")

