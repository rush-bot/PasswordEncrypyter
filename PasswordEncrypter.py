#File: PasswordEncrypter.py
#Modules
import time
import sys
import hashlib

#Title
print("\033[1;31;47m Password Encrypter: SHA1, SHA224, SHA256, SHA384, SHA512,and MD5")
print("Hi! Welcome to the password encrypter. Here, you can make your passwords more secure.")
print("Version 1.0 - Made by rush-bot")
time.sleep(1)

#Check
while True:
  check = input("\033[1;37;46m Are you sure you want to encrypt your password? (y/n)\n")
  if "y" in check:
    break
  elif "n" in check:
    print("Sorry to hear that. Come back when you are ready.")
    sys.exit()
  else:
    print("\033[1;35;41m Error: {} is not an acceptable arguement." .format(check))
    continue
password = input("\n Please provide the password you want to encrypt below.\n")  
#Ciphers
def executeSHA256():
  global encrypt
  encrypt = hashlib.sha256(password.encode())
  encrypt =(encrypt.hexdigest())

def executeMD5():
  global encrypt
  encrypt = hashlib.md5(password.encode())
  encrypt =(encrypt.hexdigest())

def executeSHA512():
  global encrypt
  encrypt = hashlib.sha512(password.encode())
  encrypt =(encrypt.hexdigest())

def executeSHA1():
  global encrypt
  encrypt = hashlib.sha1(password.encode())
  encrypt =(encrypt.hexdigest())

def executeSHA224():
  global encrypt
  encrypt = hashlib.sha224(password.encode())
  encrypt =(encrypt.hexdigest())

def executeSHA384():
  global encrypt
  encrypt = hashlib.sha384(password.encode())
  encrypt =(encrypt.hexdigest())

#Statements
while True:
  cipherType = input("\n What encryption cipher do you want to use?\n" )
  if "sha256" in cipherType:
    executeSHA256()
    break
  elif "SHA256" in cipherType:
    executeSHA256()
    break
  elif "Sha256" in cipherType:
    executeSHA256()
    break
  elif "md5" in cipherType:
    executeMD5()
    break
  elif "MD5" in cipherType:
    executeMD5()
    break
  elif "Md5" in cipherType:
    executeMD5()
    break
  elif "sha512" in cipherType:
    executeSHA512()
    break
  elif "SHA512" in cipherType:
    executeSHA512()
    break
  elif "Sha512" in cipherType:
    executeSHA512()
    break
  elif "sha1" in cipherType:
    executeSHA1()
    break
  elif "SHA1" in cipherType:
    executeSHA1()
    break
  elif "Sha1" in cipherType:
    executeSHA1()
    break
  elif "sha224" in cipherType:
    executeSHA224()
    break
  elif "SHA224" in cipherType:
    executeSHA224()
    break
  elif "Sha224" in cipherType:
    executeSHA224()
    break
  elif "sha384" in cipherType:
    executeSHA384()
    break
  elif "SHA384" in cipherType:
    executeSHA384()
    break
  elif "Sha384" in cipherType:
    executeSHA384()
    break
  else:
    print("\033[1;35;41m Error: {} is not a recognized cipher" .format(cipherType))
    continue

#Info Gathering
print("\n Great! Your encrypted password is being created.\n We just need to collect a little more information.\n\n")
#Name
name = input("\033[1;34;47m What is your name?\n")
#Source
source = input("\nWhat website or source is this password for?\n")
#Urgency
while True:
  essential = input("\n\033[1;34;47m On a scale of 1-10, how important is this password?\n")
  try:
    esseential = int(essential)
    break
  except:
    print("\033[1;35;41m Error: {} is not an acceptable value." .format(essential))
    continue    
#Safe Password
safePass = password[0:3] + "***" + password[-3:]
#Document Creation
print("\nCompiling Information...")
time.sleep(2)
f = open("passwordInfo.txt", "x")
f.write("Password Information:\n")
f.write("Name: {}\nSource: {}\nImportance: {}/10\n\n\n".format(name,source,essential))
f.write("Original Password:\n{}\n\nEncrypted Password:\n{}" .format(safePass, encrypt))
f.write("\n\n\nMade by rush-bot")
f.close()
