# BASE UTILITY METHODS
#
# Contains methods to get account information, positions, and make orders
#

import config
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.client import TradingClient

trading_client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)


def get_account():
    return trading_client.get_account()


def get_positions():
    return trading_client.get_all_positions()


def order(symbol, qty, side):
    try:
        market_order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=side,
            time_in_force=TimeInForce.GTC
        )

        trading_client.submit_order(market_order_data)
        return True

    except Exception as e:
        print('order() error: {0}'.format(e))
        return False

