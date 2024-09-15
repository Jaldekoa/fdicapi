from bankfindapi import __get_data

__all__ = ["get_institutions", "get_locations"]

def get_institutions(filters: str = None, search: str = None, **kwargs):
    return __get_data("institutions", filters, search, **kwargs)

def get_locations(filters: str = None, **kwargs):
    return __get_data("locations", filters, search = None, **kwargs)