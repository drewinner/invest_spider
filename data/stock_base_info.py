import pandas as pd
from utils.stock_exchange import get_exchange_by_code,get_market_board
from utils.pinyin import PinyinConverter
from utils.date_utils import get_timestamp_ms
from core.storage.storage_factory import StorageFactory
from configs.settings import DATABASE, STORAGE_TYPE


class DBStockBaseInfo:
    def saveOrUpdate (df:pd.DataFrame) :
        sql = """
        INSERT INTO stock_base_info (code,exchange, board_type,name, pinyin, create_time, update_time)
        VALUES (%s, %s,%s,%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            exchange=VALUES(exchange),
            board_type=VALUES(board_type),
            name = VALUES(name),
            pinyin = VALUES(pinyin),
            update_time = VALUES(update_time);
        """
        
        timeStampMs = get_timestamp_ms()
        converter = PinyinConverter()

        data = [(
                row["code"], 
                get_exchange_by_code(row["code"]),
                get_market_board(row["code"]),
                converter.clean_stock_name(row["name"]),
                converter.hanzi_to_pinyin(row["name"],mode="first"),
                timeStampMs,timeStampMs) 
                for _, row in df.iterrows()
            ]
        
        return StorageFactory.get_storage(STORAGE_TYPE, DATABASE).insert_many(sql,data)
    
    def getAll():
        last_id = 0
        batch_size=100
        storage = StorageFactory.get_storage(STORAGE_TYPE, DATABASE)
        allRows = []
        while True:
            sql = f"SELECT * FROM stock_base_info WHERE id > %s ORDER BY id ASC LIMIT {batch_size}"
            rows = storage.query(sql, (last_id))
            if not rows:
                break
            
            last_id = rows[-1]["id"]
            allRows.extend(rows)
            
        return allRows