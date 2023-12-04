import tkinter as tk
from tkinter import filedialog
import threading
from tkcalendar import DateEntry
import style
from Zmeya_Backend.core import (
    customScan,
    fullScan,
)
def display_scanning(main_frame, update_main_frame, clear_main_frame):
    switch_to_scan_page(main_frame, update_main_frame, clear_main_frame)

def switch_to_scan_page(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", **style.LABEL_STYLES)
    scan_page_title.pack(pady=20)

    btn_full_scan = tk.Button(main_frame, text="Full System Scan", command=lambda: display_full_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=lambda: display_schedule_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=lambda: display_custom_scan_options(main_frame, update_main_frame, clear_main_frame), **style.BUTTON_STYLES)

    btn_full_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_schedule_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)
    btn_custom_scan.pack(pady=style.PAD_Y, padx=style.PAD_X)

def display_full_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    full_scan_title = tk.Label(main_frame, text="Full System Scan", **style.LABEL_STYLES)
    full_scan_title.pack(pady=20)

    scan_status_label = tk.Label(main_frame, text="", **style.LABEL_STYLES)
    scan_status_label.pack(pady=20)

    def start_full_scan():
        scan_thread = threading.Thread(target=run_full_scan, args=(scan_status_label,))
        scan_thread.start()

    def run_full_scan(status_label):
        log_path = "path_to_log_directory"  # Update with actual log path
        quarantine_path = "path_to_quarantine_directory"  # Update with actual quarantine path
        for output in fullScan(log_path, quarantine_path):
            status_label.config(text=output)
            main_frame.update_idletasks()

    start_scan_btn = tk.Button(main_frame, text="Start Full Scan", command=start_full_scan, **style.BUTTON_STYLES)
    start_scan_btn.pack(pady=10)

def display_custom_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    custom_scan_title = tk.Label(main_frame, text="Custom Drive Scan", **style.LABEL_STYLES)
    custom_scan_title.pack(pady=20)

    scan_status_label = tk.Label(main_frame, text="", **style.LABEL_STYLES)
    scan_status_label.pack(pady=20)
    
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

    def browse_target(entry_widget):
        folder_selected = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)

    def browse_log_path(entry_widget):
        log_path = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, log_path)

    def start_scan(scan_target, log_path):
        if not scan_target:
            scan_status_label.config(text="Error: Please select a drive or folder to scan.")
            return
        scan_thread = threading.Thread(target=run_scan, args=(scan_target, log_path, scan_status_label))
        scan_thread.start()

    def run_scan(scan_target, log_path, status_label):
        for output in basicScan([scan_target], log_path, None):
            status_label.config(text=output)
            main_frame.update_idletasks()

    btn_start_scan = tk.Button(main_frame, text="Start Scan", command=lambda: start_scan(entry_scan_target.get(), entry_log_path.get()), **style.BUTTON_STYLES)
    btn_start_scan.pack(pady=style.PAD_Y)

def display_schedule_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    title_label = tk.Label(main_frame, text="Schedule Scan", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Calendar for selecting days
    lbl_calendar = tk.Label(main_frame, text="Select Date for Scheduled Scan:", **style.LABEL_STYLES)
    lbl_calendar.pack(pady=style.PAD_Y)
    calendar = DateEntry(main_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    calendar.pack(pady=style.PAD_Y)

# Time Entry for selecting time (Hour, Minute) in 24-hour format
    lbl_time = tk.Label(main_frame, text="Select Time (HH:MM) in 24-hour format:", **style.LABEL_STYLES)
    lbl_time.pack(pady=style.PAD_Y)
    
    time_frame = tk.Frame(main_frame, bg=style.BACKGROUND_COLOR)  # Frame to hold time selection widgets

    lbl_time = tk.Label(time_frame, text="Select Time:", **style.LABEL_STYLES)
    lbl_time.pack(side=tk.LEFT, padx=(0, 10))  # Left side and some padding to the right
    
    entry_hour = tk.Entry(time_frame, width=2, **style.ENTRY_STYLES)  # Width set to 2 to hold two digits
    entry_hour.pack(side=tk.LEFT)
    
    lbl_colon = tk.Label(time_frame, text=":", **style.LABEL_STYLES)  # Colon label
    lbl_colon.pack(side=tk.LEFT)
    
    entry_minute = tk.Entry(time_frame, width=2, **style.ENTRY_STYLES)  # Width set to 2 to hold two digits
    entry_minute.pack(side=tk.LEFT)

    time_frame.pack(pady=style.PAD_Y)  # Pack the entire frame

    # Dropdown for selecting scan frequency (Daily, Weekly, Monthly, Once)
    lbl_frequency = tk.Label(main_frame, text="Select Frequency:", **style.LABEL_STYLES)
    lbl_frequency.pack(pady=style.PAD_Y)
    frequency_var = tk.StringVar(main_frame)
    frequency_options = ['Daily', 'Weekly', 'Monthly', 'Once']
    frequency_menu = tk.OptionMenu(main_frame, frequency_var, *frequency_options)
    frequency_menu.pack(pady=style.PAD_Y)

    # Entry for additional frequency options (Day of week or Month)
    lbl_additional = tk.Label(main_frame, text="Day of Week/Month (if applicable):", **style.LABEL_STYLES)
    lbl_additional.pack(pady=style.PAD_Y)
    entry_additional = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_additional.pack(pady=style.PAD_Y)

    def schedule_scan():
        date = calendar.get_date()
        hour = entry_hour.get()
        minute = entry_minute.get()
        frequency = frequency_var.get()
        additional_info = entry_additional.get()

        try:
            hour = int(hour)
            minute = int(minute)
            if frequency == 'Daily':
                schedule_scan_daily(hour, minute)
            elif frequency == 'Weekly':
                schedule_scan_weekly(additional_info, hour, minute)
            elif frequency == 'Monthly':
                schedule_scan_monthly(int(additional_info), hour, minute)
            elif frequency == 'Once':
                year, month, day = map(int, date.split('-'))
                schedule_scan_once(year, month, day, hour, minute)
            update_main_frame(f"Scan scheduled successfully for {frequency} at {hour}:{minute}.")
        except ValueError as e:
            update_main_frame(f"Error scheduling scan: {e}")

    # Schedule Button
    btn_schedule = tk.Button(main_frame, text="Schedule Scan", command=schedule_scan, **style.BUTTON_STYLES)
    btn_schedule.pack(pady=style.PAD_Y)


    def schedule_scan(date, hour, minute, am_pm):
        # Convert 12-hour format to 24-hour format
        hour_24 = int(hour) + 12 if am_pm == 'PM' and hour != '12' else int(hour)
        hour_24 = hour_24 if am_pm == 'AM' or hour == '12' else 0

        # Call appropriate scheduling function from core.py
        schedule_scan_daily(hour_24, int(minute))  # Example: Scheduling a daily scan
        update_main_frame(f"Scan scheduled at {hour}:{minute} {am_pm} on {date}")