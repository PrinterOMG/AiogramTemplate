FROM python:3.10-buster

WORKDIR app/

COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy

COPY . .

CMD ["python3", "bot.py"]
