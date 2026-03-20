from datetime import datetime

class Trip:
    def init(self, name, destination, start_date_str, end_date_str, budget):
        self.name = name
        self.destination = destination
        self.start_date = self.validate_date(start_date_str)
        self.end_date = self.validate_date(end_date_str)
        self.budget = float(budget)

    @staticmethod
    def validate_date(date_str):
        """Перевірка та конвертація рядка у об'єкт дати (Кутинський)"""
        try:
            return datetime.strptime(date_str, "%d.%m.%Y")
        except (ValueError, TypeError):
            return None

    def to_dict(self):
        """Перетворення об'єкта в словник для збереження в JSON (Кутинський)"""
        return {
            "name": self.name,
            "destination": self.destination,
            "start_date": self.start_date.strftime("%d.%m.%Y") if self.start_date else "",
            "end_date": self.end_date.strftime("%d.%m.%Y") if self.end_date else "",
            "budget": self.budget
        }

def calculate_stats(trips):
    """Розрахунок статистики: кількість та загальний бюджет (Кутинський)"""
    total_trips = len(trips)
    total_budget = sum(trip.budget for trip in trips)
    return total_trips, total_budget