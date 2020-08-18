#!/usr/local/bin/python3
#coding:utf-8
import pymysql,json
def readGitComment():
    db_host = '52.82.95.113'
    # db_host = '10.0.0.16'
    db_user = "root"
    db_pass = "lnnfenwdf^T&^(2489..1"
    database = 'service_info'

    db = pymysql.connect(db_host,db_user,db_pass,database)
    cursor = db.cursor()
    sql = "INSERT INTO `mis-website-service-dev-fargate` (buildNumber,gitHash,gitComment) VALUES (997,'8d25s4dae641','我亦留此地-本条为模拟数据，仅用于测试');"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取第一条记录，cursor.fetchall()是获取全部，返回一个元祖
        # ('补充学员档案筛选逻辑-本条为模拟数据，仅用于测试',)
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    readGitComment()