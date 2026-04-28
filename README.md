# Аналіз витрат

## Запуск
python app.py

## Тести
python -m unittest test_app.py

## CI
Автоматично запускається при кожному коміті

## Git Hook
Створити файл .git/hooks/pre-commit:

#!/bin/sh
flake8 lab77/
