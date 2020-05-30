import datetime as dt



class Calculator:

    def __init__(self,limit):
        self.limit = limit
        self.records = []
        
    
    def add_record(self,rec):
        """ Adds a record in the list "records". """
        self.records.append(rec)

    def get_today_stats(self):
        """ Returns total amount for today. """

        summ = 0
        for rec in self.records:
            if rec.date == dt.date.today():
                summ += rec.amount
        return summ

    def get_week_stats(self):
        """ Returns total amount for the last week. """

        summ = 0
        week = dt.timedelta(days=7)
        for rec in self.records:
            if (dt.date.today() - week) <= rec.date <= dt.date.today():
                summ += rec.amount
        return summ
    



class Record:
    def __init__(self,amount,comment,date=""):
        self.amount = amount
        self.comment = comment
        if date == "":
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()

class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 80.0

    def get_today_cash_remained(self, currency):
        """ Returns a string, where remained cash
         is shown in currency. 
         """

        remained = 0
        summ = self.get_today_stats()

        if currency == "usd":
            remained = round((self.limit - summ)/self.USD_RATE,2)
            currency = "USD"
        elif currency == "eur":
            remained = round((self.limit - summ)/self.EURO_RATE,2)
            currency = "Euro"
        elif currency == "rub":
            remained = round(self.limit - summ,2)
            currency = "руб"

        if remained > 0:
            return f"На сегодня осталось {remained} {currency}"
        elif remained == 0:
            return "Денег нет, держись"
        elif remained < 0:
            remained *= -1
            return f"Денег нет, держись: твой долг - {remained} {currency}"

    

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """ Returns remained calories for today.
        """

        summ = self.get_today_stats()

        remained = (self.limit - summ)

        if remained > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал"
        else:
            return "Хватит есть!"
