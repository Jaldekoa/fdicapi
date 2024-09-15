from bankfindapi.structure import get_institutions, get_locations
import pandas as pd


def test_get_institutions():
    assert isinstance(get_institutions(), pd.DataFrame)


def test_get_locations():
    assert isinstance(get_locations(), pd.DataFrame)
