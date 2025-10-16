akshare_spider/
├── configs/                 # 配置文件目录
│   ├── settings.py          # 全局配置，比如数据库、日志、调度
│
├── core/                    # 核心模块
│   ├── fetcher.py           # 数据获取（调用 akshare）
│   ├── parser.py            # 数据清洗/指标提取
│   ├── storage.py           # 数据存储（CSV/MySQL/SQLite）
│   ├── scheduler.py         # 定时任务调度
│   └── logger.py            # 日志管理
│
├── tasks/                   # 爬取任务
│   ├── stock_basic.py       # 股票基础信息任务
│   ├── stock_financial.py   # 股票财务指标任务
│   ├── stock_market.py      # 股票行情任务
│   └── __init__.py
│
├── utils/                   # 工具库
│   ├── date_utils.py
│   └── common.py
│
├── main.py                  # 项目入口
├── requirements.txt
└── README.md

2. 安装包
pip3.11 install akshare pandas sqlalchemy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade

3. python3.11 -m venv .venv 创建虚拟环境
4. source .venv/bin/activate   windows: .venv\Scripts\activate
5. pip install -r requirements.txt
