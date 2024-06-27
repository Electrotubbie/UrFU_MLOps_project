# UrFU_MLOps_project
Project on the UrFU MLOps course

# Команда
- Сорокин Андрей Дмитриевич (РИМ-130907)
- Земов Василий Александрович (РИМ-130908)

# Описание
Приложение предназначено для оценки стоимости бриллианта.

Для оценки достаточно знать его вес в каратах, диаметр в миллиметрах, цвет, а также степень прозрачности.

# Модель
Для работы модели был выбран алгоритм DecisionTreeRegressor.

Процесс подготовки датасета можно рассмотреть в [preprocessing.ipynb](./preparation/preprocessing.ipynb) 

Процесс обучения можно рассмотреть в [model_prepare.ipynb](./preparation/model_prepare.ipynb) 

# Apps
## Streamlit web-app
Для развёртывания веб-приложения streamlit локально воспользуйтесь командой
```bash
streamlit run apps/web.py
```

## API
Для развёртывания api локально воспользуйтесь командой
```bash
uvicorn apps/api:app
```
