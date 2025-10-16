import os
import pandas as pd


class CSVStorage:
    """CSV 文件存储实现"""

    def __init__(self, config=None):
        self.save_dir = config.get("save_dir", "./data") if config else "./data"
        os.makedirs(self.save_dir, exist_ok=True)

    def save_dataframe(self, df, filename):
        filepath = os.path.join(self.save_dir, filename)
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        print(f"✅ 已保存 CSV 文件：{filepath}")
