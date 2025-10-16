import pymysql
from dbutils.pooled_db import PooledDB


class MySQLPool:
    """MySQL 连接池封装"""

    def __init__(self, host, port, user, password, database, min_conn=1, max_conn=5):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=max_conn,
            mincached=min_conn,
            maxcached=max_conn,
            blocking=True,
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def get_conn(self):
        """获取连接"""
        return self.pool.connection()
