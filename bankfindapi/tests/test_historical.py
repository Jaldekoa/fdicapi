from bankfindapi.historical import get_summary
import pandas as pd


def test_get_summary():
    assert isinstance(get_summary(), pd.DataFrame)