from fdicapi import __get_data
import pandas as pd

__all__ = ["get_failures"]


def get_failures(**kwargs) -> pd.DataFrame:
    """
    Get detail on historical bank failures from 1934 to present.

    Keyword Args:
        filters (str): The filter criteria that refines the records returned. **None by default**.
        fields (str): Comma delimited list of fields of failed financial institutions to return.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.
        total_fields (str): Fields to sum up (in a totals response object). Only numeric columns are valid.
        subtotal_by (str): The field by which data will be subtotaled (in totals response object). Only categorical values should be used.
        agg_by (str): The field by which data will be aggregated.
        agg_term_fields (str): The field(s) for which aggregations will be counted for each unique term.
        agg_sum_fields (str): The field(s) for which aggregations will be summed or aggregated.
        agg_limit (int): The limit on how many aggregated results will be displayed.

    Returns:
        pd.DataFrame: Returns details on failed financial institutions.
    """
    return __get_data("failures", **kwargs)
