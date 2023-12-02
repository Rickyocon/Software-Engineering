import tkinter as tk
from tkinter import filedialog
import style
import threading
from Zmeya_Backend.core import customScan
from Zmeya_Backend.core import fullScan

def display_scanning(main_frame, update_main_frame, clear_main_frame):
    switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", **style.LABEL_STYLES)
    scan_page_title.pack(pady=20)

    btn_full_scan = tk.Button(main_frame, text="Full system scan", command=lambda: display_full_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)

   
    btn_full_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_schedule_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_custom_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    
    
def display_full_scan_options(main_frame, update_main_frame, clear_main_frame):
    # Clear the main frame
    clear_main_frame()

    # Title Label for Full Scan Page
    full_scan_title = tk.Label(main_frame, text="Full System Scan", font=("Helvetica", 16), bg="#202A44", fg="white")
    full_scan_title.pack(pady=20)

    # Scan Status Label
    scan_status_label = tk.Label(main_frame, text="", font=("Helvetica", 12), bg="#202A44", fg="white")
    scan_status_label.pack(pady=20)

    # Start Scan Button Function
    def start_full_scan():
        # Placeholder paths for log and quarantine. Modify as needed.
        log_path = "path_to_log_directory"
        quarantine_path = "path_to_quarantine_directory"

        # Update UI with scan status
        scan_status_label.config(text="Scanning... Please wait.")
        main_frame.update()

        # Start full scan
        fullScan(log_path, quarantine_path)

        # Update UI post scan
        scan_status_label.config(text="Scan Complete. Check logs for details.")

    # Start Scan Button
    start_scan_btn = tk.Button(main_frame, text="Start Full Scan", command=start_full_scan, bg="light blue", font=("Helvetica", 12))
    start_scan_btn.pack(pady=10)

# This function can be called from the relevant part of your main UI.
# Example: When the user clicks the 'Full Scan' button on the scanning page, call `display_full_scan_options`.


def display_schedule_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    # Title Label
    title_label = tk.Label(main_frame, text="Schedule Scan", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Input for days
    lbl_days = tk.Label(main_frame, text="Enter days (e.g., Mon,Tue,Wed):", **style.LABEL_STYLES)
    lbl_days.pack(pady=style.PAD_Y)
    entry_days = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_days.pack(pady=style.PAD_Y)

    # Input for frequency
    lbl_frequency = tk.Label(main_frame, text="Enter frequency (in days):", **style.LABEL_STYLES)
    lbl_frequency.pack(pady=style.PAD_Y)
    entry_frequency = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_frequency.pack(pady=style.PAD_Y)

    # Input for time
    lbl_time = tk.Label(main_frame, text="Enter time (HH:MM):", **style.LABEL_STYLES)
    lbl_time.pack(pady=style.PAD_Y)
    entry_time = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_time.pack(pady=style.PAD_Y)

    # Path Selections (scan path, log path, quarantine path)
    # Similar to what you have in the custom scan UI

    # Schedule Button
    btn_schedule = tk.Button(main_frame, text="Schedule Scan", command=lambda: schedule_scan(entry_days.get(), entry_frequency.get(), entry_time.get()), **style.BUTTON_STYLES)
    btn_schedule.pack(pady=style.PAD_Y)

    # Function to handle the scheduling
    def schedule_scan(days, frequency, time):
        # You'll need to implement the logic to handle the scheduling based on the inputs
        pass
 
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

    lbl_log_path = tk.Label(main_frame, text="Optional: Log File Path:", **style.LABEL_STYLES)
    lbl_log_path.pack(pady=style.PAD_Y)
    entry_log_path = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_log_path.pack(pady=style.PAD_Y)
    btn_browse_log = tk.Button(main_frame, text="Browse Log", command=lambda: browse_log_path(entry_log_path), **style.BUTTON_STYLES)
    btn_browse_log.pack(pady=style.PAD_Y)

    # Start Scan Button
    btn_start_scan = tk.Button(main_frame, text="Start Scan", command=lambda: start_scan(entry_scan_target.get(), entry_log_path.get()), **style.BUTTON_STYLES)
    btn_start_scan.pack(pady=style.PAD_Y)

    # Function to browse for a file/folder
    def browse_target(entry_widget):
        folder_selected = filedialog.askdirectory()  # For directory
        # file_selected = filedialog.askopenfilename()  # For file selection, if you need
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)
        
    # Function to browse for a log file path
    def browse_log_path(entry_widget):
        folder_selected = filedialog.askdirectory()  # For directory
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