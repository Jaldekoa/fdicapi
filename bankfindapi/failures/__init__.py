from bankfindapi import __get_data

__all__ = ["get_failures"]

def get_failures(filters: str = None, **kwargs):
    return __get_data("failures", filters, search = None, **kwargs)
