class Token:
    def __init__(self, token_symbol):
        self.token_symbol = token_symbol
        self.price = None

    def update(self, timestamp, price):
        self.price = price
        self.timestamp = timestamp
