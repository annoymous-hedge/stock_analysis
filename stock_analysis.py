import pandas as pd


def read_data(path):
    df = pd.read_csv(path, encoding='latin1')
    df.columns = df.columns.str.strip()

    return df


def cal_roi(close):
    return round((close.iat[-1] - close[0]) / close[0], 2) * 100


def price_summary(close):
    return close.max(), close.min(), close.mean()


def cal_daily_returns(close):
    dr = round(close.pct_change() * 100, 2)
    dr.drop(labels=0, inplace=True)  # series
    avg = round(sum(dr) / len(dr) * 100, 2)
    return dr, avg


def flag_large_moves(date, daily_returns, threshold=2):
    df = pd.DataFrame({'Date': date, 'Daily Return': daily_returns})
    flags = df[abs(df['Daily Return']) > threshold]
    return flags


def main(path):
    df = read_data(path)
    date, close = df['Date'], df['Close']
    roi = cal_roi(close)
    max_price, min_price, ave_price = price_summary(close)
    daily_returns, average_daily_returns = cal_daily_returns(close)
    flags = flag_large_moves(date, daily_returns)

    print(f'Highest price: {max_price}\n'
          f'Lowest price: {min_price}\n'
          f'Average price: {ave_price}\n'
          f'Average daily return: {average_daily_returns}\n\n'
          f'⚠️ Days with large price moves (>2%):')
    for date, returns in flags.values.tolist():
        print(f'{date:<9}: {returns:>6.2f}%')    # no need .2f cause already round
        # print(f'{date.ljust(10)}: {str(returns).rjust(6)}')


if __name__ == '__main__':
    main('C:\\Users\\User\\PycharmProjects\\stock_analysis\\data\\tesla_stock.csv')







# read data
#     df = pd.read_csv(path, encoding='latin1')
#     df.columns = df.columns.str.strip()  # remove every space or special character
#
#     # get data
#     date = df['Date']
#     close = df['Close']
#
#     # calculate roi
#     roi = round((close.iat[-1] - close[0]) / close[0], 2) * 100
#
#     # find max/min price
#     max_price = close.max()
#     min_price = close.min()
#     ave_price = close.mean()
#
#     # calculate daily returns
#     daily_returns = round(close.pct_change() * 100, 2)
#     daily_returns.drop(labels=0, inplace=True)  # series
#     average_daily_returns = round(sum(daily_returns) / len(daily_returns) * 100, 2)
#
#     # flag large moves
#     date_daily_returns = pd.DataFrame({'Date': date, 'Daily Return': daily_returns})
#     flags = date_daily_returns[abs(date_daily_returns['Daily Return']) > 2]  # show the entire data frame
#     high = date_daily_returns['Daily Return'][date_daily_returns['Daily Return'] > 2]  # only daily return (no column)
#     # print(flags.to_string(index=False))
#     # flags.reset_index(drop=True)
#
#     # for date, returns in flags.values.tolist():
#     #     print(date, returns)
#     # print(flags.values.tolist())




