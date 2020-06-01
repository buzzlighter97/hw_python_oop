import datetime as dt



class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, rec):
        """ Adds a record in the list "records". """
        self.records.append(rec)

    def get_today_stats(self):
        """ Returns total amount for today. """
        today_date = dt.date.today()

        amounts = [
            rec.amount 
            for rec in self.records 
            if rec.date == today_date
        ]

        return sum(amounts)

    def get_today_remained(self):
        """ Returns remained amount for today. """
        return self.limit - self.get_today_stats()

    def get_week_stats(self):
        """ Returns total amount for the last week. """
        today_date = dt.date.today()
        week_ago_date = today_date - dt.timedelta(days=7)

        amounts = [
            rec.amount
            for rec in self.records
            if week_ago_date <= rec.date <= today_date
        ]

        return sum(amounts)
    



class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()

class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 80.0
    RUB_RATE = 1.0    

    def get_today_cash_remained(self, currency):
        """ Returns a string, where remained cash
         is shown in currency. 
         """
        currencies = {
            "eur": ("Euro", self.EURO_RATE),
            "usd": ("USD", self.USD_RATE),
            "rub": ("руб", self.RUB_RATE),
        }

        today_remained = self.get_today_remained()
        if today_remained == 0:
            return "Денег нет, держись"

        currency_name, currency_rate = currencies[currency]

        today_remained = round(today_remained/currency_rate, 2)

        if today_remained > 0:
            return f"На сегодня осталось {today_remained} {currency_name}"
        elif today_remained < 0:
            today_remained = abs(today_remained)
            return f"Денег нет, держись: твой долг - {today_remained} {currency_name}"

    

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """ Returns remained calories for today.
        """
        today_remained = self.get_today_remained()
        if today_remained <= 0:
            return "Хватит есть!"
        if today_remained > 0:
            return ("Сегодня можно съесть что-нибудь ещё, "
            f"но с общей калорийностью не более {today_remained} кКал")