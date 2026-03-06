rom datetime import datetime, timedelta
import re

def parse_date(date_str: str) -> datetime | None:
    # Примеры: "6 марта 2026", "завтра", "через 3 дня"
    today = datetime.now().date()

    if date_str.lower() == "завтра":
        return datetime.combine(today + timedelta(days=1), datetime.min.time())

    if date_str.lower().startswith("через"):
        days = int(re.search(r"\d+", date_str).group())
        return datetime.combine(today + timedelta(days=days), datetime.min.time())

    # Парсинг "6 марта 2026"
    try:
        return datetime.strptime(date_str, "%d %B %Y")
    except ValueError:
        return None
