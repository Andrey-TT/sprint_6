import datetime
import random

today = datetime.date.today()
day1 = today + datetime.timedelta(days=1)
day2 = today + datetime.timedelta(days=2)
tomorrow = day1.strftime('%d.%m.%y')
day_after_tomorrow = day2.strftime('%d.%m.%y')

phone_num1 = f'8{random.randint(1000000000, 9999999999)}'
phone_num2 = f'7{random.randint(1000000000, 9999999999)}'

