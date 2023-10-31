import tkinter as tk
from tkinter import filedialog
import style
from Zmeya_Backend.ClamAV.fullscan import customScan, fullScan

def display_scanning(main_frame, update_main_frame, clear_main_frame):
    switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", **style.LABEL_STYLES)
    scan_page_title.pack(pady=20)

    btn_full_scan = tk.Button(main_frame, text="Full Scan", command=lambda: display_full_scan_options(update_main_frame), **style.BUTTON_STYLES)
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(update_main_frame), **style.BUTTON_STYLES)
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)

   
    btn_full_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_schedule_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_custom_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)

def display_full_scan_options(update_main_frame):
    update_main_frame("Full Scan options will be displayed here")

def display_schedule_scan_options(update_main_frame):
    update_main_frame("Schedule Scan options will be displayed here")
 
def display_custom_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    # Title Label
    custom_scan_title = tk.Label(main_frame, text="Custom Drive Scan", **style.LABEL_STYLES)
    custom_scan_title.pack(pady=20)

    # Scan Target Selection
    lbl_scan_target = tk.Label(main_frame, text="Select Drive/Folder to Scan:", **style.LABEL_STYLES)
    lbl_scan_target.pack(pady=style.PAD_Y)
    entry_scan_target = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_scan_target.pack(pady=style.PAD_Y)
    btn_browse = tk.Button(main_frame, text="Browse", command=lambda: browse_target(entry_scan_target), **style.BUTTON_STYLES)
    btn_browse.pack(pady=style.PAD_Y)

    # Optional Log File Path
    lbl_log_path = tk.Label(main_frame, text="Optional: Log File Path:", **style.LABEL_STYLES)
    lbl_log_path.pack(pady=style.PAD_Y)
    entry_log_path = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_log_path.pack(pady=style.PAD_Y)
    btn_browse = tk.Button(main_frame, text="Browse", command=lambda: browse_target(entry_scan_target), **style.BUTTON_STYLES)
    btn_browse.pack(pady=style.PAD_Y)

    # Start Scan Button
    btn_start_scan = tk.Button(main_frame, text="Start Scan", command=lambda: start_scan(entry_scan_target.get(), entry_log_path.get()), **style.BUTTON_STYLES)
    btn_start_scan.pack(pady=style.PAD_Y)

    # Function to browse for a file/folder
    def browse_target(entry_widget):
        folder_selected = filedialog.askdirectory()  # For directory
        # file_selected = filedialog.askopenfilename()  # For file selection, if you need
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)

    # Function to start the scan
    def start_scan(scan_target, log_path):
        if not scan_target:
            update_main_frame("Error: Please select a drive or file to scan.")
            # Back Button
            btn_back = tk.Button(main_frame, text="Back", command=lambda: display_custom_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
            btn_back.pack(pady=style.PAD_Y, padx=style.PAD_X)
            return
        log_path = log_path if log_path else None  # Use None if no log path is specified
        customScan([scan_target], log_path, None)  # Assuming quarantine path is not used here
        update_main_frame(f"Scanning {scan_target}...")  # Update the UI to show scanning
