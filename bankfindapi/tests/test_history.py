from bankfindapi.history import get_history
import pandas as pd


def test_get_history():
    assert isinstance(get_history(), pd.DataFrame)
    df = get_history(filters="STATE:VIRGINIA",
                     #search="NAME:Island",
                     fields="INSTNAME,CERT,PCITY,PSTALP,PZIP5",
                     sort_by="PROCDATE",
                     sort_order="DESC",
                     limit=10,
                     offset=0,
                     #agg_by="",
                     #agg_term_fields="",
                     agg_limit=10)
    assert isinstance(df, pd.DataFrame)