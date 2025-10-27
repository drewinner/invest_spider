import akshare as ak
from core.logger import logger
from data.stock_base_info import DBStockBaseInfo

class StockCompanyDetailInfo:
    @classmethod
    def saveOrUpdte(self):
        logger.info("StockDetailInfo 同步开始")

        rows = DBStockBaseInfo.getAll()
        for row in rows:
            stockInfo =self.get_stock_basic_info(row["code"])
            companInfo = self.get_company_info(row["exchange"]+row["code"])
            print(companInfo)
            break

    
        logger.info("StockDetailInfo 同步结束")

    @classmethod
    def get_stock_basic_info(self,symbol: str) -> dict:
        """
        获取单只股票关键信息，返回字典
        适配 DataFrame 结构：
            item                value
            0    最新                 11.4
            1  股票代码               000001
            2  股票简称                 平安银行
            3   总股本        19405918198.0
            4   流通股        19405600653.0
            5   总市值  221227467457.200012
            6  流通市值  221223847444.200012
            7    行业                   银行
            8  上市时间             19910403

        返回：
            dict: {item: value}
        """
        try:
            df = ak.stock_individual_info_em(symbol=symbol)
            if df is None or df.empty:
                return {}

            # 将 item 列作为 key，value 列作为 value
            info_dict = dict(zip(df["item"], df["value"]))

            # 可选：映射部分字段为统一 key
            mapped_dict = {
                "latest": info_dict.get("最新"),
                "code": info_dict.get("股票代码"),
                "name": info_dict.get("股票简称"),
                "total_share": info_dict.get("总股本"),
                "circulate_share": info_dict.get("流通股"),
                "total_market_value": info_dict.get("总市值"),
                "circulate_market_value": info_dict.get("流通市值"),
                "industry": info_dict.get("行业"),
                "list_date": info_dict.get("上市时间"),
            }

            return mapped_dict

        except Exception as e:
            print(f"获取 {symbol} 信息失败: {e}")
            return {}
        
    @classmethod
    def get_company_info(self,symbol: str) -> dict:
        try:
            df = ak.stock_individual_basic_info_xq(symbol=symbol)
            if df is None or df.empty:
                return {}

            return dict(zip(df["item"], df["value"]))
        
        except Exception as e:
            print(f"获取 {symbol} 信息失败: {e}")
            return {}