#!/bin/zsh
lambda_name="updateGitComment"

serviceName='service-dev-fargate'
buildNumber=1004
gitHash='dat34eor82t'
gitComment='测试用的备注信息001'

event='{"tb_name":'\"$serviceName\"',"buildNumber":'\"$buildNumber\"',"gitHash":'\"$gitHash\"',"gitComment":'\"$gitComment\"'}'

aws lambda invoke \
    --function-name ${lambda_name} \
    --invocation-type Event \
    --payload $event \
    response.json
