# DOCX Modifier

Этот проект содержит скрипт для изменения всех файлов `.docx` в указанной директории. Скрипт изменяет шрифт, размер шрифта и межстрочный интервал для всех абзацев в документах.

## Возможности

- Изменение шрифта на Times New Roman
- Установка размера шрифта 14
- Установка межстрочного интервала 1.5

## Требования

- Python 3.x
- Библиотека `python-docx`

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/yourusername/docx-modifier.git
    cd docx-modifier
    ```

2. Установите необходимую библиотеку:

    ```sh
    pip install python-docx
    ```

## Использование

1. Поместите ваши `.docx` файлы в директорию.
2. Обновите переменную `directory` в `main.py`, указав путь к вашей директории:

    ```python
    directory = "path/to/your/docx/files"
    ```

3. Запустите скрипт:

    ```sh
    python main.py
    ```

## Структура файлов

- `main.py`: Основной скрипт, который обрабатывает все `.docx` файлы в указанной директории.
- `docx_modifier.py`: Содержит функции для изменения шрифта, размера шрифта и межстрочного интервала в документе `.docx`.

## Функции

### `docx_modifier.py`

- `change_font_and_size(document, font_name='Times New Roman', font_size=14)`: Изменяет шрифт и размер для всех абзацев в документе.
- `set_line_spacing(document, line_spacing=1.5)`: Устанавливает межстрочный интервал для всех абзацев в документе.
- `modify_docx(file_path, font_name='Times New Roman', font_size=14, line_spacing=1.5)`: Изменяет указанный файл `.docx` с заданным шрифтом, размером шрифта и межстрочным интервалом.

### `main.py`

- `process_all_files(directory, file_extension=".docx")`: Обрабатывает все файлы `.docx` в указанной директории.

## Пример

1. Поместите ваши `.docx` файлы в директорию, например, `./docs`.
2. Обновите `directory` в `main.py`:

    ```python
    directory = "./docs"
    ```

3. Запустите скрипт:

    ```sh
    python main.py
    ```

