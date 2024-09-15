from bankfindapi import __get_data

__all__ = ["get_sod"]

def get_sod(filters: str = None, **kwargs):
    return __get_data("sod", filters, search = None, **kwargs)
