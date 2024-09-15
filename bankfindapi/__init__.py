from urllib.parse import urlencode
import pandas as pd

__all__ = ["demographics", "failures", "financials", "historical", "history", "structure", "summary_of_deposits"]


def __encode_params(filters: str = None, search: str = None, **kwargs):
    params = {
        "sort_by": kwargs.get("sort_by", None),
        "sort_order": kwargs.get("sort_order", None),
        "limit": kwargs.get("limit", None),
        "offset": kwargs.get("offset", None),
        "fields": kwargs.get("fields", None),
        "filters": filters,
        "search": search,
        "format": "csv",
        "download": "false"
    }
    return {k: v for k, v in params.items() if v is not None}


def __get_data(endpoint: str, filters: str = None, search: str = None, **kwargs):
    params = __encode_params(filters, search, **kwargs)
    return pd.read_csv(f"https://banks.data.fdic.gov/api/{endpoint}?{urlencode(params)}")
