import datetime
import shutil
import os
from cryptography.fernet import Fernet

def lock(qPath): #First time lock function with qPath
	key = Fernet.generate_key()
	keyfile = qPath + "\\" + "Key.txt"
	filestolock = os.listdir(qPath)
	fernet = Fernet(key)
	for fil in filestolock:
		ePath = qPath + "\\" + fil
		with open(ePath, 'rb') as file:
			original = file.read()
		encrypted = fernet.encrypt(original)
		with open(ePath, 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
	with open(keyfile, 'w+') as f:
		f.write(str(key))
	throwAwayTheKey(qPath)

def throwAwayTheKey(qPath, hide=False): #Tunnels Encrypted File into its own self-contained directory
	dir = "Q-" + str(datetime.date.today())
	if hide:
		dir = "."+dir
	dir = qPath + "\\" + dir
	os.mkdir(dir)

	filesinq = os.listdir(qPath)
	for f in filesinq:
		fullpath = qPath+"\\"+f
		shutil.move(fullpath, dir)
          
def unlock(pathToV, vname): #decrypts chosen file vname in folder pathToV
	#Test format of dPath
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