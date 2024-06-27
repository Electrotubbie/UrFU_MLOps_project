from fastapi.testclient import TestClient
from ..apps.api import app
from ..preparation.pipe import model


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message':
"Оценка стоимости бриллианта по его параметрам:"
"carat: вес в каратах, "
"diametr: диаметр, "
"color: цвет, одна из категорий "
"['D', 'E', 'F', 'G', 'H', 'I', 'J'], "
"clarity: прозрачность, "
"одна из категорий ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']"
}


def test_predict_price():
    params = {"carat": 0.72, "diametr": 5.76, "color": "D", "clarity": "SI1"}
    response = client.post("/predict_price/", json=params)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data == {"price": 2826.921875}