from bankfindapi.failures import get_failures
import pandas as pd


def test_get_failures():
    assert isinstance(get_failures(), pd.DataFrame)