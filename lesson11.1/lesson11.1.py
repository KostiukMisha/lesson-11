def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути нижче нуля")
    if age % 2 == 0:
        return "Вік парний."
    else:
        return "Вік непарний."

def main():
    try:
        age = int(input("Введіть ваш вік: ")) 
        result = check_age(age)     
        print(result)
    
    except ValueError as ve:
        print(f"Помилка: {ve}")

if __name__ == "__main__":
    main()
