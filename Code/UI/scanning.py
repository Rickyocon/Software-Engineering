import tkinter as tk
from tkinter import filedialog
import threading
from tkcalendar import DateEntry
import style
from Zmeya_Backend.core import customScan,basicScan, fullScan, run_schtasks, schedule_scan_daily, schedule_scan_weekly, schedule_scan_monthly, schedule_scan_once

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

    # Log Folder Selection
    lbl_log_path = tk.Label(main_frame, text="Log File Path:", **style.LABEL_STYLES)
    lbl_log_path.pack(pady=style.PAD_Y)
    entry_log_path = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_log_path.pack(pady=style.PAD_Y)
    btn_browse_log = tk.Button(main_frame, text="Browse", command=lambda: browse_path(entry_log_path), **style.BUTTON_STYLES)
    btn_browse_log.pack(pady=style.PAD_Y)

    # Quarantine Folder Selection
    lbl_quarantine_path = tk.Label(main_frame, text="Quarantine Folder Path:", **style.LABEL_STYLES)
    lbl_quarantine_path.pack(pady=style.PAD_Y)
    entry_quarantine_path = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_quarantine_path.pack(pady=style.PAD_Y)
    btn_browse_quarantine = tk.Button(main_frame, text="Browse", command=lambda: browse_path(entry_quarantine_path), **style.BUTTON_STYLES)
    btn_browse_quarantine.pack(pady=style.PAD_Y)

    def browse_path(entry_widget):
        selected_path = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, selected_path)

    scan_status_label = tk.Label(main_frame, text="", **style.LABEL_STYLES)
    scan_status_label.pack(pady=20)

    def start_full_scan():
        log_path = entry_log_path.get()
        quarantine_path = entry_quarantine_path.get()
        scan_thread = threading.Thread(target=run_full_scan, args=(log_path, quarantine_path, scan_status_label))
        scan_thread.start()

    def run_full_scan(log_path, quarantine_path, status_label):
        virus_count = fullScan(log_path, quarantine_path)
        if virus_count > 0:
            status_label.config(text=f"{virus_count} infected file(s) found.")
        else:
            status_label.config(text="No infected files found.")
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

    # Quarantine Folder Selection
    lbl_quarantine_path = tk.Label(main_frame, text="Quarantine Folder Path:", **style.LABEL_STYLES)
    lbl_quarantine_path.pack(pady=style.PAD_Y)
    entry_quarantine_path = tk.Entry(main_frame, **style.ENTRY_STYLES)
    entry_quarantine_path.pack(pady=style.PAD_Y)
    btn_browse_quarantine = tk.Button(main_frame, text="Browse", command=lambda: browse_target(entry_quarantine_path), **style.BUTTON_STYLES)
    btn_browse_quarantine.pack(pady=style.PAD_Y)

    def browse_target(entry_widget):
        folder_selected = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_selected)

    def browse_log_path(entry_widget):
        log_path = filedialog.askdirectory()
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, log_path)

    def start_scan(scan_target, log_path, quarantine_path):
        if not scan_target:
            scan_status_label.config(text="Error: Please select a drive or folder to scan.")
            return
        scan_thread = threading.Thread(target=run_scan, args=(scan_target, log_path, quarantine_path, scan_status_label))
        scan_thread.start()

    def run_scan(scan_target, log_path, quarantine_path, status_label):
        # Assuming customScan performs the scan and does not return iterable data
        customScan([scan_target], log_path, quarantine_path)
        # Update the status label after the scan is complete
        status_label.config(text="Scan completed.")
        main_frame.update_idletasks()


    btn_start_scan = tk.Button(main_frame, text="Start Scan", command=lambda: start_scan(entry_scan_target.get(), entry_log_path.get(),entry_quarantine_path.get()), **style.BUTTON_STYLES)
    btn_start_scan.pack(pady=style.PAD_Y)

def display_schedule_scan_options(main_frame, update_main_frame, clear_main_frame):
    clear_main_frame()

    title_label = tk.Label(main_frame, text="Schedule Scan", **style.LABEL_STYLES)
    title_label.pack(pady=style.PAD_Y)

    # Calendar for selecting days
    lbl_calendar = tk.Label(main_frame, text="Select Date:", **style.LABEL_STYLES)
    lbl_calendar.pack(pady=style.PAD_Y)
    calendar = DateEntry(main_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    calendar.pack(pady=style.PAD_Y)

    # Dropdown for selecting time (Hour, Minute, AM/PM)
    lbl_time = tk.Label(main_frame, text="Select Time (HH:MM):", **style.LABEL_STYLES)
    lbl_time.pack(pady=style.PAD_Y)
    hours = [f"{h:02d}" for h in range(1, 13)]  # 1 to 12 for 12-hour format
    minutes = [f"{m:02d}" for m in range(60)]
    am_pm = ["AM", "PM"]
    hour_var = tk.StringVar(main_frame)
    minute_var = tk.StringVar(main_frame)
    am_pm_var = tk.StringVar(main_frame)
    hour_menu = tk.OptionMenu(main_frame, hour_var, *hours)
    minute_menu = tk.OptionMenu(main_frame, minute_var, *minutes)
    am_pm_menu = tk.OptionMenu(main_frame, am_pm_var, *am_pm)
    hour_menu.pack(pady=style.PAD_Y)
    minute_menu.pack(pady=style.PAD_Y)
    am_pm_menu.pack(pady=style.PAD_Y)

    # Schedule Button
    btn_schedule = tk.Button(main_frame, text="Schedule Scan", command=lambda: schedule_scan(calendar.get_date(), hour_var.get(), minute_var.get(), am_pm_var.get()), **style.BUTTON_STYLES)
    btn_schedule.pack(pady=style.PAD_Y)

    def schedule_scan(date, hour, minute, am_pm):
        # Convert 12-hour format to 24-hour format
        hour_24 = int(hour) + 12 if am_pm == 'PM' and hour != '12' else int(hour)
        hour_24 = hour_24 if am_pm == 'AM' or hour == '12' else 0

        # Call appropriate scheduling function from core.py
        schedule_scan_daily(hour_24, int(minute))  # Example: Scheduling a daily scan
        update_main_frame(f"Scan scheduled at {hour}:{minute} {am_pm} on {date}")
