import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 指定股票代码
stocks = ['PDD', 'BABA', 'JD']

# 模拟参数
num_days = 252  # 交易年度的天数
num_simulations = 1000  # 模拟次数

# 获取历史股价数据
data = yf.download(stocks, start='2020-01-01', end='2023-01-01', progress=False)['Adj Close']
returns = data.pct_change().dropna()

# 蒙特卡洛模拟
simulated_prices = pd.DataFrame()

for _ in range(num_simulations):
    simulated_returns = np.random.normal(loc=returns.mean(), scale=returns.std(), size=(num_days, len(stocks)))
    cumulative_returns = np.cumprod(1 + simulated_returns, axis=0) - 1
    simulated_prices = pd.concat([simulated_prices, data.iloc[-1] * (1 + cumulative_returns.T)])

# 绘制蒙特卡洛模拟的股价演变图表
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(simulated_prices[stock], alpha=0.1, color='blue')

plt.title('Monte Carlo Simulation of Stock Prices')
plt.xlabel('Trading Days')
plt.ylabel('Stock Price')
plt.show()
