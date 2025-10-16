from tasks.stock_basic import run_stock_basic

if __name__ == "__main__":
    run_stock_basic()



# if __name__ == "__main__":
#     stock_code = "600519"  # 平安银行

    # 1. 实时行情
    # realtime_df = StockFetcher.get_stock_realtime()
    # print("实时行情：", realtime_df)
    # Storage.save_to_csv(realtime_df, f"{stock_code}_realtime.csv")

    # 2. 历史行情
    # history_df = StockFetcher.get_stock_history(stock_code, start="20220101", end="20220631")
    # print("历史行情：", history_df.head())
    # Storage.save(history_df, f"{stock_code}_history.csv")


    # fin_df = StockFetcher.get_stock_financial(stock_code)
    # print("财务指标：", fin_df)


    # https://akshare.akfamily.xyz/data/stock/stock.html#id247
    # 获取 A 股股票代码与名称
    # stock_info_a_code_name_df = ak.stock_info_a_code_name()
    # 遍历并打印全部股票代码与名称
    # for index, row in stock_info_a_code_name_df.iterrows():
    #     print(f"{index+1:04d}. 代码: {row['code']}, 名称: {row['name']}")


    # Storage.save(fin_df, f"{stock_code}_financial.csv")

    # 3. 财务指标
    # fin_df = StockFetcher.get_stock_financial(stock_code)
    # print("财务指标：", fin_df.head())
    # Storage.save(fin_df, f"{stock_code}_financial.csv")

    # 4. 个股信息
    # stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
    # print(stock_individual_info_em_df)
    
    # stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(symbol="SH601127")
    # print(stock_individual_basic_info_xq_df)

