from fdicapi import __get_data
import pandas as pd

__all__ = ["get_institutions", "get_locations"]


def get_institutions(**kwargs) -> pd.DataFrame:
    """
    Get Financial Institutions

    Keyword Args:
        filters (str): The filter for the bank search.
        search (str): Flexible text search against institution records - currently only supporting name search. Search supports text search and fuzzy matching, as opposed to filters that are exact matches.
        fields (str): Comma delimited list of fields to search.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.

    Returns:
        pd.DataFrame: Return a pandas DataFrame of financial institutions.
    """
    return __get_data("institutions", **kwargs)


def get_locations(**kwargs) -> pd.DataFrame:
    """
    Get Institution Locations.

    Keyword Args:
        filters (str): The filter for the location search.
        fields (str): Comma delimited list of fields to return.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.

    Returns:
        pd.DataFrame: Returns locations/branches of financial institutions.
    """
    return __get_data("locations", **kwargs)
