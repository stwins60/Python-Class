import stocker
import pyfiglet
import pandas as pd
# from stocker import Stocker

df = pd.read_csv('tickers.csv', delimiter=',')

symbol = df['Symbol'].tolist()
name = df['Name'].tolist()
#
# # print(f"{symbol} - {name}")
# print(symbol)
# print(name)
#
ticker_dict = {}

for key in symbol:
    for value in name:
        ticker_dict[key] = value
        name.remove(value)
        break

ticker_dict['D'] = 'Dogecoin'
logo = pyfiglet.figlet_format("Crypto Predictor")
print(logo)

ticker = input("Enter the Crypto Currency Symbol: ")
for i in ticker_dict.keys():
    if i == ticker:
        name = ticker_dict.get(i)
        data = stocker.predict.tomorrow(i, training=0.1, years=2, error_method='mape', plot=True, period=7)

        print(f"{name} is {data}")
