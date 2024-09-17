from fdicapi.structure import get_institutions, get_locations
import pandas as pd


def test_get_institutions():
    assert isinstance(get_institutions(), pd.DataFrame)
    df = get_institutions(filters="STALP:IA AND ACTIVE:1",
                          #search="NAME:Island",
                          fields="ZIP,OFFDOM,CITY,COUNTY,STNAME,STALP,NAME,ACTIVE,CERT,CBSA,ASSET,NETINC,DEP,DEPDOM,"
                                 "ROE,ROA,DATEUPDT,OFFICES",
                          sort_by="OFFICES",
                          sort_order="DESC",
                          limit=10,
                          offset=0)
    assert isinstance(df, pd.DataFrame)


def test_get_locations():
    assert isinstance(get_locations(), pd.DataFrame)
    df = get_institutions(filters="STALP:IA AND ACTIVE:1",
                          fields="NAME,UNINUM,SERVTYPE,RUNDATE,CITY,STNAME,ZIP,COUNTY",
                          sort_by="NAME",
                          sort_order="DESC",
                          limit=10,
                          offset=0)
    assert isinstance(df, pd.DataFrame)
