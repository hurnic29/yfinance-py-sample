# 请预测未来一个交易年度（252天）内三只股票潜在价格序列演变的单一模拟，基于遵循正态分布的每日收益随机的抽取。第一个图表中显示单线系列表示。第二个图表绘制一年期间这些随机每日收益的直方图。请给出python代码。
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 指定股票代码
stocks = ['PDD', 'BABA', 'JD']

# 模拟参数
num_days = 252  # 交易年度的天数
num_simulations = 1  # 模拟次数

# 获取历史股价数据
data = yf.download(stocks, start='2020-01-01', end='2023-01-01', progress=False)['Adj Close']
returns = data.pct_change().dropna()

# 模拟未来价格序列演变
simulated_prices = pd.DataFrame()

for stock in stocks:
    # 使用正态分布生成每日收益率
    daily_returns = np.random.normal(loc=returns[stock].mean(), scale=returns[stock].std(),
                                     size=(num_simulations, num_days))

    # 计算累计收益率
    cumulative_returns = np.cumprod(1 + daily_returns, axis=1) - 1

    # 计算模拟价格序列
    simulated_prices[stock] = data[stock].iloc[-1] * (1 + cumulative_returns.T)

# 绘制单一模拟的未来价格序列演变图表
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(simulated_prices[stock], label=stock)

plt.title('Simulated Future Stock Prices')
plt.xlabel('Trading Days')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

# 绘制每日收益的直方图
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.hist(np.ravel(daily_returns), bins=30, alpha=0.5, label=stock)

plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.legend()
plt.show()
