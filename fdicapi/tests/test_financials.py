from fdicapi.financials import get_financials
import pandas as pd


def test_get_financials():
    assert isinstance(get_financials(), pd.DataFrame)
    df = get_financials(filters="CERT:14",
                        fields="CERT,REPDTE,ASSET,DEP",
                        sort_by="REPDTE",
                        sort_order="DESC",
                        limit=10,
                        offset=0,
                        agg_by="CERT",
                        agg_term_fields="REPDTE",
                        agg_sum_fields="ASSET",
                        agg_limit=1)
    assert isinstance(df, pd.DataFrame)