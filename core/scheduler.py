from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import stock_basic, stock_financial, stock_market


def start_scheduler():
    scheduler = BlockingScheduler()

    # 每天收盘后更新基础信息
    scheduler.add_job(stock_basic.run, 'cron', hour=18, minute=0)

    # 每天收盘后更新财务指标
    scheduler.add_job(stock_financial.run, 'cron', hour=18, minute=30)

    # 每天定时更新行情
    scheduler.add_job(stock_market.run, 'cron', hour=15, minute=5)

    scheduler.start()
