from bankfindapi.failures import get_failures
import pandas as pd


def test_get_failures():
    assert isinstance(get_failures(), pd.DataFrame)
    df = get_failures(filters='FAILYR:["2014" TO "2015"]',
                      fields="NAME,CERT,FIN,CITYST,FAILDATE,SAVR,RESTYPE,RESTYPE1,QBFDEP,QBFASSET,COST",
                      sort_by="FAILDATE",
                      sort_order="DESC",
                      limit=10,
                      offset=0,
                      total_fields="QBFDEP,QBFASSET,COST",
                      agg_by="FAILYR",
                      agg_term_fields="RESTYPE",
                      agg_sum_fields="QBFASSET,QBFDEP,COST",
                      agg_limit=10)
    assert isinstance(df, pd.DataFrame)