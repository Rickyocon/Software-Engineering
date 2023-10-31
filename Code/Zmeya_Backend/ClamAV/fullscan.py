import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
import shutil #This module provides a higher-level interface for file operations. 
import pathlib #This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
import string
import os

def customScan(sPaths, lPath=None, qPath=None):
    #Usage:
    #sPath (String) [First Argument] represents the path to the file that is going to be scanned.
    #lPath (String) [Second Argument] represents the path to the file where the logs are to be deposited.
    #qPath (String) [Third Argument] represents the path to the file where the virus/infected folder is to be deposited.

    #Message of scanning directories
    log_message = []
    for sPath in sPaths:
        message = "\n"+"Scanned " + sPath + " and its subdirectories." 
        log_message.append(message)

    #Set the marker of stdout
    marker = "----------- SCAN SUMMARY -----------"
    marker_found = False
 
    #Generate filename based on date
    filename = "L"+str(datetime.date.today())+".txt"

    if not lPath:
        log_folder = "C:\\Program Files\\ClamAV\\log"
        lPath = "C:\\Program Files\\ClamAV\\log"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder, exist_ok=True)


    #If today's log file exists (in the log folder), grab it and append the next scan summary
    #If today's log file does not exist, create one and append the next scan summary
    try:
        shutil.move(lPath + "\\"+filename, pathlib.Path(__file__).parent.resolve())
        #shutil.move(src, dst, copy_function=copy2): recursively move a file or directory (src) to another location (dst) and return the destination.
    except:
        print("File not yet created.")

    #Commond for ClamAV
    scan_command = ["clamscan.exe", "-r", "--max-dir-recursion=10"]
    scan_command.extend(sPaths)
    print(" ".join(scan_command))

    with open(filename, "a") as f:  
        process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            if marker in line:
                marker_found = True
            if marker_found:
                f.write(line)
        for message in log_message:    
            f.write(message)
        f.write("\n\n")    

    
    #Close and move back to the log file
    f.close()
    shutil.move(filename, lPath)
    print("Scanned" +", ".join(sPaths))

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
    
    customScan(drives, lPath, qPath)
  

#Test case
#lPath = os.path.join(os.path.expanduser("~"), "Desktop")
#fullScan(lPath, None,)


