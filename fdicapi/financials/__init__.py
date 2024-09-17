from fdicapi import __get_data
import pandas as pd

__all__ = ["get_financials"]


def get_financials(**kwargs) -> pd.DataFrame:
    """
    Get Financial Information for FDIC Insured Institutions.

    Keyword Args:
        filters (str): The filter criteria that refines the records returned. **None by default**.
        fields (str): Comma delimited list of fields with quarterly financial data to return.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000. However, if the fields request is for more than 250 fields (variables), the maximum limit is 500 to ensure the request is successful.
        offset (int): The offset of page to return.
        agg_by (str): The field by which data will be aggregated.
        agg_term_fields (str): The field(s) for which aggregations will be counted for each unique term.
        agg_sum_fields (str): The field(s) for which aggregations will be summed or aggregated.
        agg_limit (int): The limit on how many aggregated results will be displayed.

    Returns:
        pd.DataFrame: Returns financial information for financial institutions,
    """
    return __get_data("financials", **kwargs)
