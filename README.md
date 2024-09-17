# fdicapi

This repository contains A Python wrapper to easily retrieve data from the BankFind Suite official API from FDIC in pandas format.

## Overview
FDIC’s application programming interface (API) lets developers access FDIC’s publically available bank data. 
There are eight endpoints that the FDIC has exposed to the public:

- **institutions**: Returns a list of financial institutions.
- **locations**: Returns locations/branches of financial institutions.
- **history**: Returns details on structure change events
- **financials**: Returns financial information for financial institutions
- **summary**: Returns aggregate financial and structure data, subtotaled by year, regarding finanical institutions.
- **failures**: Returns details on failed financial institutions.
- **sod**: Returns summary of deposits information for institutions
- **demographics**: Returns summary of demographic information

## Requirements
- Python 3.9 or higher.
- Requests
- Pandas

## Installation
```terminal
pip install fdicapi
```

## Endpoints
### get_institutions
Get Financial Institutions.

```python
from fdicapi.structure import get_institutions
df = get_institutions(**kwargs)
```

#### Keyword Arguments
| Parameter    | Type  | Description                                                                                                                                                                             |
|--------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `filters`    | `str` | The filter for the bank search.                                                                                                                                                         |
| `search`     | `str` | Flexible text search against institution records - currently only supporting name search. Search supports text search and fuzzy matching, as opposed to filters that are exact matches. |
| `fields`     | `str` | Comma delimited list of fields to search.                                                                                                                                               |
| `sort_by`    | `str` | Field name by which to sort returned data.                                                                                                                                              |
| `sort_order` | `str` | Indicator if ascending (ASC) or descending (DESC).                                                                                                                                      |
| `limit`      | `int` | The number of records to return. Default is 10 and maximum is 10,000.                                                                                                                   |
| `offset`     | `int` | The offset of page to return.                                                                                                                                                           |

#### Returns
- `pd.DataFrame`: Return a pandas DataFrame of financial institutions.

### get_locations
Get Institution Locations.

```python
from fdicapi.structure import get_locations
df = get_locations(**kwargs)
```

#### Keyword Arguments
| Parameter    | Type  | Description                                                           |
|--------------|-------|-----------------------------------------------------------------------|
| `filters`    | `str` | The filter for the location search.                                   |
| `fields`     | `str` | Comma delimited list of fields to search.                             |
| `sort_by`    | `str` | Field name by which to sort returned data.                            |
| `sort_order` | `str` | Indicator if ascending (ASC) or descending (DESC).                    |
| `limit`      | `int` | The number of records to return. Default is 10 and maximum is 10,000. |
| `offset`     | `int` | The offset of page to return.                                         |

#### Returns
- `pd.DataFrame`: Returns locations/branches of financial institutions.


### get_history
Get Detail on Structure Change Events.

