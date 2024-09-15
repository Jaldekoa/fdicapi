from bankfindapi.financials import get_financials
import pandas as pd


def test_get_financials():
    assert isinstance(get_financials(), pd.DataFrame)