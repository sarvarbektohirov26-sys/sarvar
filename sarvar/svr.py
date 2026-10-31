while True:
    try:
        n = int(input("Введите количество элементов в цепи: "))
        if n <= 0:
            print("Ошибка: количество элементов должно быть больше нуля. Попробуйте снова.")
            continue 
        break 
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте снова.\n")
total_resistance = 0.0 
print("\nНачинаем ввод сопротивлений:")
for i in range(n):
    while True:
        try:
            r = float(input(f"Введите сопротивление {i+1}-го элемента (Ом): "))
            if r < 0:
                print("Ошибка: сопротивление не может быть отрицательным. Попробуйте снова.")
                continue 
            break 
        except ValueError:
            print("Ошибка: нужно ввести число (можно с точкой). Попробуйте снова.")
total_resistance += r
print(f"\nОбщее сопротивление цепи: {total_resistance:.2f} Ом")