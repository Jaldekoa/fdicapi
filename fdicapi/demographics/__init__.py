from fdicapi import __get_data
import pandas as pd

__all__ = ["get_demographics"]


def get_demographics(**kwargs) -> pd.DataFrame:
    """
    Get Summary of Demographic Information.

    Keyword Args:
        filters (str): The filter criteria that refines the records included in the result. **None by default**.

    Returns:
        pd.DataFrame: Returns summary of demographic information.
    """
    return __get_data("demographics", **kwargs)
