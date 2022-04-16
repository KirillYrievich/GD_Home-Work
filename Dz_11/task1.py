class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def converter(cls, day_month_year):
        constructor = []
        for i in day_month_year.split():
            if i != '-': constructor.append(i)
        return int(constructor[0]), int(constructor[1]), int(constructor[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.converter(self.day_month_year)}'


date_today = Date("04 - 05 - 2022")

print(date_today)
print(Date.converter("4 - 5 - 2022"))
print(Date.valid(13, 25, 1000))
