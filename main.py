import logging

from trader import Trader
from strategy import Strategy
from risk_manager import RiskManager
from telegram_bot import TelegramBot


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    """
    项目主入口（示例模板）
    """

    logging.info("正在启动项目...")

    trader = Trader(config=None)
    strategy = Strategy()
    risk_manager = RiskManager()
    telegram = TelegramBot()

    telegram.connect()
    trader.connect()

    logging.info("所有模块加载完成")

    market_data = trader.get_market_info()

    signal = strategy.generate_signal(market_data)

    logging.info(f"当前信号：{signal}")

    risk_manager.evaluate()

    telegram.send_status()

    trader.disconnect()

    telegram.stop()

    logging.info("程序已结束")


if __name__ == "__main__":
    main()
