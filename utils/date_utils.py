import time
from datetime import datetime

def get_timestamp_ms():
    """
    获取当前时间的毫秒时间戳
    
    Returns:
        int: 13位毫秒时间戳
    """
    return int(time.time() * 1000)