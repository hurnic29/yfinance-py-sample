# 请分别计算三只股票的复合年均增长率和收益的年度波动率，并给出python代码。
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 指定股票代码
stocks = ['PDD', 'BABA', 'JD']

# 获取历史股价数据
data = yf.download(stocks, start='2020-01-01', end='2023-01-01', progress=False)['Adj Close']

# 计算每只股票的日收益率
returns = data.pct_change()

# 计算复合年均增长率
annual_returns = (1 + returns).resample('Y').prod() - 1
compound_annual_growth_rate = (1 + annual_returns.mean()) ** (1 / len(annual_returns.index.year.unique())) - 1

# 计算年度波动率
annual_volatility = returns.resample('Y').std() * np.sqrt(252)

# 打印结果
for stock in stocks:
    print(f"{stock}:")
    print(f"Compound Annual Growth Rate: {compound_annual_growth_rate[stock] * 100:.2f}%")
    # print(f"Annual Volatility: {annual_volatility[stock] * 100:.2f}%\n")
    print(f"Annual Volatility: {annual_volatility[stock] * 100}%")

# 如果你想可视化年度波动率，可以使用以下代码
plt.figure(figsize=(10, 6))
for stock in stocks:
    plt.plot(annual_volatility.index.year, annual_volatility[stock] * 100, label=stock)

plt.title('Annual Volatility')
plt.xlabel('Year')
plt.ylabel('Volatility (%)')
plt.legend()
plt.show()
