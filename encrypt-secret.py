from os import environ
from random import random


def main():
  ## Get Github environment file
  ## Only run this part when GITHUB_ENV is set -> workflow detection
  env_file = environ.get('GITHUB_ENV', None)
  if env_file:
    
    access_token = environ.get("ACCESS_TOKEN")


    print("Access Token: {}".format(access_token))


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
    with open(env_file, "a") as file:
      file.write("ACCESS_TOKEN={}\n".format(new_access_token))

if __name__ == "__main__":
  main()
