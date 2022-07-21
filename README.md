# Workflow Templates

## encrypt-secrets.yml

Example workflow on how to use a secret access token which will be updated during runtime without exposing the token in the logs.

Initial access token must be provided as `ACCESS_TOKEN` repository secret. The secret will be updated on each run of the workflow.

Workflow can be used for test workflows with requests to an API with refreshing access tokens.
