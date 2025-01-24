FROM python:3.13

# установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# настройка прав
RUN useradd -m user
USER user
WORKDIR /home/user

# копирование самого проекта
COPY . .

# CMD [ "python", "-u", "main.py" ]
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]
