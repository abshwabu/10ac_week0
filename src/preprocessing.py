import pandas as pd

def merge_datasets(data_df, domain_location_df):
    """Merge datasets based on common keys."""
    # Assuming 'source_name' in `data_df` corresponds to 'SourceCommonName' in `domain_location_df`
    merged_df = data_df.merge(domain_location_df, left_on='source_name', right_on='SourceCommonName', how='left')
    return merged_df
