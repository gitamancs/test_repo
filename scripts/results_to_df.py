import pandas as pd

def result_to_df(forecast_model_df, sales_data):
   
    forecast_model_df = forecast_model_df.set_index('Model').astype(int).reset_index()

    # Merging the DataFrames
    df = forecast_model_df.merge(
        sales_data[['Make_new', 'Model_new']],
        left_on='Model',
        right_on='Model_new',
        how='left'
    ).drop_duplicates().drop('Model_new', axis=1).reset_index(drop=True)

    # Reorder columns
    new_column_order = ['Make_new', 'Model'] + [col for col in df.columns if col not in ['Make_new', 'Model']]
    df = df[new_column_order].reset_index(drop=True)

    df.loc[df['Model'] == 'Other', 'Make_new'] = 'Other' 

    df.drop_duplicates(inplace=True)
    df.dropna(inplace = True)
    df = df.reset_index(drop=True)
    df.iloc[17,0] = 'Other'
    df.drop_duplicates(inplace=True)

    # Display the result
    df.head(10)
    return df
    