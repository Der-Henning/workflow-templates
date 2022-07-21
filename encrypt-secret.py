from os import environ
from random import random


def main():
    # Get Github environment file
    # Only run this part when GITHUB_ENV is set -> workflow detection
    env_file = environ.get('GITHUB_ENV', None)
    if env_file:

        # Read access token from environment
        access_token = environ.get("ACCESS_TOKEN")

        # Even printing the variable in python will display the masked version
        print("Access Token: {}".format(access_token))
        print("Correct Access Token: {}".format(
            access_token.startswith("ThisIsASecret")))

        ######
        #
        # Do stuff here
        # Use old_access_token to access an API ...
        # Generate/receive the new access token
        #
        #####
        new_access_token = "ThisIsASecret{}".format(random())

        # New access token will be printed in plain text!
        print("New Token: {}".format(new_access_token))

        # Write new access token to environment file
        with open(env_file, "a") as file:
            file.write("ACCESS_TOKEN={}\n".format(new_access_token))


if __name__ == "__main__":
    main()
