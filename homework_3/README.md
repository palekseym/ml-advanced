# ДЗ 3
Нужно обучить модель, обернуть в веб сервис и собрать докер образ.

## Обучение модели
Обучил простинкую модель в ноутбуке `homework.ipynb`.

## Подготовка веб сервиса

Написал небольшое приложение на flask. Находится в папке `app`.

## Docker

Подгтовил докер файл `Dockerfile` для сборки образа.

Собрать можно выполнив:

```bash
docker build -t homework_3 .
```

Запустить:

```bash
docker run -d -p 8080:80 homework_3
```

Проверить результат:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"age":63.0,"sex":1.0,"cp":3.0,"trestbps":145.0,"chol":233.0,"fbs":1.0,"restecg":0.0,"thalach":150.0,"exang":0.0,"oldpeak":2.3,"slope":0.0,"ca":0.0,"thal":1.0}' http://localhost:8080/predict
```