#coding=utf-8
import os
import time
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_dam.settings")
django.setup()
import warnings
warnings.filterwarnings('ignore')
import logging
logger = logging.getLogger(__name__)
collect_logger = logging.getLogger("collect")

# 在Django中的setting中设置下边的配置信息
from django.conf import settings

default_database = settings.DATABASES["default"]
host = default_database["HOST"]
port = int(default_database["PORT"])
user = default_database["USER"]
password = default_database["PASSWORD"]
database = default_database["NAME"]
# db_dict = ret()
# host = db_dict['db_host']
# port = int(db_dict['db_port'])
# user = db_dict['db_user']
# password = db_dict['db_pass']
# database = db_dict['db_name']
# print host,port,user,password,database

# success
def getCursorConn(host=host,port=port,user=user,password=password,database=database):
    """
    连接数据库返回cursor和conn
    :return:
    """
    import pymysql
    pymysql.install_as_MySQLdb()
    conn=pymysql.connect(host=host, port=port, user=user, password=password,database=database,charset="utf8")
    cursor=conn.cursor()
    return cursor,conn

#success
def closeCurseConn(cursor,conn):
    """
    关闭之前打开的cursor，conn
    :param cursor:
    :param conn:
    :return:
    """
    cursor.close()
    conn.close()

# success
def common_sql(cols_data,tb_name,condition,many=False):
    cursor, conn = getCursorConn()
    result = ""
    try:
        if condition:
            sql = "select "+cols_data+" from "+tb_name+" where "+condition
        else:
            sql = "select "+cols_data+" from "+tb_name
        cursor.execute(sql)
        result = cursor.fetchall() if many else cursor.fetchone()

    except Exception as e:
        print("common_sql"+str(e))
    finally:
        closeCurseConn(cursor, conn)
    return result

# success
def fetch_one_sql(str_cols_data,str_tb_name,str_condition=""):
    """
    查询表获取一行值,返回值如果是空表示没有查到数据query_data = {"str_cols_data": "","str_tb_name":"","str_condition":""}
    :param cols_data:
    :param tb_name:
    :param condition:
    :return:
    """
    result = common_sql(str_cols_data,str_tb_name,str_condition,False)

    return result
# one_sql = {"str_cols_data":" * ","str_tb_name":"xin_daba_unit_grid","str_condition":"uid='important-0716' and latitude>32.54756640 and latitude<32.54756642 and longitude>103.02737041 and longitude<103.02737043"}
# start_time = time.time()
# result = fetch_one_sql(**one_sql)
# end_time = time.time()
# print(result)
# print(end_time-start_time)


#success
def fetch_many_sql(str_cols_data,str_tb_name,str_condition=""):
    """
    查询多个数据,返回值如果是空表示没有查到数据query_data = {"str_cols_data": "","str_tb_name":"","str_condition":""}
    :param str_cols_data:
    :param str_tb_name:
    :param str_condition:
    :return:
    """
    return common_sql(str_cols_data,str_tb_name,str_condition,True)

# success
def update_sql(str_tb_name,str_cols_sql,str_condition=""):
    """
    返回false表示更新失败,true表示成功update_data = {"str_tb_name": "","str_cols_sql":"","str_condition":""}
    :param str_tb_name:
    :param str_cols_sql:
    :param str_condition:
    :return:
    """
    state = False
    try:
        cursor,conn = getCursorConn()
        sql = "update "+str_tb_name+" set "+str_cols_sql+" where "+str_condition
        # print('update sql', sql)
        cursor.execute(sql)
        conn.commit()
        state = True
    except Exception as e:
        print("common_sql"+str(e))
    finally:
        closeCurseConn(cursor,conn)
    return state

# success
def inset_sql(str_tb_name,str_insert_cols,str_cols_value,many=False):
    """
    inert_one_data = {"str_tb_name": "","str_insert_cols":"","str_cols_value":"(这个括号已经写过了)"}
    insert_many_data = {"str_tb_name": "","str_insert_cols":"","str_cols_value":"(这些括号自己写),(),()"}
    :param str_tb_name: 字符串类型表名
    :param str_insert_cols: 要插入的字段
    :param str_cols_value:  要插入的值 "(value1，value2)",多行插入"(value1，value2),(value1,value2)"
    :param many:
    :return: state = false 默认插入失败， true 成功
    """
    state = False
    try:
        cursor, conn = getCursorConn()
        if many:
            sql = "insert into " + str_tb_name + "( " + str_insert_cols + " ) values" + str_cols_value
        else:
            sql = "insert into "+str_tb_name+"( "+str_insert_cols+" ) values( "+str_cols_value+" )"
        cursor.execute(sql)
        conn.commit()
        state = True
    except Exception as e:
        print("inset_sql "+str(e))
    finally:
        closeCurseConn(cursor,conn)
    return state
