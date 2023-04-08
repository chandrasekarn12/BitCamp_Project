from alpaca.trading.client import TradingClient
from config import *

trading_client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
account = trading_client.get_account()

