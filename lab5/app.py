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


def add_express_fee(cost, express):
    """
    Додає плату за терміновість

    >>> add_express_fee(100, True)
    150
    >>> add_express_fee(100, False)
    100
    """
    if express:
        return cost + 50
    return cost


def calculate_total_cost(weight, express=False):
    """
    Загальна вартість доставки

    >>> calculate_total_cost(2, True)
    90
    >>> calculate_total_cost(3, False)
    60
    """
    base = calculate_weight_cost(weight)
    total = add_express_fee(base, express)
    return total