```python
from fdicapi.history import get_history
df = get_history(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                                                                                                    |
|-------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                                                                                         |
| `search`          | `str` | Flexible text search against institution records Search supports text search and fuzzy matching, as opposed to filters that are exact matches. |
| `fields`          | `str` | Comma delimited list of fields to search.                                                                                                      |
| `sort_by`         | `str` | Field name by which to sort returned data.                                                                                                     |
| `sort_order`      | `str` | Indicator if ascending (ASC) or descending (DESC).                                                                                             |
| `limit`           | `int` | The number of records to return. Default is 10 and maximum is 10,000.                                                                          |
| `offset`          | `int` | The offset of page to return.                                                                                                                  |
| `agg_by`          | `str` | The field by which data will be aggregated.                                                                                                    |
| `agg_term_fields` | `str` | The field(s) for which aggregations will be counted for each unique term.                                                                      |
| `agg_limit`       | `int` | The limit on how many aggregated results will be displayed.                                                                                    |

#### Returns
- `pd.DataFrame`: Return a pandas DataFrame of financial institutions.


### get_financials
Get Financial Information for FDIC Insured Institutions

```python
from fdicapi.financials import get_financials
df = get_financials(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                               |
|-------------------|-------|---------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                    |
| `fields`          | `str` | Comma delimited list of fields with quarterly financial data to return.   |
| `sort_by`         | `str` | Field name by which to sort returned data.                                |
| `sort_order`      | `str` | Indicator if ascending (ASC) or descending (DESC).                        |
| `limit`           | `int` | The number of records to return. Default is 10 and maximum is 10,000.     |
| `offset`          | `int` | The offset of page to return.                                             |
| `agg_by`          | `str` | The field by which data will be aggregated.                               |
| `agg_term_fields` | `str` | The field(s) for which aggregations will be counted for each unique term. |
| `agg_sum_fields`  | `str` | The field(s) for which aggregations will be summed or aggregated.         |
| `agg_limit`       | `int` | The limit on how many aggregated results will be displayed.               |

#### Returns
- `pd.DataFrame`: Returns financial information for financial institutions,


### get_summary
Get Historical Aggregate Data by Year.

```python
from fdicapi.historical import get_summary
df = get_summary(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                                                      |
|-------------------|-------|--------------------------------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                                           |
| `fields`          | `str` | Comma delimited list of fields with quarterly financial data to return.                          |
| `sort_by`         | `str` | Field name by which to sort returned data.                                                       |
| `sort_order`      | `str` | Indicator if ascending (ASC) or descending (DESC).                                               |
| `limit`           | `int` | The number of records to return. Default is 10 and maximum is 10,000.                            |
| `offset`          | `int` | The offset of page to return.                                                                    |
| `agg_by`          | `str` | The field by which data will be aggregated.                                                      |
| `agg_term_fields` | `str` | The field(s) for which aggregations will be counted for each unique term.                        |
| `agg_sum_fields`  | `str` | The field(s) for which aggregations will be summed or aggregated.                                |
| `agg_limit`       | `int` | The limit on how many aggregated results will be displayed.                                      |
| `max_value`       | `int` | The field by which the max value is desired.                                                     |
| `max_value_by`    | `int` | The field that will be used to determine unique records, similar to a primary key (i.e. CERT, ). |

#### Returns
- `pd.DataFrame`: Returns aggregate financial and structure data, subtotaled by year, regarding finanical institutions.


### get_failures
Get detail on historical bank failures from 1934 to present.

```python
from fdicapi.failures import get_failures
df = get_failures(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                                                                     |
|-------------------|-------|-----------------------------------------------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                                                          |
| `fields`          | `str` | Comma delimited list of fields with quarterly financial data to return.                                         |
| `sort_by`         | `str` | Field name by which to sort returned data.                                                                      |
| `sort_order`      | `str` | Indicator if ascending (ASC) or descending (DESC).                                                              |
| `limit`           | `int` | The number of records to return. Default is 10 and maximum is 10,000.                                           |
| `offset`          | `int` | The offset of page to return.                                                                                   |
| `total_fields`    | `str` | Fields to sum up (in a totals response object). Only numeric columns are valid.                                 |
| `subtotal_fields` | `str` | The field by which data will be subtotaled (in totals response object). Only categorical values should be used. |
| `agg_by`          | `str` | The field by which data will be aggregated.                                                                     |
| `agg_term_fields` | `str` | The field(s) for which aggregations will be counted for each unique term.                                       |
| `agg_sum_fields`  | `str` | The field(s) for which aggregations will be summed or aggregated.                                               |
| `agg_limit`       | `int` | The limit on how many aggregated results will be displayed.                                                     |

#### Returns
- `pd.DataFrame`: Returns details on failed financial institutions.


### get_sod
Get Summary of Deposits Information for FDIC Insured Institutions.

```python
from fdicapi.sod import get_sod
df = get_sod(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                                                                     |
|-------------------|-------|-----------------------------------------------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                                                          |
| `fields`          | `str` | Comma delimited list of fields with quarterly financial data to return.                                         |
| `sort_by`         | `str` | Field name by which to sort returned data.                                                                      |
| `sort_order`      | `str` | Indicator if ascending (ASC) or descending (DESC).                                                              |
| `limit`           | `int` | The number of records to return. Default is 10 and maximum is 10,000.                                           |
| `offset`          | `int` | The offset of page to return.                                                                                   |
| `agg_by`          | `str` | The field by which data will be aggregated.                                                                     |
| `agg_term_fields` | `str` | The field(s) for which aggregations will be counted for each unique term.                                       |
| `agg_sum_fields`  | `str` | The field(s) for which aggregations will be summed or aggregated.                                               |
| `agg_limit`       | `int` | The limit on how many aggregated results will be displayed.                                                     |

#### Returns
- `pd.DataFrame`: Returns summary of deposits information for institutions.


### get_demographics
Get Summary of Demographic Information.

```python
from fdicapi.demographics import get_demographics
df = get_demographics(**kwargs)
```

#### Keyword Arguments
| Parameter         | Type  | Description                                                                                                     |
|-------------------|-------|-----------------------------------------------------------------------------------------------------------------|
| `filters`         | `str` | The filter criteria that refines the records returned.                                                          |

#### Returns
- `pd.DataFrame`: Returns summary of demographic information.

## API Documentation
- [BankFind Suite: API for Data Miners & Developers (FDIC)](https://banks.data.fdic.gov/docs/)