import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
import shutil #This module provides a higher-level interface for file operations. 
import pathlib #This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
import string
import os

def customScan(sPaths, lPath, qPath):
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
    filename = "Q"+str(datetime.date.today())+".txt"

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

#Test case
sPaths = ["C:\\Users\\kitty\\Desktop", "Z:\\"]
lPath = os.path.join(os.path.expanduser("~"), "Desktop")
customScan(sPaths,lPath, None)


