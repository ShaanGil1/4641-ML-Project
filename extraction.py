import simfin as sf
import pandas as pd
import matplotlib as plt

from simfin.names import *

def getData():
    sf.set_api_key('free')

    # Set the local directory where data-files are stored.
    # The dir will be created if it does not already exist.
    sf.set_data_dir('~/simfin_data/')

    # Load daily share-prices for all companies in USA.
    # The data is automatically downloaded if you don't have it already.
    df_prices = sf.load_shareprices(market='us', variant='daily')

    # Plot the closing share-prices for ticker MSFT.
    msft_close_values_TEMP = df_prices.loc['MSFT']

    print(msft_close_values_TEMP.columns)

    list_of_stocks = ['AAPL', 'MSFT', 'CLDR', 'CRM', 'TSLA', 'NVDA', 'DAL']

    big_df = pd.DataFrame()
    for stock in list_of_stocks:
        temp_df = df_prices.loc[stock].tail(100)
        temp_df = temp_df[["SimFinId", "Close", "Open", "High", "Low"]]
        big_df = pd.concat([big_df, temp_df])

    ultimate_df = big_df

    return ultimate_df


def plottingExperiments(df_prices):
    #PLOTTING
    msft_close_values= df_prices.loc['MSFT']
    msft_close_values = msft_close_values[["Close", "Open", "High", "Low"]]
    msft_close_values.plot(grid=True, figsize=(10, 5), title='MSFT Close')

    aapl_close_values = df_prices.loc['AAPL', CLOSE].tail(100)
    aapl_close_values.plot(grid=True, figsize=(10, 5), title='APPL Close')

    print(type(msft_close_values))

    #plt.scatter(x, y)

if __name__ == '__main__':
    data = getData()
    #plottingExperiments()

