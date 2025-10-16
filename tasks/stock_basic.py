import akshare as ak
from core.storage.storage_factory import StorageFactory
from configs.settings import DATABASE, STORAGE_TYPE
from core.logger import logger


def run_stock_basic():
    logger.info("📊 正在从 AkShare 获取股票基础信息...")
    
    df = ak.stock_info_a_code_name()
    logger.info(f"获取到 {len(df)} 条数据")

    if len(df) == 0:
        logger.error("获取数据失败，请检查 AkShare 配置")
        return

    sql = """
    INSERT INTO `stock_base_info` (code, name)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE code = VALUES(code)
    """
    data = [(row["code"], row["name"]) for _, row in df.iterrows()]
    storage = StorageFactory.get_storage(STORAGE_TYPE, DATABASE)
    storage.insert_many(sql, data)
    
    logger.info(f" 已写入 MySQL，共 {len(data)} 条。")
    

    
