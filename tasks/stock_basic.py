import akshare as ak
from core.storage.storage_factory import StorageFactory
from configs.settings import DATABASE, STORAGE_TYPE
from core.logger import logger
from utils.pinyin import PinyinConverter
from utils.date_utils import get_timestamp_ms

class StockBasicInfo:

    def saveOrUpdateStockBaseInfo():
        logger.info("正在从 AkShare 获取股票基础信息...")
        
        df = ak.stock_info_a_code_name()

        if len(df) == 0:
            logger.error("获取数据失败，请检查 AkShare 配置")
            return

        sql = """
        INSERT INTO stock_base_info (code, name, pinyin, create_time, update_time)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            pinyin = VALUES(pinyin),
            update_time = VALUES(update_time);
        """

        timeStampMs = get_timestamp_ms()
        converter = PinyinConverter()

        data = [(
                row["code"], 
                converter.clean_stock_name(row["name"]),
                converter.hanzi_to_pinyin(row["name"],mode="first"),
                timeStampMs,timeStampMs) 
                for _, row in df.iterrows()
            ]
        
        storage = StorageFactory.get_storage(STORAGE_TYPE, DATABASE)
        storage.insert_many(sql, data)
        
        logger.info(f" 已写入 MySQL,共 {len(data)} 条。")
    

    
