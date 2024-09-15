from bankfindapi.summary_of_deposits import get_sod
import pandas as pd


def test_get_sod():
    assert isinstance(get_sod(), pd.DataFrame)