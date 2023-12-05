import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import datetime
from datetime import datetime as time
import string
import os
import shutil
from cryptography.fernet import Fernet

def lock(qPath): #First time lock function with qPath
    filestolock = os.listdir(qPath)
    key = Fernet.generate_key()
    keyfile = qPath + "\\" + "Key.txt"
    fernet = Fernet(key)
    for fil in filestolock:
        ePath = qPath + "\\" + fil
        try:
            with open(ePath, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(ePath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except:
            print("Access Denied")
    with open(keyfile, 'w+') as f:
        f.write(str(key))
    throwAwayTheKey(qPath)
    return 0

def throwAwayTheKey(qPath, hide=False): #Tunnels Encrypted File into its own self-contained directory
    dir = str(datetime.date.today())
    filestolock = os.listdir(qPath)
    ext = 1
    while (("Q"+str(ext) + "-" + dir) in filestolock):
        ext+=1
    dir = "Q" +str(ext)+"-"+dir
    if hide:
        dir = "."+dir
    dir = qPath + "\\" + dir
    os.mkdir(dir)
    filesinq = os.listdir(qPath)
    for f in filesinq:
        if f[0] != 'Q' or '-' not in f or not f[1].isnumeric():
            fullpath = qPath+"\\"+f
            shutil.move(fullpath, dir)
          
def unlock(pathToV, vname): #decrypts chosen file vname in folder pathToV
    pathToV = path_format(pathToV)
    pathToV = str(pathToV) + "\\"
    kPath = str(pathToV) +"Key.txt"
    dPath = str(pathToV) + vname

    with open(kPath, 'rb') as file:
        key = file.read()
    key = key[2:len(key)-1]
    fernet = Fernet(key)
    with open(dPath, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(dPath, 'wb') as dec_file:
        dec_file.write(decrypted)
    return str(decrypted)[2:len(str(decrypted))-1]

def peek(pathToV, vname): #Peeks at chosen encrypted file in folder pathToV with name vname
    print(unlock(pathToV, vname))
    relock(pathToV, vname)

def relock(pathToV, vname): #Locks chosen decrypted file vname using Key.txt in PathToV (where vname is also)
    pathToV = path_format(pathToV)
    kPath = pathToV + "\\"+"Key.txt"
    ePath = str(pathToV) + "\\" + vname

    with open(kPath, 'rb') as file:
        key = file.read()
    key = key[1:len(key)-1]
    fernet = Fernet(key)

    with open(ePath, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(ePath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

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
    fPath = os.path.join(path, fName)
    if not os.path.exists(fPath):
        os.makedirs(fPath, exist_ok=True)
    os.chmod(fPath, 0o700)
    return fPath

def virus_count(logFile):
    with open(logFile, 'r') as file:
        lines = file.readlines()
        try:
              target_line = [line for line in lines if "Infected files:" in line][-1]
              virus_count = int(target_line.split(":")[-1].strip())
        except:
              virus_count=0
    return virus_count
    
def schedule_scan_once(year, month, day, input_hour, input_minute, scan_path):
      path = os.path.abspath(__file__)
      date = f"{month:02d}/{day:02d}/{year}" # so date is in MM/DD/YYYY format
      command = f"SCHTASKS /CREATE /SC ONCE /SD {date} /TN \"YourScanTaskNameOnce\" /TR \"python {path} scan{scan_path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
      run_schtasks(command)

def schedule_scan_daily(input_hour, input_minute, scan_path, input_often=1):
      path = os.path.abspath(__file__)
      command = f"SCHTASKS /CREATE /SC DAILY /MO {input_often} /TN \"YourScanTaskNameDaily\" /TR \"python {path} scan{scan_path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
      run_schtasks(command)

def schedule_scan_weekly(weekday, input_hour, input_minute, scan_path, input_often=1):
        path = os.path.abspath(__file__)
        command = f"SCHTASKS /CREATE /SC WEEKLY /D {weekday} /MO {input_often} /TN \"YourScanTaskNameWeekly\" /TR \"python {path} scan{scan_path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
        run_schtasks(command)

def schedule_scan_monthly(day_of_month, input_hour, input_minute, scan_path, input_often=1):
        path = os.path.abspath(__file__)
        command = f"SCHTASKS /CREATE /SC MONTHLY /D {day_of_month} /MO {input_often} /TN \"YourScanTaskNameMonthly\" /TR \"python {path} scan{scan_path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
        run_schtasks(command)

def customScan(sPaths, lPath=None, qPath=None):
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
    basicScan(sPaths, lPath, qPath)
    print(lock(qPath))
    
    

def basicScan(sPaths, lPath=None, qPath=None):

    #Usage:
    #sPaths (String list) [First Argument] represents the path to the file that is going to be scanned.
    #lPath (String) [Second Argument] represents the path to the file where the logs are to be deposited.
    #qPath (String) [Fourth Argument] represents the path to the file where the virus/infected folder is to be deposited.

    #Commond for ClamAV
    scan_command = ["clamscan.exe", "-r", "--max-dir-recursion=10",f"--move={qPath}", "-i"]
    scan_command.extend(sPaths)
    #print(" ".join(scan_command))
    
    #Message of scanning directories
    log_message = []
    for sPath in sPaths:
        message = "\n"+"Scanned " + sPath + " and its subdirectories."
        log_message.append(message)

    #Generate log file based on date
    log_file = "L"+str(datetime.date.today())+".txt"
    log_file = lPath + "\\" + log_file
    
    try:
        with open(log_file, "a") as f:
            process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for message in log_message:
                f.write(message)
            f.write("\n\n")
            for line in process.stdout:
                f.write(line)
            f.close()
    except FileNotFoundError:
        print("File not yet created.")

    for sPath in sPaths:
        print("Scanned ", sPath)

    virus_num = virus_count(log_file)  # Ensure consistent indentation
    print("Infected file(s): ", virus_num)
    return virus_num

      
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
    virus_num = basicScan(drives, lPath, qPath)
    print(lock(qPath))
    return virus_num
######
def run_schtasks(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print("Scheduled task created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
'''
# TIME IN 24HR FORMAT

def schedule_scan_daily(input_hour, input_minute, input_often=1):
    path = os.path.abspath(__file__)
    command = f"SCHTASKS /CREATE /SC DAILY /MO {input_often} /TN \"YourScanTaskNameDaily\" /TR \"python {path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
    run_schtasks(command)

def schedule_scan_weekly(weekday, input_hour, input_minute, input_often=1):
    path = os.path.abspath(__file__)
    command = f"SCHTASKS /CREATE /SC WEEKLY /D {weekday} /MO {input_often} /TN \"YourScanTaskNameWeekly\" /TR \"python {path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
    run_schtasks(command)

def schedule_scan_monthly(day_of_month, input_hour, input_minute, input_often=1):
    path = os.path.abspath(__file__)
    command = f"SCHTASKS /CREATE /SC MONTHLY /D {day_of_month} /MO {input_often} /TN \"YourScanTaskNameMonthly\" /TR \"python {path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
    run_schtasks(command)

def schedule_scan_once(year, month, day, input_hour, input_minute):
    path = os.path.abspath(__file__)
    date = f"{month:02d}/{day:02d}/{year}" # so date is in MM/DD/YYYY format
    command = f"SCHTASKS /CREATE /SC ONCE /SD {date} /TN \"YourScanTaskNameOnce\" /TR \"python {path} {input_hour} {input_minute}\" /ST {input_hour:02d}:{input_minute:02d} /F"
    run_schtasks(command)

"""
#print(lock("C:\\Users\\ian\\OneDrive\\Desktop\\Zmeya Prototyping\\ClamAV\\Viruses"))

sPaths = ["C:/Users/kitty/Desktop"]
lPath = "Z:/test"
qPath = "Z:/test"
customScan(sPaths, None, None)
customScan(sPaths, lPath, qPath)
schedule_scan_daily(15, 30, 2)
schedule_scan_weekly("MON", 15, 30, 1)
schedule_scan_monthly(15, 15, 30, 1)
schedule_scan_once(2023, 12, 25, 15, 30)
'''
