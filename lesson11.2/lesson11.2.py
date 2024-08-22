def get_day_of_week(number):
    days_of_week = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }

    if number in days_of_week:
        return days_of_week[number]
    else:
        return "Неправильний номер. Введіть число від 1 до 7."

def main():
    try:
        number = int(input("Введіть число від 1 до 7 яке відповідає дню тижня: "))
        
        day = get_day_of_week(number)
        
        print(day)
    
    except ValueError:
        print("Помилка: Будь ласка, введіть коректне число.")

if __name__ == "__main__":
    main()
