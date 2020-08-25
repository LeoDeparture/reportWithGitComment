import json
import pymysql

def lambda_handler(event, lambda_context):
    db_host = '10.0.0.1'
    db_user = "user"
    db_pass = "passwd"
    database = 'service_info'

    tb_name = event["tb_name"]
    buildNumber = event["buildNumber"]
    gitHash = event["gitHash"]
    gitComment = event["gitComment"]

    db = pymysql.connect(db_host, db_user, db_pass, database)
    cursor = db.cursor()
    sql = "INSERT INTO `%s` (buildNumber,gitHash,gitComment,buildUrl) VALUES (%i,'%s','%s','%s');" % (tb_name, buildNumber, gitHash, gitComment, buildUrl)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
    except:
        # 发生错误时回滚
        print("SQL执行失败，rollback...")
        db.rollback()
    finally:
        db.close()
