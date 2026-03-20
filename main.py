import models
import storage


def main():
    trips = storage.load_trips()
    while True:
        print("\n1. Додати 2. Список 3. Редагувати 4. Видалити 5. Пошук 6. Період 7. Сортувати 8. Статистика 0. Вихід")
        choice = input("Дія: ")

        if choice == "1":
            t = models.Trip(input("Назва: "), input("Місце: "), input("Початок (дд.мм.рррр): "), input("Кінець: "),
                            input("Бюджет: "))
            if t.start_date: trips.append(t); storage.save_trips(trips); print("Додано!")

        elif choice == "2":
            for i, t in enumerate(trips):
                print(f"{i + 1}. {t.name} ({t.destination}) | {t.budget} грн")

        elif choice == "4":
            idx = int(input("Номер для видалення: ")) - 1
            if 0 <= idx < len(trips): trips.pop(idx); storage.save_trips(trips)

        elif choice == "5":
            s = input("Назва: ").lower()
            for t in trips:
                if s in t.name.lower(): print(f"Знайдено: {t.name}")

        elif choice == "7":
            trips.sort(key=lambda x: x.start_date)
            storage.save_trips(trips);
            print("Відсортовано")

        elif choice == "8":
            count, total = models.calculate_stats(trips)
            print(f"Кількість: {count}, Бюджет: {total}")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()