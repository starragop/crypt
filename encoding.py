import base64

def encode(key, string):
    encoded_chars = []# Encoded array/list
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return str(base64.urlsafe_b64encode(bytes(encoded_string,"utf-8")))

def decode(key,string):
  decode = str(base64.urlsafe_b64decode(string))
  decoded_string=[]
  for i in range(len(decode)):
    key_c = key[i % len(key)]
    print(ord(decode[i]) - ord(key_c),decode[i],key_c,ord(decode[i]),ord(key_c))
    decoded_c = chr(ord(decode[i]) - ord(key_c))
    print(decoded_c)
    decoded_string.append(decoded_c)
  return "".join(decoded_string)
