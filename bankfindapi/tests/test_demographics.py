from bankfindapi.demographics import get_demographics
import pandas as pd


def test_get_demographics():
    assert isinstance(get_demographics(), pd.DataFrame)
    df = get_demographics(filters="CERT:14 AND REPDTE:20230630")
    assert isinstance(df, pd.DataFrame)