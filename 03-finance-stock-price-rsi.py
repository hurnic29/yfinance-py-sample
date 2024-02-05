import pandas as pd
# 请应用技术指标（如移动平均线、相对强弱指数等）来预测价格走势，并利用图标分析来识别趋势和交易模式。请给出完整的python代码。
import matplotlib.pyplot as plt
import yfinance as yf
import talib

# 指定股票代码
stock = 'AAPL'

# 获取历史股价数据
data = yf.download(stock, start='2020-01-01', end='2023-01-01', progress=False)

# 计算移动平均线（使用简单移动平均）
data['SMA_50'] = talib.SMA(data['Adj Close'], timeperiod=50)
data['SMA_200'] = talib.SMA(data['Adj Close'], timeperiod=200)

# 计算相对强弱指数（14天）
data['RSI'] = talib.RSI(data['Adj Close'], timeperiod=14)

# 绘制股价图表和移动平均线
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Adj Close'], label='Stock Price', color='black')
plt.plot(data.index, data['SMA_50'], label='50-day SMA', linestyle='--', color='blue')
plt.plot(data.index, data['SMA_200'], label='200-day SMA', linestyle='--', color='red')

# 标记交叉点
buy_signals = data[data['SMA_50'] > data['SMA_200']]
sell_signals = data[data['SMA_50'] < data['SMA_200']]
plt.scatter(buy_signals.index, buy_signals['Adj Close'], marker='^', color='g', label='Buy Signal')
plt.scatter(sell_signals.index, sell_signals['Adj Close'], marker='v', color='r', label='Sell Signal')

plt.title(f'{stock} Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

# 绘制相对强弱指数图表
plt.figure(figsize=(14, 5))
plt.plot(data.index, data['RSI'], label='RSI', color='purple')
plt.axhline(70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='g', linestyle='--', label='Oversold (30)')
plt.title(f'{stock} Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.show()
