#!/usr/bin/env bash

pip install awsebcli --upgrade --ignore-installed

# Prepare deployment
echo "mkdir"
mkdir ~/.aws/
touch ~/.aws/credentials
printf "[eb-cli]\naws_access_key_id = %s\naws_secret_access_key = %s\n" "$AWS_ACCESS_KEY_ID" "$AWS_SECRET_ACCESS_KEY" >> ~/.aws/credentials
cat ~/.aws/credentials
touch ~/.aws/config
printf "[profile eb-cli]\nregion=us-east-1\noutput=json" >> ~/.aws/config
touch ~/.aws/config
eb init FlaskGitlabCi-staging -p python -r us-east-1
eb use FlaskGitlabCi-staging
eb deploy FlaskGitlabCi-staging -l FlaskGitlabCi-staging-$CI_COMMIT_SHA