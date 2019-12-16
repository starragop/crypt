# Python 2
import base64
import os
import json

def encode(key, string):
    encoded_chars = []# Encoded array/list
    for i in xrange(len(string)):
        key_c = key[i % len(key)] # Turn the key into a character, in this case, "Neo" turns into "o"
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256) # Turn the letter into its unicode, add it by the unicode of the key, if it's over 256, substract 256 then turn it into a character again.
        encoded_chars.append(encoded_c) # Add the encoded character into the encoded array/list
    encoded_string = "".join(encoded_chars) # Turn the array/list into a string.
    return base64.urlsafe_b64encode(encoded_string) # Return the encrypted string

def decode(key,string):
  decode = base64.urlsafe_b64decode(string)
  decoded_string=[]
  for i in xrange(len(decode)):
    key_c = key[i % len(key)]
    decoded_c = chr(ord(decode[i]) - ord(key_c))
    decoded_string.append(decoded_c)
  return "".join(decoded_string)

def getUserInput(prompt):
  UserResponse = raw_input(prompt)
  return str(UserResponse)

def ChooseMode(): # Should this method use cases instead of if?
  chosen = getUserInput("Encrypt or Decrypt? (E/D/C)\n>")
  if chosen == "E":
    return True
  elif chosen == "D":
    return False
  elif chosen == "C":
    exit(0)
  else:
    return ChooseMode()

def ChooseType():
  type = getUserInput("File or Folder? (Fi/Fo/C)\n>")
  if type == "Fi":
    return True
  elif type == "Fo":
    return False
  elif type == "C":
    exit(0)
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
    filename = getUserInput("What would you like to name the file?\n>")
    chosenpath = chosenpath + filename
    return chosenpath
  else:
    print("Invalid path, please try again")
    return ChooseDeposit()

def GetFile(path): # Unused
  try:
    with open(path, "r") as file:
      return file
  except IOError:
    return False

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
      indexed = {}
      def ScanDir(Dir):
        scan = os.listdir(Dir)
        print("Scanning " + Dir)
        for i in xrange(len(scan)):
          print("Scanning... " + scan[i])
          if os.path.isdir(Dir + contents[i]):
            indexed[contents[i]] = {"type":"Dir","path":Dir + contents[i],"content":ScanDir(Dir + contents[i] + "/")}
          else:
            indexed[contents[i]] = {"type":"File","path":Dir + contents[i],"content":open(Dir + contents[i],"r").read()}
      ScanDir(dir)
      deposited = open(deposit,"w+")
      jsondump = json.dumps(indexed)
      print("INDEXED: " + str(indexed))
      print("JSON DUMP: " + jsondump)
      deposited.write(encode(key,jsondump))
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
      print("Folder encryption/decryption not supported at the moment, only individual files.")
      
      exit(0)

if __name__ == "__main__":
  Initiate()
