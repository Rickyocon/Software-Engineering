from core import path_format, customPath

#Delete most recent quarantine folder when users choose to delete.
def delete(qPath):
    if qPath:
        qPath = path_format(qPath)
    else:
        qfolder = "Zmeya_quarantine"
        qPath = customPath(qfolder)

    qFolders = [os.path.join(qPath, folder) for folder in os.listdir(qPath) if os.path.isdir(os.path.join(qPath, folder))]
    if qFolders:
        target_qFolder = max(qFolders, key=os.path.getctime)
        shutil.rmtree(target_qFolder)
        print("Infected files were deleted successfully!")
    else:
        print("Nothing to delete.")
