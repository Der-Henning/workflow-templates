# Workflow Templates

## encrypt-secrets.yml

Example workflow on how to use a secret access token which will be updated during runtime without exposing the token in the logs.

Initial access token must be provided as `ACCESS_TOKEN` repositorty secret. The secret will be updated on each run of the workflow.
