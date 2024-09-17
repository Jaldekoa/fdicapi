from urllib.parse import urlencode
import pandas as pd

__all__ = ["demographics", "failures", "financials", "historical", "history", "structure", "sod"]
__valid_params = {
    "institutions": ["filters", "search", "fields", "sort_by", "sort_order", "limit", "offset"],
    "locations": ["filters", "fields", "sort_by", "sort_order", "limit", "offset"],
    "history": ["filters", "search", "fields", "sort_by", "sort_order", "limit", "offset", "agg_by", "agg_term_fields",
                "agg_limit"],
    "financials": ["filters", "fields", "sort_by", "sort_order", "limit", "offset", "agg_by", "agg_term_fields",
                   "agg_sum_fields", "agg_limit"],
    "summary": ["filters", "fields", "sort_by", "sort_order", "agg_by", "agg_term_fields", "agg_sum_fields",
                "agg_limit", "max_value", "max_value_by"],
    "failures": ["filters", "fields", "sort_by", "sort_order", "limit", "offset", "total_fields", "subtotal_by",
                 "agg_by", "agg_sum_fields", "agg_limit"],
    "sod": ["filters", "fields", "sort_by", "sort_order", "limit", "offset", "agg_by", "agg_term_fields",
            "agg_sum_fields", "agg_limit"],
    "demographics": ["filters"],
}


def __encode_params(endpoint: str, **kwargs) -> dict[str, str]:
    params = {k: v for k, v in kwargs.items() if k in __valid_params[endpoint]}
    params.update({"format": "csv", "download": "false"})
    return params


def __get_data(endpoint: str, **kwargs):
    params = __encode_params(endpoint, **kwargs)
    return pd.read_csv(f"https://banks.data.fdic.gov/api/{endpoint}?{urlencode(params)}")
