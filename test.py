from os import environ
from random import random
from cryptography.fernet import Fernet


def main():
  cipher_suite = Fernet(environ.get("FERNET_KEY"))
  
  encrypted_old_access_token = environ.get("ACCESS_TOKEN", None)
  old_access_token = None
  try:
    old_access_token = cipher_suite.decrypt(bytes(encrypted_old_access_token,'UTF-8'))
  except:
    pass
  
  print("Access Token from secret: {}".format(old_access_token))
  if old_access_token: print("Correct Token: {}".format(old_access_token.startswith('ThisIsASecret')))
 
  new_access_token = "ThisIsASecret{}".format(random())
  print("New Token: {}".format(new_access_token))
  encrypted_new_access_token = cipher_suite.encrypt(bytes(new_access_token,'UTF-8'))
  
  env_file = environ.get('GITHUB_ENV', None)
  
  if env_file:
    with open(env_file, "a") as file:
      file.write("NEW_ACCESS_TOKEN={}\n".format(encrypted_new_access_token))

if __name__ == "__main__":
  main()
