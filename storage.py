import json
from models import travel

FILENAME = "trips_data.json"

def save_trips(trips):
    """Збереження списку подорожей у файл (Кутинський)"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in trips], f, ensure_ascii=False, indent=4)

def load_trips():
    """Завантаження даних з файлу (Седлак)"""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            loaded_trips = []
            for item in data:
                loaded_trips.append(Trip(
                    item['name'], item['destination'],
                    item['start_date'], item['end_date'], item['budget']
                ))
            return loaded_trips
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def filter_by_date_range(trips, start_limit, end_limit):
    """Пошук подорожей, що потрапляють у вказаний період (Седлак)"""
    return [t for t in trips if t.start_date >= start_limit and t.end_date <= end_limit]