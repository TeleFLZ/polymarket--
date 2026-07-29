
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# =====================================
# Polymarket API 配置
# =====================================

POLYMARKET_API_KEY = os.getenv("POLYMARKET_API_KEY", "")
POLYMARKET_API_SECRET = os.getenv("POLYMARKET_API_SECRET", "")
POLYMARKET_API_URL = os.getenv(
    "POLYMARKET_API_URL",
    "https://clob.polymarket.com"
)

# =====================================
# 钱包配置
# =====================================

PRIVATE_KEY = os.getenv("PRIVATE_KEY", "")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "")

# =====================================
# Telegram 机器人配置
# =====================================

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# =====================================
# 自动交易参数
# =====================================

DEFAULT_MARKET = os.getenv("DEFAULT_MARKET", "")

ORDER_SIZE = float(os.getenv("ORDER_SIZE", "10"))

MAX_POSITION = float(os.getenv("MAX_POSITION", "100"))

STOP_LOSS = float(os.getenv("STOP_LOSS", "0.05"))

TAKE_PROFIT = float(os.getenv("TAKE_PROFIT", "0.10"))

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "10"))

# =====================================
# 日志配置
# =====================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
