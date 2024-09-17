from bankfindapi.sod import get_sod
import pandas as pd


def test_get_sod():
    assert isinstance(get_sod(), pd.DataFrame)
    df = get_sod(filters="CERT:14",
                      fields="CERT,YEAR,ASSET,DEPSUMBR,STALPBR",
                      sort_by="YEAR",
                      sort_order="DESC",
                      limit=10,
                      offset=0,
                      agg_by="CERT",
                      agg_term_fields="YEAR",
                      agg_sum_fields="ASSET",
                      agg_limit=1)
    assert isinstance(df, pd.DataFrame)