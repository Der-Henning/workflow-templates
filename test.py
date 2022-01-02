from os import environ
from random import random
import cryptocode


def main():
  passkey = environ.get("FERNET_KEY")
  
  encrypted_old_access_token = environ.get("ACCESS_TOKEN", None)

  old_access_token = cryptocode.decrypt(encrypted_old_access_token, passkey)

  
  print("Access Token from secret: {}".format(old_access_token))
  print("Correct Token: {}".format(old_access_token.startswith('ThisIsASecret')))
 
  new_access_token = "ThisIsASecret{}".format(random())
  print("New Token: {}".format(new_access_token))
  encrypted_new_access_token = cryptocode.encrypt(new_access_token, passkey)
  
  env_file = environ.get('GITHUB_ENV', None)
  
  if env_file:
    with open(env_file, "a") as file:
      file.write("NEW_ACCESS_TOKEN={}\n".format(encrypted_new_access_token))

if __name__ == "__main__":
  main()
