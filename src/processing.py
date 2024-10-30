def filter_by_state(data, state='EXECUTED'):
    """Фильтрация словарей по значению ключа "state"""
    return [item for item in data if item.get("state") == state]

def sort_by_date(data, reverse=True):
    """Сортирует список словарей по значению ключа "date"."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)