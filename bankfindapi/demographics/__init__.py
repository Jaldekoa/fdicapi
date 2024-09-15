from bankfindapi import __get_data

__all__ = ["get_demographics"]

def get_demographics(filters: str = None, **kwargs):
    return __get_data("demographics", filters, search = None, **kwargs)
