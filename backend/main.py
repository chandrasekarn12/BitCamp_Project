import config
from alpaca.trading.client import TradingClient


trading_client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
account = trading_client.get_account()

