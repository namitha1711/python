from datetime import datetime, timedelta

def birthday_info(bday_str):
    bday = datetime.strptime(bday_str, "%Y-%m-%d")
    now = datetime.now()
    age = now - bday
    years = age.days // 365
    next_bday = bday.replace(year=now.year)
    if next_bday < now:
        next_bday = next_bday.replace(year=now.year + 1)
    diff = next_bday - now
    days, rem = diff.days, diff.seconds
    hours = rem // 3600
    minutes = rem % 3600 // 60
    seconds = rem % 60
    print(f"Age: {years} years")
    print(f"Time until next birthday: {days}d {hours}h {minutes}m {seconds}s")
