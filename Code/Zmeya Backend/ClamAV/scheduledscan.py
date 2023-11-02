import subprocess
import datetime
import shutil
import pathlib
import os
import string
import schedule
import time

def customScan(sPath, lPath=None, qPath=None):
    """
    Usage:
    sPath (String): Path to the file or directory that is going to be scanned.
    lPath (String): Path to the directory where the logs will be saved.
    qPath (String): Path to the directory where quarantined files will be deposited.
    """

    # Message of scanning directories
    log_message = "\nScanned " + sPath + " and its subdirectories."

    # Set the marker for stdout
    marker = "----------- SCAN SUMMARY -----------"
    marker_found = False

    # Generate filename based on date
    filename = "Q" + str(datetime.date.today()) + ".txt"

    if not lPath:
        lPath = os.path.join(os.path.expanduser("~"), "Desktop", "ScanningLogs")

    # Ensure the log directory exists
    os.makedirs(lPath, exist_ok=True)

    # If today's log file exists in the log folder, move it to the script's directory and append the next scan summary
    try:
        shutil.move(os.path.join(lPath, filename), pathlib.Path(__file__).parent.resolve())
    except FileNotFoundError:
        print("File not yet created.")

    # Command for ClamAV
    scan_command = ["clamscan.exe", "-r", "--max-dir-recursion=10", sPath]

    with open(filename, "a") as f:
        process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            if marker in line:
                marker_found = True
            if marker_found:
                f.write(line)
        f.write(log_message)
        f.write("\n\n")

    # Close and move the log file back to the log directory
    f.close()
    shutil.move(filename, os.path.join(lPath, filename))
    print("Scanned " + sPath)

def get_user_schedule():
    while True:
        try:
            days_input = input("Enter days to schedule (e.g., Mon,Tue,Wed): ").strip().split(",")
            frequency = int(input("Enter frequency (in days): "))
            user_time = input("Enter the desired scan time in HH:MM format (e.g., 10:00): ")
            user_schedule = {
                "days": days_input,
                "frequency": frequency,
                "time": user_time,
            }
            return user_schedule
        except (ValueError, KeyError):
            print("Invalid input format. Please follow the format specified.")

def get_user_paths():
    sPath = input("Enter the path to be scanned: ").strip()
    lPath = input("Enter the path where the logs will be saved: ").strip()
    qPath = input("Enter the path where quarantined files will be deposited (optional, press Enter to skip): ").strip()
    return sPath, lPath, qPath

def scheduled_scan(user_schedule, paths):
    sPath, lPath, qPath = paths

    # Perform the custom scan
    customScan(sPath, lPath, qPath)

# Get the user's preferred schedule settings
user_schedule = get_user_schedule()

# Get the user's preferred file paths
paths = get_user_paths()

# Schedule the scan based on user's preferences
for day in user_schedule["days"]:
    schedule.every(user_schedule["frequency"]).days.at(user_schedule["time"]).do(scheduled_scan, user_schedule, paths)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)