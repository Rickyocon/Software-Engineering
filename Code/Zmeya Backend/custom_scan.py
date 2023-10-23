import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
import shutil #This module provides a higher-level interface for file operations. 
import pathlib #This module offers classes representing filesystem paths with semantics appropriate for different operating systems.
import string
import os

def customScan(sPaths, lPath, qPath):
    log_message = []
    for sPath in sPaths:
        message = "\n"+"Scanned " + sPath + " and its subdirectories." 
        log_message.append(message)
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

    #Commond for ClamAV
    scan_command = ["clamscan.exe", "-r", "--max-dir-recursion=10"]

    #Set paths need to be scanned
    scan_command.extend(sPaths)
    
    #Run ClamAV    
    subprocess.call(scan_command, stdout=f)

    #Garbage Collecting in the text file
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if "\\" not in line:
                f.write(line)
        for message in log_message:    
            f.write(message)
    
    #Close and move back to the log file
    f.close()
    shutil.move(filename, lPath)
    print("Scan finished!")


sPaths = ["C:\\Users\\kitty\\Desktop", "Z:\\"]
lPath = os.path.join(os.path.expanduser("~"), "Desktop")

customScan(sPaths,lPath, None)


