# 以下面的建表语句为标准，创建29张表，对应serviceDict.json中的各项服务
# salmon
CREATE TABLE IF NOT EXISTS `mis-website-service-dev-fargate`(
`buildNumber` INT UNSIGNED,
`serviceName` VARCHAR(100) DEFAULT 'mis-website-service-dev-fargate',
`taskFamily` VARCHAR(100) DEFAULT 'mis-website-task-dev-fargate',
`clusterName` VARCHAR(100) DEFAULT 'zhiwen-cluster-dev',
`imageTag` VARCHAR(100) DEFAULT 'DEV',
`branchName` VARCHAR(100) DEFAULT 'develop',
`ecRegistry` VARCHAR(100) DEFAULT 'https://412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn',
`ecrRepo` VARCHAR(100) DEFAULT '412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn/salmon',
`taskRevision` INT UNSIGNED,
`gitHash` VARCHAR(100),
`gitComment` VARCHAR(1000),
PRIMARY KEY ( `buildNumber` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `mis-website-service-staging-fargate`(
`buildNumber` INT UNSIGNED,
`serviceName` VARCHAR(100) DEFAULT 'mis-website-service-staging-fargate',
`taskFamily` VARCHAR(100) DEFAULT 'mis-website-task-staging-fargate',
`clusterName` VARCHAR(100) DEFAULT 'zhiwen-cluster-dev',
`imageTag` VARCHAR(100) DEFAULT 'STAGING',
`branchName` VARCHAR(100) DEFAULT 'release',
`ecRegistry` VARCHAR(100) DEFAULT 'https://412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn',
`ecrRepo` VARCHAR(100) DEFAULT '412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn/salmon',
`taskRevision` INT UNSIGNED,
`gitHash` VARCHAR(100),
`gitComment` VARCHAR(1000),
PRIMARY KEY ( `buildNumber` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `mis-website-service-fargate`(
`buildNumber` INT UNSIGNED,
`serviceName` VARCHAR(100) DEFAULT 'mis-website-service-fargate',
`taskFamily` VARCHAR(100) DEFAULT 'mis-website-task-fargate',
`clusterName` VARCHAR(100) DEFAULT 'zhiwen-cluster',
`imageTag` VARCHAR(100) DEFAULT 'PROD',
`branchName` VARCHAR(100) DEFAULT 'master',
`ecRegistry` VARCHAR(100) DEFAULT 'https://412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn',
`ecrRepo` VARCHAR(100) DEFAULT '412934042350.dkr.ecr.cn-northwest-1.amazonaws.com.cn/salmon',
`taskRevision` INT UNSIGNED,
`gitHash` VARCHAR(100),
`gitComment` VARCHAR(1000),
PRIMARY KEY ( `buildNumber` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;