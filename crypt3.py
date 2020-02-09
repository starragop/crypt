#!/usr/bin/env python3
# Python 3, report any issues
# Purely for CLI use, not made for GUI uses, GUI module will come out in 1.1
import sys
if sys.version_info < (3,0):
  print("Sorry, this program file is only for Python 3!")
  exit()
import os
import json
from encoding import *
try:
  from termcolor import colored
except ImportError as err:
  print("Had issues importing termcolor:",err)

def getUserInput(prompt):
  UserResponse = input(prompt)
  return str(UserResponse)

def ChooseMode(): # Should this method use cases instead of if?
  chosen = getUserInput("Encrypt or Decrypt? (E/D/C)\n>")
  if chosen.upper() == "E":
    return True
  elif chosen.upper() == "D":
    return False
  elif chosen.upper() == "C":
    exit()
  else:
    return ChooseMode()

def ChooseType():
  type = getUserInput("File or Directory? (F/D/C)\n>")
  if type.upper() == "F":
    return True
  elif type.upper() == "D":
    return False
  elif type.upper() == "C":
    exit()
  else:
    return ChooseType()

def GetKey():
  gkey = getUserInput("What is the key?\n>")
  return gkey

def ChooseFile(IsDir):
  chosenfile = getUserInput("What file would you like to select?\n>")
  if os.path.exists(chosenfile):
    return chosenfile
  else:
    print("File not found, please try again")
    return ChooseFile(IsDir)

def ChooseDeposit():
  chosenpath = getUserInput("Where would you like to deposit the encrypted files?\n>")
  if os.path.isdir(chosenpath):
    def checkSpaces():
      if chosenpath[-1] == " ":
        chosenpath[-1] = ""
        checkSpaces()
    checkSpaces()
    if chosenpath[-1] != "/":
      chosenpath = chosenpath + "/"
    filename = getUserInput("What would you like to name the file/folder?(No slashes)\n>")
    chosenpath = chosenpath + filename
    return chosenpath
  else:
    print("Invalid path, please try again")
    return ChooseDeposit()

def Initiate():
  mode = ChooseMode()
  type = ChooseType()
  key = GetKey()
  if mode is True: # Encrypt
    if type is True: # File type chosen
      file = open(ChooseFile(False), "r")
      deposit = ChooseDeposit()
      filecontents = file.read()
      encryptedfile = encode(key, filecontents)
      depositedfile = open(deposit, "w+")
      depositedfile.write(encryptedfile)
      print("Done! Saved to " + deposit)
    else:
      dir = ChooseFile(True)
      deposit = ChooseDeposit()
      contents = os.listdir(dir)
      def ScanDir(Dir):
        print("Scanning directory:",Dir)
        scan = os.listdir(Dir)
        dirdata = {"files":[],"sub":[]}
        print("Scanning " + Dir)
        for current in scan:
          currentpath = Dir + "/" + current
          if os.path.isfile(currentpath):
            print("Processing file:",os.path.abspath(currentpath))
            currentfile = open(currentpath,"r")
            filecontents = currentfile.read()
            dirdata["files"].append([os.path.basename(currentpath),filecontents])
          elif os.path.isdir(currentpath):
            print("Processing sub directory:",os.path.abspath(currentpath))
            dirdata["sub"].append(ScanDir(os.path.abspath(currentpath)))
        return dirdata
      dir_data = ScanDir(dir)
      print(dir_data)
      deposited = open(deposit,"w+")
      deposited.write(encode(key,str(dir_data)))
      print("Done! Saved to " + deposit)
      exit(0)
  else: # Decrypt
    if type is True: # File type chosen
      file = open(ChooseFile(False), "r")
      deposit = ChooseDeposit()
      filecontents = file.read()
      decryptedfile = decode(key, filecontents)
      depositedfile = open(deposit, "w+")
      depositedfile.write(decryptedfile)
      print("Done! Saved to " + deposit)
    else:
      file = open(ChooseFile(False), "r")
      deposit = ChooseDeposit()
      filecontents = file.read()
      contents = json.loads(decode(key,filecontents))
      print(contents)
      def SetupDir(Dir):
        CurrentDir = deposit + Dir
        for currentfile in contents["files"]:
          de_file = open((CurrentDir + currentfile[0]),"w+")
          de_file.write(currentfile[1])
        for currentdir in contents["sub"]:
          os.mkdir(CurrentDir + "/" + currentdir[0])
          SetupDir("/" + os.path.relpath(CurrentDir + "/" + currentdir[0], deposit))
      SetupDir("")

if __name__ == "__main__":
  try:
    Initiate()
  except KeyboardInterrupt:
    try:
      print(colored("\nOperation canceled by user!(KeyboardInterrupt)","red",attrs=['reverse', 'blink']))
    except:
      print("\nOperation canceled by used!!(KeyboardInterrupt)")
  except Exception as err:
    try:
      print(colored("\nFatal error!!!","red",attrs=['reverse', 'blink']))
      print(err,"\n",sys.exc_info()[2])
    except:
      print("\nFatal error!!\n",err,"\n",sys.exc_info()[2])
