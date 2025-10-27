def get_exchange_by_code(code: str) -> str:
    """
    根据股票代码判断所属交易所

    返回：
        'sh' - 上海证券交易所
        'sz' - 深圳证券交易所
        'bj' - 北京证券交易所
        ''   - 未知代码
    """
    if not code or not code.isdigit():
        return ""

    # 上交所（SH）
    if code.startswith(("600", "601", "603", "605", "688")):
        return "sh"
    # 深交所（SZ）
    elif code.startswith(("000", "001", "002", "003", "300")):
        return "sz"
    # 北交所（BJ）
    elif code.startswith(("830", "831", "832", "833", "835", "836", "837", "838", "839")):
        return "bj"
    else:
        return ""

def get_market_board(code: str) -> str:
    """
    根据股票代码判断所属板块（主板 / 创业板 / 科创板 / 北交所）
    参数:
        code (str): 股票代码（如 '600000', '000001', '300750', '688001', '832000')
    返回:
        str: 板块名称 ('主板' / '创业板' / '科创板' / '北交所' / '未知')
    """
    if not code or not code.isdigit():
        return "未知"

    if code.startswith(("688",)):  # 科创板
        return "科创板"
    elif code.startswith(("300",)):  # 创业板
        return "创业板"
    elif code.startswith(("830", "831", "832", "833", "835", "836", "837", "838", "839")):
        return "北交所"
    elif code.startswith(("000", "001", "002", "003", "600", "601", "603", "605")):
        return "主板"
    else:
        return "未知"
