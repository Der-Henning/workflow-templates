from os import environ
from random import random


def main():
  print("Access Token from secret: {}".format(environ.get("ACCESS_TOKEN", None)))
  env_file = environ.get('GITHUB_ENV', None)
  if env_file:
    with open(env_file, "a") as file:
      file.write("NEW_ACCESS_TOKEN={}{}\n".format("ThisIsASecret", random()))

if __name__ == "__main__":
  main()
