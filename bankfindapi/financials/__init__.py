from bankfindapi import __get_data

__all__ = ["get_financials"]

def get_financials(filters: str = None, **kwargs):
    return __get_data("financials", filters, search = None, **kwargs)
