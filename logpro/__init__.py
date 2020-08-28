# # python3以上版本需要修改pymysql
import pymysql
# # 指定pymysql版本
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()