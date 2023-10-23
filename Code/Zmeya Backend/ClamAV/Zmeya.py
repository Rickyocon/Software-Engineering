import subprocess
import datetime
import shutil
import pathlib

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
