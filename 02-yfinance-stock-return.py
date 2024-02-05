# 分析并获取每只股票最大交易总额的日期，并计算每只股票的日收益率、累计收益率。以图表形式展示，并给出python代码。
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# 指定股票代码
stocks = ['PDD', 'BABA', 'JD']

# 获取历史股价数据
data = yf.download(stocks, start='2020-01-01', end='2023-01-01', progress=False)

# 计算每只股票的日收益率
returns = data['Adj Close'].pct_change()

# 获取每只股票最大交易总额的日期
max_volume_dates = {stock: data['Volume'][stock].idxmax() for stock in stocks}

# 计算每只股票的日收益率和累计收益率
daily_returns = pd.DataFrame({stock: returns[stock] for stock in stocks})
cumulative_returns = (1 + daily_returns).cumprod() - 1

# 绘制每只股票的日收益率图表
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
for stock in stocks:
    plt.plot(daily_returns.index, daily_returns[stock], label=stock)
    plt.scatter(max_volume_dates[stock], daily_returns[stock].loc[max_volume_dates[stock]], color='red')

plt.title('Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()

# 绘制每只股票的累计收益率图表
plt.subplot(2, 1, 2)
for stock in stocks:
    plt.plot(cumulative_returns.index, cumulative_returns[stock], label=stock)
    plt.scatter(max_volume_dates[stock], cumulative_returns[stock].loc[max_volume_dates[stock]], color='red')

plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()

plt.tight_layout()
plt.show()
