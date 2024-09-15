from bankfindapi import __get_data

__all__ = ["get_history"]

def get_history(filters: str = None, search: str = None, **kwargs):
    return __get_data("history", filters, search, **kwargs)
