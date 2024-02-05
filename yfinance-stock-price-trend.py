# 请你研究三只股票的历史价格走势和交易量，分析股价波动与市场整体趋势的关连，输出可视化结果，请给出完整的python代码。
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf  # 请确保安装了yfinance库，可以使用 pip install yfinance 安装

# 指定股票代码
stocks = ['PDD', 'BABA', 'JD']

# 获取历史股价数据
data = yf.download(stocks, start='2017-01-01', end='2024-02-01', progress=False)

# 绘制股价走势图
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
for stock in stocks:
    plt.plot(data['Adj Close'][stock], label=stock)

plt.title('Stock Price Trend')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()

# 绘制交易量图
plt.subplot(2, 1, 2)
for stock in stocks:
    plt.plot(data['Volume'][stock], label=stock)

plt.title('Trading Volume Trend')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()

plt.tight_layout()
plt.show()
