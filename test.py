from os import environ
from random import random
from cryptography.fernet import Fernet


def main():
  cipher_suite = Fernet(environ.get("FERNET_KEY"))
  
  encrypted_old_access_token = environ.get("ACCESS_TOKEN", None)
  old_access_token = cipher_suite.decrypt(encrypted_old_access_token)
  
  print("Access Token from secret: {}".format(old_access_token))
  print("Correct Token: {}".format(old_access_token.startswith('ThisIsASecret')))
 
  new_access_token = "ThisIsASecret{}".format(random())
  print("New Token: {}".format(new_access_token))
  
  env_file = environ.get('GITHUB_ENV', None)
  
  if env_file:
    with open(env_file, "a") as file:
      file.write("NEW_ACCESS_TOKEN={}\n".format(new_access_token))

if __name__ == "__main__":
  main()
