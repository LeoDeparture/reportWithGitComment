# 以下面的建表语句为标准，创建若干张表，对应serviceDict.json中的各项服务
# salmon
CREATE TABLE IF NOT EXISTS `service-name`(
`buildNumber` INT UNSIGNED,
`serviceName` VARCHAR(100) DEFAULT 'service-name',
`taskFamily` VARCHAR(100) DEFAULT 'task-name',
`clusterName` VARCHAR(100) DEFAULT 'cluster-name',
`imageTag` VARCHAR(100) DEFAULT 'DEV',
`branchName` VARCHAR(100) DEFAULT 'develop',
`ecRegistry` VARCHAR(100) DEFAULT 'https://***.dkr.ecr.cn-northwest-1.amazonaws.com.cn',
`ecrRepo` VARCHAR(100) DEFAULT '***.dkr.ecr.cn-northwest-1.amazonaws.com.cn/salmon',
`taskRevision` INT UNSIGNED,
`gitHash` VARCHAR(100),
`gitComment` VARCHAR(1000),
PRIMARY KEY ( `buildNumber` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
