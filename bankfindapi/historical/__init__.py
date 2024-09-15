from bankfindapi import __get_data

__all__ = ["get_summary"]

def get_summary(filters: str = None, **kwargs):
    return __get_data("summary", filters, search = None, **kwargs)
