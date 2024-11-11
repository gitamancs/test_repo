import pandas as pd

from upload_load_db import load_data_sql, upload_data_sql
from data_cleaning import Cleanig_Data
from final_model import Models
from results_to_df import result_to_df

#DataBase name and sheet name
database_name = 'car_sales_forecast'
sheet_name = 'sales data - from view'

#load The data From MySQL
df = load_data_sql(database_name, sheet_name)


#Clean The Data 
clean_ob = Cleanig_Data()
clean_data = clean_ob.sales_data_cleaning(df)

#Create a model for forecasting
model_obj = Models()
results = model_obj.final_model(clean_data)

main_result = result_to_df(results, clean_data)

print(main_result.head())

retn = upload_data_sql(main_result, 'vehi_models_model', 'clean_data_car')

if retn:
    print('Data is upload successfully in database')
else :
    print('data is not upload successfuly')







