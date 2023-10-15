import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
import shutil #This module provides a higher-level interface for file operations. 
import pathlib #This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
import string
import os

def manualScan(sPath, lPath, qPath):

    #Usage:
    #sPath (String) [First Argument] represents the path to the file that is going to be scanned.
    #lPath (String) [Second Argument] represents the path to the file where the logs are to be deposited.
    #qPath (String) [Third Argument] represents the path to the file where the virus/infected folder is to be deposited.

    #Generate filename based on date
    filename = "Q"+str(datetime.date.today())+".txt"

    #If today's log file exists (in the log folder), grab it and append the next scan summary
    #If today's log file does not exist, create one and append the next scan summary
    try:
        shutil.move(lPath + "\\"+filename, pathlib.Path(__file__).parent.resolve())
        #shutil.move(src, dst, copy_function=copy2): recursively move a file or directory (src) to another location (dst) and return the destination.
    except:
        print("File not yet created.")
    f = open(filename, "a")
    subprocess.call(["clamscan.exe",sPath], stdout=f)

    #Garbage Collecting in the text file
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if "SCAN" in line.strip("\n") or ":" in line.strip("\n"):
                f.write(line)
    
    #Move back to the log file
    shutil.move(filename, lPath)

def fullScan(lPath, qPath):
    """
    Conduct a full system scan on Windows 10.
    Usage:
    lPath (String): The path where the log file should be saved.
    qPath (String): The directory where infected files will be moved if detected.
    """
    drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]
    """
    1. Detect the available drives and then iterate scan over them.
    2. '%s:\\'%d' replases '%s" with the value of 'd'. It creates a sting representation of 
       each possible drive path.
    3. 'os.path.exists('%s:\\' % d)': This checks if a path with the given drive letter exists.
       If the drive exists, its path (like 'C:\\') is added to the list.
    """
    for drive in drives:
        print(f"Scanning {drive}...")
        """
        f-string. Inside an f-string, you can include expressions inside curly braces {}, 
        and these expressions will be evaluated at runtime and then formatted into the 
        resulting string.
        """
        manualScan(drive, lPath, qPath)


