from fdicapi import __get_data
import pandas as pd

__all__ = ["get_summary"]


def get_summary(**kwargs) -> pd.DataFrame:
    """
    Get Historical Aggregate Data by Year.

    Keyword Args:
        filters (str): The filter criteria that refines the records returned. **None by default**.
        fields (str): Comma delimited list of fields with aggregated annual financial data to return.
        sort_by (str): Field name by which to sort returned data.
        sort_order (str): Indicator if ascending (ASC) or descending (DESC).
        limit (int): The number of records to return. Default is 10 and maximum is 10,000.
        offset (int): The offset of page to return.
        agg_by (str): The field by which data will be aggregated.
        agg_term_fields (str): The field(s) for which aggregations will be counted for each unique term.
        agg_sum_fields (str): The field(s) for which aggregations will be summed or aggregated.
        agg_limit (int): The limit on how many aggregated results will be displayed.
        max_value (str): The field by which the max value is desired.
        max_value_by (str): The field that will be used to determine unique records, similar to a primary key (i.e. CERT, ).

    Returns:
        pd.DataFrame: Returns aggregate financial and structure data, subtotaled by year, regarding finanical institutions.
    """
    return __get_data("summary", **kwargs)
