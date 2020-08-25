#!/usr/local/bin/python3
#coding=utf-8
import json
import requests
import boto3,pymysql
from datetime import datetime, timezone

with open("serviceDict.json", 'r', encoding='UTF-8') as f:
    dict = json.load(f)
ecs = boto3.client('ecs')
prefix = 'https://cn-northwest-1.console.amazonaws.cn/ecs/home?region=cn-northwest-1#'
# /clusters/
# zhiwen-cluster-dev
# /services/
# app-protocol-service-dev-fargate
# /events

def readGitComment(serveiceName):
    db_host = '10.0.0.1'
    db_user = "username"
    db_pass = "passwd"
    database = 'service_info'

    db = pymysql.connect(db_host,db_user,db_pass,database)
    cursor = db.cursor()
    sql = "select buildNumber,gitHash,gitComment,buildUrl,commitUrl from `%s` ORDER BY buildNumber DESC ;" % serveiceName
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取第一条记录，cursor.fetchall()是获取全部，返回一个元祖
        # ('补充学员档案筛选逻辑-本条为模拟数据，仅用于测试',)
        comment = cursor.fetchone()
    except:
        # 发生错误时回滚
        db.rollback()
        comment = ("Null", "Null", "库中暂无数据", "Null", "Null", "Null")
    finally:
        db.close()
    if comment == None:
        comment = ("Null", "Null", "库中暂无数据", "Null", "Null", "Null")
    return comment

def dingMessage(content):
    botWebHook = 'https://oapi.dingtalk.com/robot/send?access_token=your_token'
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "markdown",
        "markdown": {
            "title":"AWS ECS SERVICE_STEADY_STATE Report ",
            "text": "# AWS ECS Service Report\n\n> 仅用于提示服务部署状态\n\n %s\n" % (content)
        },
        "at": {
            "atMobiles": [
                "***"
            ],
            "isAtAll": False
        }
    }
    message_json = json.dumps(message)
    report = requests.post(url=botWebHook,headers=header,data=message_json)

def lambda_handler(event, context):
    if event['detail']['eventName'] == 'SERVICE_STEADY_STATE':
        serveiceArn = event['resources'][0] # str.
        cluster = event['detail']['clusterArn'] # str.
        clusterName = cluster.replace('arn:aws-cn:ecs:cn-northwest-1:***:cluster/','')
        serveiceName = serveiceArn.replace('arn:aws-cn:ecs:cn-northwest-1:***:service/','')
        serviceEventsUrl = prefix + '/clusters/' + clusterName + '/services/' + serveiceName + '/events'

        r_describe_services = ecs.describe_services(cluster=clusterName,services=[serveiceName])
        # print(r_describe_services['services'][0]['events'][0]['message'])  # 输出第0条 event 的 message
        # print(r_describe_services['services'][0]['events'][0]['createdAt']) # 输出第0条 event 的 createtime，datetime.datetime类型
        interval = datetime.now(timezone.utc) - r_describe_services['services'][0]['events'][1]['createdAt']
        content = '所属集群：%s\n\n服务名称：%s\n\n服务状态：运行稳定，可以测试 @***\n\n[AWS控制台传送门](%s)\n\n' % (clusterName, serveiceName, serviceEventsUrl)
    if (interval.seconds // 900) < 1:
        if serveiceName in dict.keys():
            a = '#### 部署环境: %s\n\n' % dict[serveiceName]['ENV']
            b = '#### 业务描述: %s\n\n' % dict[serveiceName]['description']
            c = '> 以下为业务相关信息\n\n[构建编号: %s](%s)\n\n' % (readGitComment(serveiceName)[0],readGitComment(serveiceName)[3])
            d = '[CommitID: %s](%s%s)\n\n' % (readGitComment(serveiceName)[1],readGitComment(serveiceName)[4],readGitComment(serveiceName)[1])
            e = '### 更新摘要:%s\n\n' % readGitComment(serveiceName)[2].replace('+*+','\n - ',)
            content = content + a + b + c + d + e
        print('查询当前event到上一个事件的间隔： %s' % interval + '\n' + content)
        dingMessage(content)
    else:
        print('查询当前event到上一个事件的间隔： %s' % interval)
        print('本次event为AWS-ECS健康检测触发的service_steady_state')
