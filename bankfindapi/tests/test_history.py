from bankfindapi.history import get_history
import pandas as pd


def test_get_history():
    assert isinstance(get_history(), pd.DataFrame)