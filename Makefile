# Название интерпретатора и путь к виртуальному окружению
PYTHON = python
PIP = pip
UVICORN = uvicorn
POETRY = poetry

# Файлы и директории
SRC = blog
TESTS = tests

.PHONY: install run test lint format clean

# Установка зависимостей
install:
	$(PIP) install -r requirements.txt

# Запуск приложения
run:
	$(UVICORN) $(SRC).main:app --reload --app-dir src/

# Запуск тестов
test:
	pytest $(TESTS)

# Запуск линтеров
lint:
	flake8 $(SRC) $(TESTS)

# Форматирование кода
format:
	black $(SRC) $(TESTS)
	isort $(SRC) $(TESTS)

# Очистка временных и кеш файлов
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
