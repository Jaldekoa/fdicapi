from bankfindapi.historical import get_summary
import pandas as pd


def test_get_summary():
    assert isinstance(get_summary(), pd.DataFrame)
    df = get_summary(filters="STNAME:Alabama",
                    fields="STNAME,YEAR,INTINC,EINTEXP,NIM,NONII,NONIX,ELNATR,ITAXR,IGLSEC,ITAX,EXTRA,NETINC",
                    sort_by="YEAR",
                    sort_order="DESC",
                    limit=10,
                    offset=0,
                    #agg_by="",
                    #agg_term_fields="",
                    #agg_sum_fields="",
                    #agg_limit=1,
                    #max_value="",
                    #max_value_by=""
    )
    assert isinstance(df, pd.DataFrame)