import core
import string
import os

def main():
    # Paths to scan - all available drives
    drives = [f'{d}:\\' for d in string.ascii_uppercase if os.path.exists(f'{d}:\\')]
    
    # Define log and quarantine paths
    log_path = core.customPath("Zmeya_log")
    quarantine_path = core.customPath("Zmeya_quarantine")

    # Perform the custom scan
    core.customScan(drives, log_path, quarantine_path)

if __name__ == "__main__":
    main()
