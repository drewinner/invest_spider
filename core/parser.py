import pandas as pd


class StockParser:

    @staticmethod
    def parse_basic_info(df: pd.DataFrame) -> pd.DataFrame:
        """清洗基础信息"""
        return df[["股票代码", "股票简称", "所属行业", "市盈率-动态", "市净率"]]

    @staticmethod
    def parse_financial(df: pd.DataFrame) -> pd.DataFrame:
        """清洗财务指标"""
        return df[["trade_date", "pe_ttm", "pb", "roe", "grossprofit_margin"]]
