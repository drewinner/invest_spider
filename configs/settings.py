# 数据库配置
DATABASE = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "invest",
}

# 存储类型：mysql 或 csv
STORAGE_TYPE = "mysql"

# CSV 保存配置
CSV_CONFIG = {
    "save_dir": "./data"
}

# 日志
LOG_CONFIG = {
    "log_dir": "./logs",
    "log_name": "akshare_spider"
}