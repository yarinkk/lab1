def categorize_expenses(records):
    result = {}
    total = 0

    for record in records:
        category = record.get("category")
        amount = record.get("amount", 0)

        if category in result:
            result[category] += amount
        else:
            result[category] = amount

        total += amount

    result["total"] = total
    return result


def main():
    records = [
        {"category": "food", "amount": 200},
        {"category": "transport", "amount": 50},
        {"category": "food", "amount": 150},
    ]

    print(categorize_expenses(records))


if __name__ == "__main__":
    main()
