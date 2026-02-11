# Python частина лабораторної роботи 2

## Створення віртуального середовища

python -m venv venv
source venv/Scripts/activate

## Збереження залежностей

python -m pip freeze > requirements.txt

## Встановлення залежностей з файлу requirements.txt

pip install -r requirements.txt

## Перевірка вразливостей

pip-audit -r requirements.txt
