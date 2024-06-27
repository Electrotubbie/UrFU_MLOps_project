from preparation.pipe import model
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pandas as pd


app = FastAPI()


class Diamond(BaseModel):
    carat: float
    diametr: float
    color: Literal['D', 'E', 'F', 'G', 'H', 'I', 'J']
    clarity: Literal['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']


@app.get("/")
async def root():
    return {'message':
        "Оценка стоимости бриллианта по его параметрам:"
        "carat: вес в каратах, "
        "diametr: диаметр, "
        "color: цвет, одна из категорий "
        "['D', 'E', 'F', 'G', 'H', 'I', 'J'], "
        "clarity: прозрачность, "
        "одна из категорий ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']"
        }


@app.post('/predict_price/')
async def predict_price(diamond: Diamond):
    params = pd.DataFrame({'carat':[diamond.carat], 
                           'y':[diamond.diametr], 
                           'color':[diamond.color], 
                           'clarity':[diamond.clarity]})
    result = model.predict(params)
    return {'price': result[0]}
