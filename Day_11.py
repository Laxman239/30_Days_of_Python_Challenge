from datetime import date

today = date.today()

try:
    target_day = today.replace(year=today.year + 1)
except ValueError:
    # Handles leap year (Feb 29 -> Feb 28 next year)
    target_day = today.replace(year=today.year + 1, day=28)

difference = target_day - today

print(f"🎯 Only {difference.days} days left until the next year!")