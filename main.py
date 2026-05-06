import models
import storage
from datetime import datetime


def main():
    trips = storage.load_trips()
    while True:
        print("\n" + "=" * 50)
        print("1. Додати   2. Список    3. Редагувати  4. Видалити")
        print("5. Пошук    6. Період    7. Сортувати   8. Статистика")
        print("0. Вихід")
        print("=" * 50)

        choice = input("Дія: ")

        if choice == "1":
            try:
                name = input("Назва: ")
                dest = input("Місце: ")
                start_str = input("Початок (дд.мм.рррр): ")
                end_str = input("Кінець (дд.мм.рррр): ")
                budget = input("Бюджет: ")

                start_date = datetime.strptime(start_str, "%d.%m.%Y")
                end_date = datetime.strptime(end_str, "%d.%m.%Y")

                t = models.Trip(name, dest, start_date, end_date, budget)
                trips.append(t)
                storage.save_trips(trips)
                print("✅ Успішно додано!")
            except ValueError:
                print("❌ Помилка! Невірний формат дати (дд.мм.рррр).")

        elif choice == "2":
            if not trips:
                print("📭 Список порожній.")
            else:
                for i, t in enumerate(trips):
                    # Безпечне відображення дати
                    d_show = t.start_date.strftime("%d.%m.%Y") if hasattr(t.start_date, 'strftime') else str(
                        t.start_date)
                    print(f"{i + 1}. {t.name} ({t.destination}) | {d_show} | {t.budget} грн")

        elif choice == "3":
            try:
                idx = int(input("Номер для редагування: ")) - 1
                if 0 <= idx < len(trips):
                    t = trips[idx]
                    print(f"--- Редагування: {t.name} ---")
                    t.name = input(f"Нова назва [{t.name}]: ") or t.name
                    t.destination = input(f"Нове місце [{t.destination}]: ") or t.destination

                    s_inp = input(f"Нова дата початку [{t.start_date}]: ")
                    if s_inp: t.start_date = datetime.strptime(s_inp, "%d.%m.%Y")

                    e_inp = input(f"Нова дата кінця [{t.end_date}]: ")
                    if e_inp: t.end_date = datetime.strptime(e_inp, "%d.%m.%Y")

                    t.budget = input(f"Новий бюджет [{t.budget}]: ") or t.budget
                    storage.save_trips(trips)
                    print("✅ Оновлено!")
                else:
                    print("❌ Невірний номер.")
            except Exception as e:
                print(f"❌ Помилка: {e}")

        elif choice == "4":
            try:
                idx = int(input("Номер для видалення: ")) - 1
                if 0 <= idx < len(trips):
                    trips.pop(idx)
                    storage.save_trips(trips)
                    print("🗑️ Видалено.")
            except:
                print("❌ Помилка введення.")

        elif choice == "5":
            s = input("Пошук: ").lower()
            for t in trips:
                if s in t.name.lower(): print(f"🔍 {t.name} ({t.destination})")

        elif choice == "6":
            try:
                s_d = datetime.strptime(input("З (дд.мм.рррр): "), "%d.%m.%Y")
                e_d = datetime.strptime(input("По (дд.мм.рррр): "), "%d.%m.%Y")
                for t in trips:
                    if hasattr(t.start_date, 'year'):
                        if s_d <= t.start_date <= e_d:
                            print(f"📍 {t.name}: {t.start_date.strftime('%d.%m.%Y')}")
            except:
                print("❌ Невірна дата.")

        elif choice == "7":
            # Сортуємо, ігноруючи записи з помилковими датами
            trips.sort(key=lambda x: x.start_date if hasattr(x.start_date, 'year') else datetime.min)
            storage.save_trips(trips)
            print("🚀 Відсортовано!")

        elif choice == "8":
            # Якщо функція в models.py ламається, рахуємо прямо тут (це надійніше)
            count = len(trips)
            total = 0
            for t in trips:
                try:
                    total += float(t.budget)
                except:
                    continue
            print(f"📊 Статистика:")
            print(f"Кількість подорожей: {count}")
            print(f"Загальний бюджет: {total} грн")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()