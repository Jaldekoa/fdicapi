from fdicapi import __get_data
import pandas as pd

__all__ = ["get_sod"]


def get_sod(**kwargs) -> pd.DataFrame:
    """
    Get Summary of Deposits Information for FDIC Insured Institutions.

    Keyword Args:
        filters (str): The filter criteria that refines the records included in the result. **None by default**.
        fields (str): Comma delimited list of fields with quarterly financial data to return.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.
        agg_by (str): The field by which data will be aggregated.
        agg_term_fields (str): The field(s) for which aggregations will be counted for each unique term.
        agg_sum_fields (str): The field(s) for which aggregations will be summed or aggregated.
        agg_limit (int): The limit on how many aggregated results will be displayed.

    Returns:
        pd.DataFrame: Returns summary of deposits information for institutions.
    """
    return __get_data("sod", **kwargs)
