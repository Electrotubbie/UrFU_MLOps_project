import pandas as pd
import pytest
import joblib
from sklearn.metrics import mean_absolute_error, r2_score


@pytest.fixture()
def load_model():
    model = joblib.load('./model/pipeline.joblib')
    return model


@pytest.fixture()
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


@pytest.fixture()
def make_prediction(load_model, load_dataset):
    X = load_dataset.drop(columns='price')
    y = load_dataset['price']
    y_pred = load_model.predict(X)
    return y, y_pred


def test_MAE(make_prediction):
    y, y_pred = make_prediction
    assert mean_absolute_error(y, y_pred) < 500


def test_R2(make_prediction):
    y, y_pred = make_prediction
    assert r2_score(y, y_pred) > 0.95