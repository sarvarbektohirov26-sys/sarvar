from constants import PUMP_TYPES
from menu import show_pump_menu
from validation import get_valid_float, get_valid_choice
from operations import calculate_power, get_head_class
from logger import print_and_log
def main():
    print("-- Программа: Напор и мощность насоса --")
    show_pump_menu()
    pump_choice = get_valid_choice("Ваш выбор (1-3): ", PUMP_TYPES.keys())
    pump_name = PUMP_TYPES[pump_choice]["name"]
    efficiency = PUMP_TYPES[pump_choice]["efficiency"]
    print("\n--- Ввод параметров ---")
    q = get_valid_float("Подача Q, м³/ч (0.5 - 500): ", 0.5, 500.0)
    h = get_valid_float("Напор H, м (1 - 200): ", 1.0, 200.0)
    p = get_valid_float("Плотность среды p, кг/м³ (800 - 1200): ", 800.0, 1200.0)
    power = calculate_power(p, 9.81, q, h, efficiency)
    head_class = get_head_class(h)
    print("\n--- Результаты расчета ---")
    print_and_log(f"Тип насоса: {pump_name}")
    print_and_log(f"Подача (Q): {q} м³/ч")
    print_and_log(f"Напор (H): {h} м")
    print_and_log(f"Мощность (P): {power:.2f} кВт")
    print_and_log(f"Класс напора: {head_class}")

if __name__ == "__main__":
    main()