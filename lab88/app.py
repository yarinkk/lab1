import logging

# налаштування логування
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# список доступних курсів
courses = ["Python", "Java", "C++", "Web"]

def register_user(user_id, course_name):
    logging.info(f"User {user_id} tries to register for {course_name}")

    if course_name not in courses:
        logging.error(f"Course '{course_name}' not found for user {user_id}")
        print(" Помилка: такого курсу не існує")
        return

    logging.info(f"User {user_id} successfully registered for {course_name}")
    print("Реєстрація успішна!")

# --- запуск програми ---
user_id = input("Введіть ваш ID: ")
course_name = input("Введіть назву курсу: ")

register_user(user_id, course_name)