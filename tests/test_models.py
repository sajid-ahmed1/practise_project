from src.mean import MeanModel
from src.max import MaxModel

def test_mean_model():
    X = [1, 2, 3]
    y = [10, 20, 30]

    model = MeanModel()
    model.fit(X, y)
    preds = model.predict(X)

    # assert the mean is computed correctly
    assert preds == [20,20,20]

def test_max_model():
    X = [1, 2, 3]
    y = [10, 20, 30]

    model = MaxModel()
    model.fit(X, y)
    preds = model.predict(X)

    # assert max is correct
    assert preds == [30,30,30]
