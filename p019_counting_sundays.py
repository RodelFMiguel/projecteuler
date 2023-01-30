from datetime import datetime, timedelta

def count_sundays():
    start_date = datetime(1901, 1, 1)
    end_date = datetime(2000, 12, 31)
    date = start_date
    count = 0
    while date <= end_date:
        if date.weekday() == 6 and date.day == 1:
            count += 1
        date += timedelta(days=1)
    return count

print(count_sundays())
