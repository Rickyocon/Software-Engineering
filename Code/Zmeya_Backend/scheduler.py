import core
import string
import os

def main():
    # full scan
    #Paths to scan - all available drives
    #drives = [f'{d}:\\' for d in string.ascii_uppercase if os.path.exists(f'{d}:\\')]

    # Use customPath function from core.py
    scan_path = core.customPath(dirName)
    
    #full scan : core.customScan(drives, log_path, quarantine_path)
    # Perform the custom scan
    core.customScan([scan_path], lPath, qPath) # for custompath(dirName)

if __name__ == "__main__":
    main()
