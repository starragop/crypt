# Python 2
import base64

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
  UserResponse = input(prompt)
  return UserResponse

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

print(ChooseMode)
