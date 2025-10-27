import akshare as ak
from core.storage.storage_factory import StorageFactory
from configs.settings import DATABASE, STORAGE_TYPE
from core.logger import logger
from data.stock_base_info import DBStockBaseInfo

class StockBasicInfo:
    def saveOrUpdate():
        logger.info("正在从 AkShare 获取股票基础信息...")
        
        df = ak.stock_info_a_code_name()
        if len(df) == 0:
            logger.error("获取数据失败，请检查 AkShare 配置")
            return

        total =  DBStockBaseInfo.saveOrUpdate(df)
        
        logger.info(f" 已写入 MySQL,共 {total} 条。")
    

    
