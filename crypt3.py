# Python 3
import base64
x = "It is not possible either to trick or escape the mind of Zeus"
key = "Neo"

def encode(key, string):
    encoded_chars = []# Encoded array/list
    for i in range(len(string)):
        key_c = key[i % len(key)] # Turn the key into a character, in this case, "Neo" turns into "o"
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256) # Turn the letter into its unicode, add it by the unicode of the key, if it's over 256, substract 256 then turn it into a character again.
        encoded_chars.append(encoded_c) # Add the encoded character into the encoded array/list
    encoded_string = "".join(encoded_chars) # Turn the array/list into a string.
    return base64.urlsafe_b64encode(bytes(encoded_string, 'utf-8'))# Return the encrypted string

def decode(key,string):
  decode = base64.urlsafe_b64decode(string)
  decoded_string=[]
  for i in range(len(decode)):
    key_c = key[i % len(key)]
    decoded_c = chr(ord(decode[i]) - ord(key_c))
    decoded_string.append(decoded_c)
  return "".join(decoded_string)

print(decode(key,encode(key,x)))
