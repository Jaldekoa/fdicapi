from bankfindapi.demographics import get_demographics
import pandas as pd


def test_get_demographics():
    assert isinstance(get_demographics(), pd.DataFrame)