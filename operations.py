from constants import G
def calculate_power(p, g, q, h, efficiency):
    power = (p * g * q * h) / (3600 * 1000 * efficiency)
    return power
def get_head_class(h):
    if h < 10:
        return "Малый напор"
    elif 10 <= h <= 60:
        return "Средний напор"
    else:
        return "Высокий напор"
    