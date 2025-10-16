from .mysql_storage import MySQLStorage
from .csv_storage import CSVStorage


class StorageFactory:
    """根据配置创建存储实例"""

    @staticmethod
    def get_storage(storage_type, config):
        storage_type = storage_type.lower()
        if storage_type == "mysql":
            return MySQLStorage(config)
        elif storage_type == "csv":
            return CSVStorage(config)
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
