class Travel:
    def __init__(self, name, destination, start_date, end_date, budget):
        self.name = name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget

    def to_dict(self):
        return {
            "name": self.name,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget
        }

    @staticmethod
    def from_dict(data):
        return Travel(
            data["name"],
            data["destination"],
            data["start_date"],
            data["end_date"],
            data["budget"]
        )
# Створюємо об'єкт подорожі
my_trip = Travel("Відпустка", "Карпати", "2026-06-01", "2026-06-10", 15000)

# Виводимо дані на екран
print(f"Подорож: {my_trip.name} до міста {my_trip.destination}")
print(f"Бюджет: {my_trip.budget} грн")

# Перевіряємо метод to_dict
print("Словник:", my_trip.to_dict())