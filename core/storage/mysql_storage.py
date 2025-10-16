import pymysql
from dbutils.pooled_db import PooledDB

from core.logger import logger


class MySQLStorage:
    """
    MySQL 数据存储类，封装常见的数据库操作
    支持连接池、自动提交、异常捕获、日志记录
    """

    def __init__(self, db_config: dict):
        """
        初始化数据库连接池
        :param db_config: dict, 数据库配置项
        """
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=10,        # 允许的最大连接数，0表示无限制
            mincached=2,              # 初始化时的连接数量
            maxcached=5,              # 连接池最大缓存连接数
            blocking=True,            # 连接数达到上限时是否阻塞等待
            ping=0,                   # 检查连接可用性
            host=db_config["host"],
            port=db_config["port"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
            charset="utf8mb4",
            autocommit=True
        )
        logger.info("✅ MySQL 连接池初始化完成")

    # ---------------------------
    # 基础工具
    # ---------------------------
    def _get_conn(self):
        return self.pool.connection()

    # ---------------------------
    # 查询
    # ---------------------------
    def query(self, sql: str, params=None):
        """
        执行查询语句，返回结果列表
        """
        conn = self._get_conn()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, params)
            result = cursor.fetchall()
            logger.debug(f"MySQL QUERY: {sql} | params={params}")
            return result
        except Exception as e:
            logger.exception(f"MySQL 查询失败: {e} | SQL={sql}")
            return []
        finally:
            cursor.close()
            conn.close()

    # ---------------------------
    # 插入单条记录
    # ---------------------------
    def insert_one(self, sql: str, params):
        """
        执行单条插入
        """
        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, params)
            conn.commit()
            logger.debug(f"MySQL INSERT ONE: {sql} | {params}")
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            logger.exception(f"MySQL 插入失败: {e} | SQL={sql}")
            return None
        finally:
            cursor.close()
            conn.close()

    # ---------------------------
    # 批量插入
    # ---------------------------
    def insert_many(self, sql: str, data: list):
        """
        批量插入
        """
        if not data:
            logger.warning("⚠️ insert_many 数据为空，跳过执行")
            return 0

        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, data)
            conn.commit()
            logger.info(f"MySQL 批量插入成功，共 {len(data)} 条")
            return len(data)
        except Exception as e:
            conn.rollback()
            logger.exception(f"MySQL 批量插入失败: {e}")
            return 0
        finally:
            cursor.close()
            conn.close()

    # ---------------------------
    # 更新方法
    # ---------------------------
    def update(self, sql: str, params=None):
        """
        执行 UPDATE 操作
        """
        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            affected = cursor.execute(sql, params)
            conn.commit()
            logger.debug(f"MySQL UPDATE: {sql} | params={params}")
            return affected
        except Exception as e:
            conn.rollback()
            logger.exception(f"MySQL 更新失败: {e} | SQL={sql}")
            return 0
        finally:
            cursor.close()
            conn.close()

    # ---------------------------
    # 通用执行方法（适用于DDL等）
    # ---------------------------
    def execute(self, sql: str, params=None):
        """
        执行任意 SQL（如 CREATE / DROP）
        """
        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, params)
            conn.commit()
            logger.debug(f"MySQL EXECUTE: {sql}")
            return True
        except Exception as e:
            conn.rollback()
            logger.exception(f"MySQL 执行失败: {e} | SQL={sql}")
            return False
        finally:
            cursor.close()
            conn.close()
