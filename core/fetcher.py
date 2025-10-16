import akshare as ak
import pandas as pd


class StockFetcher:

    @staticmethod
    def get_stock_basic() -> pd.DataFrame:
        """获取股票基础信息（代码、名称、行业、市盈率等）"""
        return ak.stock_individual_info_em(symbol="000001")  # 可循环所有股票

    @staticmethod
    def get_stock_realtime() -> pd.DataFrame:
        """A股实时行情"""
        return ak.stock_zh_a_spot_em()

    @staticmethod
    def get_stock_history(stock_code: str, start: str, end: str) -> pd.DataFrame:
        """日K线"""
        return ak.stock_zh_a_hist(symbol=stock_code, period="daily",
                                  start_date=start, end_date=end, adjust="qfq")

    @staticmethod
    def get_stock_financial(stock_code: str) -> pd.DataFrame:
        """财务指标（PE、PB、ROE等）"""
        return ak.stock_individual_info_em(stock_code)
