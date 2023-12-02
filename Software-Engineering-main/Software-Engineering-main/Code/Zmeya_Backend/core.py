import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
from datetime import datetime as time
import string
import os

def path_format(paths):
    if isinstance(paths, list):
        paths = [path.replace("/", "\\") for path in paths]
    else:
        paths = paths.replace("/", "\\")
    return paths

def customPath(dirName):
    path = os.path.join(os.getcwd(), dirName)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    os.chmod(path, 511)
    return path

def new_folder(path):
    now = time.now()
    fName = f"Q{now.strftime('%Y%m%d_%H%M%S')}"
    print(fName)
    fPath = os.path.join(path, fName)
    if not os.path.exists(fPath):
        os.makedirs(fPath, exist_ok=True)
    os.chmod(fPath, 0o700)
    return fPath

def customScan(sPaths, lPath=None, qPath=None):

    #Usage:
    #sPaths (String list) [First Argument] represents the path to the file that is going to be scanned.
    #lPath (String) [Second Argument] represents the path to the file where the logs are to be deposited.
    #ePaths (String list) [Third Argument] represents the path to the directories that is going to be excluded.
    #qPath (String) [Fourth Argument] represents the path to the file where the virus/infected folder is to be deposited.

    #replace "/" in the sPaths, lPath, ePaths to "\\"
    sPaths = path_format(sPaths)
   
    if lPath:
        lPath = path_format(lPath)
    else:
        lfolder = "Zmeya_log"
        lPath = customPath(lfolder)

    if qPath:
        qPath = path_format(qPath)
    else:
        qfolder = "Zmeya_quarantine"
        qPath = customPath(qfolder)
    qPath = new_folder(qPath)

    print("Zmeya is scanning: ", sPaths)
    print("The log path is: ", lPath)
    print("The quaranting path is: ", qPath)

    #Commond for ClamAV
    scan_command = ["clamscan.exe", "-r", "--max-dir-recursion=10",f"--move={qPath}", "-i"]
    scan_command.extend(sPaths)
    print(" ".join(scan_command))
    
    #Message of scanning directories
    log_message = []
    for sPath in sPaths:
        message = "\n"+"Scanned " + sPath + " and its subdirectories." 
        log_message.append(message)

    #Generate log file based on date
    log_file = "L"+str(datetime.date.today())+".txt"
    
    try:
        with open(lPath + "\\" + log_file, "a") as f:
            process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for message in log_message:    
                f.write(message)
            f.write("\n\n")
            for line in process.stdout:
                f.write(line)
            f.close()
    except FileNotFoundError:
        print("File not yet created.")
  
    print("Scanned ", sPaths)

      
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
  

sPaths = ["C:/Users/kitty/Desktop"]
lPath = "Z:/test"
qPath = "Z:/test"
customScan(sPaths, None, None)
customScan(sPaths, lPath, qPath)


