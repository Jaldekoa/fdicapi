from fdicapi import __get_data
import pandas as pd

__all__ = ["get_history"]


def get_history(**kwargs) -> pd.DataFrame:
    """
    Get Detail on Structure Change Events.

    Keyword Args:
        filters (str): The filter criteria that refines the records returned. **None by default**.
        search (str): Flexible text search against institution records Search supports text search and fuzzy matching, as opposed to filters that are exact matches. **None by default**.
        fields (str): Comma delimited list of fields to search.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.
        agg_by (str): The field by which data will be aggregated.
        agg_term_fields (str): The field(s) for which aggregations will be counted for each unique term.
        agg_limit (int): The limit on how many aggregated results will be displayed.

    Returns:
        pd.DataFrame: Returns details on structure change events.
    """
    return __get_data("history", **kwargs)
