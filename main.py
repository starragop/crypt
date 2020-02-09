import encoding
import guihandler

def start(mode, type, key, target, destination):
  print(mode,type,key,target,destination)
  return True

guihandler.begin(start)
