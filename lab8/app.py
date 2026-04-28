import sentry_sdk

sentry_sdk.init(
    dsn="https://d27258db425273c83ad2628bee2c90cd@o4511296908427264.ingest.de.sentry.io/4511296918257744"
)

def check_number(value):
    if value <= 0:
        raise ValueError("Число має бути більше 0")
    return value


def main():
    try:
        user_input = float(input("Введіть число: "))
        result = check_number(user_input)
        print(f"Все ок, ви ввели: {result}")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()