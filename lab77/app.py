def categorize_expenses(records):
    """
    Аналізує витрати та повертає суму по категоріях і загальну суму.

    >>> categorize_expenses([
    ...     {"category": "food", "amount": 100},
    ...     {"category": "transport", "amount": 50},
    ...     {"category": "food", "amount": 150}
    ... ])
    {'food': 250, 'transport': 50, 'total': 300}
    """
    result = {}
    total = 0

    for record in records:
        category = record.get("category", "unknown")
        amount = record.get("amount", 0)

        result[category] = result.get(category, 0) + amount
        total += amount

    result["total"] = total
    return result


def main():
    records = [
        {"category": "food", "amount": 200},
        {"category": "transport", "amount": 50},
        {"category": "entertainment", "amount": 100},
        {"category": "food", "amount": 150},
    ]

    result = categorize_expenses(records)

    print("Звіт витрат:")

    translations = {
        "food": "Їжа",
        "transport": "Транспорт",
        "entertainment": "Розваги",
        "total": "Загальна сума",
        "unknown": "Інше"
    }

    for k, v in result.items():
        name = translations.get(k, k)
        print(f"{name}: {v} грн")


if __name__ == "__main__":
    main()
