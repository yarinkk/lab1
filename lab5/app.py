def calculate_weight_cost(weight):
    """
    Розрахунок вартості за вагою

    >>> calculate_weight_cost(2)
    40
    >>> calculate_weight_cost(0)
    0
    """
    if weight < 0:
        raise ValueError("Weight cannot be negative")

    return weight * 20


def add_express_fee(base, express):
    """
    Додає оплату за термінову доставку

    >>> add_express_fee(100, True)
    150
    >>> add_express_fee(100, False)
    100
    """
    if express:
        return base + 50
    return base


def calculate_total_cost(weight, express=False):
    """
    Загальна вартість доставки

    >>> calculate_total_cost(2, True)
    90
    >>> calculate_total_cost(3, False)
    60
    """
    base = calculate_weight_cost(weight)
    return add_express_fee(base, express)


if __name__ == "__main__":
    weight = float(input("Введіть вагу: "))
    express_input = input("Термінова доставка? (y/n): ")

    express = express_input.lower() == "y"

    total = calculate_total_cost(weight, express)
    print("Вартість доставки:", total)