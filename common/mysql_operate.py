import pymysql
import os
from small_FrontalGate.common.read_data import data
from small_FrontalGate.common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mysql"]
# print(test_data)

DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}


class MysqlDb():

    def __init__(self, db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info(f"操作MySQL出现错误，错误原因：{e}")
            # 报错后，回滚所有更改
            self.conn.rollback()

    def executemany_db(self, sql):
        """大批量创建多条数据"""
        values = []
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 从第6条往后批量创建94条
            for i in range(6, 100):
                values.append((i, '测试数据' + str(i)))
            # sql = 'insert into stu(id,name) values(%s,%s)' 这样写

            self.cur.executemany(sql, values)
            self.conn.commit()
            print('-------------- 批量创建成功 --------------')
        except Exception as e:
            logger.info(f"操作MySQL出现错误，错误原因：{e}")
            # 报错后，回滚所有更改
            self.conn.rollback()


db = MysqlDb(DB_CONF)
# sql = 'insert into stu(id,name) values(%s,%s)'
sql = 'select name from stu where id=99'
d = db.select_db(sql)
print(d)