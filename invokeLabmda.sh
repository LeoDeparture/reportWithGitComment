#!/bin/zsh
lambda_name="updateGitComment"

serviceName='mis-website-service-dev-fargate'
buildNumber=1004
gitHash='dateornot'
gitComment='周末能不能约会去？'

event='{"tb_name":'\"$serviceName\"',"buildNumber":'\"$buildNumber\"',"gitHash":'\"$gitHash\"',"gitComment":'\"$gitComment\"'}'

aws lambda invoke \
    --function-name ${lambda_name} \
    --invocation-type Event \
    --payload $event \
    response.json