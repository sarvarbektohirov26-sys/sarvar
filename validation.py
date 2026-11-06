def get_valid_float(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print("Ошибка: значения должно быть в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введите число ")

def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        else:
            print("Ошибка: неверный выбор, попробуйте снова.")


 