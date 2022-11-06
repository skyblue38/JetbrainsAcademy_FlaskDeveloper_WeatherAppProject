class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars + cents // 100
        self.cents = cents % 100

    def add_money(self, deposit_dollars, deposit_cents):
        self.cents += deposit_cents
        self.dollars += deposit_dollars + self.cents // 100
        self.cents %= 100

