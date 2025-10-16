# -*- coding: utf-8 -*-
"""
pinyin_utils.py
汉字转拼音工具类
依赖: pip install pypinyin
"""

from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict
import re

class PinyinConverter:
    def __init__(self):
        # 可选：加载一些常见多音词
        load_phrases_dict({
            '重庆': [['chong'], ['qing']],
            '长安': [['chang'], ['an']],
            '朝阳': [['chao'], ['yang']],
        })

    def hanzi_to_pinyin(self, text, mode="normal", sep=""):
        """
        汉字转拼音
        :param text: 输入汉字
        :param mode: 模式:
            - normal: 普通拼音（不带声调）
            - tone: 带声调（数字表示声调）
            - first: 首字母
            - abbrev: 拼音首字母简拼（连写）
        :param sep: 拼音之间的分隔符（仅在非简拼模式下生效）
        :return: 转换后的字符串
        """

        cleanText = self.clean_stock_name(name=text)

        if not cleanText:
            return ""

        if mode == "normal":
            result = lazy_pinyin(cleanText)
            return sep.join(result)

        elif mode == "tone":
            result = pinyin(cleanText, style=Style.TONE3)
            return sep.join(item[0] for item in result)

        elif mode == "first":
            result = lazy_pinyin(cleanText, style=Style.FIRST_LETTER)
            return sep.join(result)

        elif mode == "abbrev":
            result = pinyin(cleanText, style=Style.FIRST_LETTER)
            return "".join(item[0] for item in result)

        else:
            raise ValueError(f"未知模式: {mode}")
        
    def clean_stock_name(self,name: str) -> str:
        """
        清洗股票名称：
        - 去除前缀标识 (*ST、ST、XD、XR、DR、N、C、U 等)
        - 去除英文字母、数字、空格、标点
        - 仅保留汉字
        """
        if not isinstance(name, str):
            return ""

        # 去掉空格
        name = name.strip().replace(" ", "")

        # 去掉常见前缀标识（不区分大小写）
        # 顺序很重要，*ST要放前面
        name = re.sub(r'^\*?ST', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^(XD|XR|DR|N|C|U)', '', name, flags=re.IGNORECASE)

        # 去掉中间或末尾的英文字母（A股、B股等）
        name = re.sub(r'[A-Za-z]+', '', name)

        # 仅保留汉字（去掉数字、标点等）
        name = re.sub(r'[^\u4e00-\u9fa5]', '', name)

        return name