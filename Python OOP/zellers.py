class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.day = day

        # Adjust month and year if January or February
        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        # Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        # Mapping result to days of the week
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

    def __str__(self):
        weekday = self.calculate_day_of_week()
        return f"The day of the week for {self.original_year}-{self.month if self.month <= 12 else self.month - 12}-{self.day} is {weekday}."


date = DateCalculator(1689, 9, 15)
print(date)
