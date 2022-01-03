from os import environ
from random import random
import cryptocode


def main():
  ## Get Github environment file
  ## Only run this part when GITHUB_ENV is set -> workflow detection
  env_file = environ.get('GITHUB_ENV', None)
  if env_file:
    
    ## PASS_KEY to encrypt the secret
    passkey = environ.get("PASS_KEY", None)

    ## get the encrypted token and decrypt with passkey
    encrypted_old_access_token = environ.get("ENCRYPTED_ACCESS_TOKEN", None)
    if encrypted_old_access_token and passkey: 
      old_access_token = cryptocode.decrypt(encrypted_old_access_token, passkey)
    if old_access_token:
      print("Access Token from secret: {}".format(old_access_token))
      print("Correct Token: {}".format(old_access_token.startswith('ThisIsASecret')))
    else:
      print("No Access Token provided!")

    ######
    #
    # Do stuff here
    # Use old_access_token to access an API ...
    #
    #####
      
    ## Encrypt new access token from API for next run
    ## Save encrypted token to GITHUB_ENV
    new_access_token = "ThisIsASecret{}".format(random())
    print("New Token: {}".format(new_access_token))
    if passkey:
      encrypted_new_access_token = cryptocode.encrypt(new_access_token, passkey)
      with open(env_file, "a") as file:
        file.write("ENCRYPTED_NEW_ACCESS_TOKEN={}\n".format(encrypted_new_access_token))

if __name__ == "__main__":
  main()
