# Calculator

Учебный проект по четырём заданиям: виртуальное окружение, NumPy, Git,
оформление кода, тестирование и исправление деления на ноль.

## Установка и запуск (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m unittest -v
.\.venv\Scripts\python.exe -m black --check .
.\.venv\Scripts\python.exe -m pycodestyle calculator.py main.py test_calculator.py
```

## Файлы

- `calculator.py` — сложение и деление с аннотациями типов и docstring.
- `main.py` — тестовый запуск NumPy и функций калькулятора.
- `test_calculator.py` — тесты сложения, деления и нулевого делителя.
- `requirements.txt` — зависимость NumPy.
- `requirements-dev.txt` — дополнительные инструменты проверки оформления.

## Открытие в PyCharm

Откройте эту папку через File → Open. В качестве интерпретатора выберите
`.venv\Scripts\python.exe`. Запускайте `main.py` или тесты
`test_calculator.py` через меню Run.

## Задание 4: деление на ноль и отладка

Исходная функция `return a / b` при `b = 0` вызывала `ZeroDivisionError`.
Исправление: перед делением проверяется `b == 0`, после чего возникает
`ValueError` с понятным сообщением. Вызывающий код в `main.py` перехватывает
это исключение, поэтому демонстрационный скрипт завершается нормально.

Чтобы проверить исправление в отладчике PyCharm:

1. Поставьте точку останова на строке `if b == 0` в `calculator.py`.
2. Запустите `main.py` через Debug.
3. При первом вызове проверьте значения `a = 10`, `b = 2` и результат `5.0`.
4. Продолжите выполнение до вызова с `a = 10`, `b = 0`.
5. Выполните шаг: сработает проверка и `raise ValueError`, а затем обработчик
   в `main.py`. До операции `a / b` выполнение при нулевом делителе не дойдёт.

Виртуальное окружение и локальные настройки PyCharm исключены из Git.
