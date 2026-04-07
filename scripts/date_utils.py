from datetime import datetime

def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def days_between(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)
