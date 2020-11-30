# Run on terminal to install packages
# pip install pandas
# pip install matplotlib

# 1 - Required imports
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 2 - Load data from CSV file
path = 'C:\AllTech\Code\python\salesByDay.csv'

dateParse = (
    lambda x: pd.datetime.strptime(x, "%d/%m/%Y")
)

data = pd.read_csv(
    path,
    # What column to be parse to date?
    parse_dates=['day'],
    # What column to use as row index?
    index_col='day',
    # What function will handle string to date?
    date_parser=dateParse
    )

# 3 - Determing rolling statistics
# pd.rolling_mean(data, 90) # older pandas
rmean = data.rolling(90).mean()
rstd = data.rolling(90).std()

# 4 - Plot rolling statistics:
plt.plot(
    data, color = "blue", label = "Original"
)

plt.plot(
    rmean, color = "red", label = "Rolling Mean"
)

plt.plot(
    rstd, color = "black", label = "Rolling Standard"
)

plt.title("Rolling Mean & Standard Deviation")

#plt.savefig("C:\AllTech\Code\python\MyPlot.png")
plt.show()