from alpaca.trading.client import TradingClient

API_KEY = "PKGK3ZI8BEG3QD3JCJLL"
SECRET_KEY = "XXiJ5gSrOG4v0LuOADi9gquNElFEkSkepmyacG0v"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()

