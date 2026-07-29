# polymarket--
基于 Python 开发的 Polymarket 自动交易机器人，支持策略交易、风险控制、Telegram 通知和自动执行。
# Polymarket 自动交易机器人

一个基于 Python 的 Polymarket 自动交易项目。

## 📌 项目简介

本项目用于研究和开发自动化交易策略，采用模块化设计，方便维护、扩展和二次开发。

---

# 📂 项目结构

```
polymarket-bot/
│
├── config.py
├── trader.py
├── strategy.py
├── risk_manager.py
├── telegram_bot.py
├── main.py
└── requirements.txt
```

---

## 📄 文件说明

### config.py

用于管理项目配置。

主要包括：

- API 配置
- 钱包配置
- Telegram 配置
- 风险参数
- 交易参数

---

### trader.py

交易执行模块。

负责：

- 创建订单
- 提交订单
- 查询市场信息
- 管理持仓
- 执行交易流程

---

### strategy.py

交易策略模块。

可用于实现不同的策略，例如：

- 趋势策略
- 概率策略
- 自动买入
- 自动卖出
- 自定义信号

---

### risk_manager.py

风险控制模块。

负责：

- 最大仓位限制
- 最大亏损限制
- 风险评估
- 仓位控制
- 自动止损

---

### telegram_bot.py

Telegram 通知模块。

功能包括：

- 推送交易通知
- 推送订单状态
- 推送异常信息
- 接收简单指令
- 查询机器人状态

---

### main.py

程序入口。

负责：

- 初始化配置
- 加载交易策略
- 启动机器人
- 运行主循环

---

### requirements.txt

Python 依赖列表。

安装：

```bash
pip install -r requirements.txt
```

---

# 🚀 使用方法

安装依赖：

```bash
pip install -r requirements.txt
```

修改配置：

```
config.py
```

启动程序：

```bash
python main.py
```

---

# ⚙️ 开发环境

- Python 3.10+
- Git
- Telegram Bot API（可选）
- Polymarket API（根据实际实现）

---

# 📦 项目特点

✅ 模块化设计

✅ 易于扩展

✅ 支持策略开发

✅ 支持风险控制

✅ 支持 Telegram 通知

---

# ⚠️ 免责声明

本项目仅供学习、研究和开发参考。

使用者应自行承担因运行、修改或部署本项目而产生的风险和责任。

---

# License

MIT License
