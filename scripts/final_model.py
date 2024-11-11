import pandas as pd
from prophet import Prophet
import numpy as np

class Models():

    def final_model(self, sales_data):

        # Convert the date column to datetime format if not already
        sales_data['INVOICEDAT'] = pd.to_datetime(sales_data['INVOICEDAT'])

        # Forecasting settings
        forecast_period = 365  # Forecast for 365 days (approximately 3 months)
        monthly_forecasts = {}

        # Iterate over each unique model in the 'Model_new' column
        for model_name in sales_data['Model_new'].unique():
            # Filter and aggregate data for the current model to daily frequency
            model_data = sales_data[sales_data['Model_new'] == model_name]
            daily_data = model_data.groupby('INVOICEDAT').size().reset_index(name='y')
            daily_data = daily_data.rename(columns={'INVOICEDAT': 'ds'})

            # Check if there's enough data to fit the Prophet model
            if len(daily_data) < 2:
                print(f"Skipping '{model_name}' due to insufficient data.")
                continue

             # Initialize the Prophet model with additional parameters
            prophet_model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=False,
                daily_seasonality=False,
                seasonality_mode='multiplicative',
                changepoint_prior_scale=0.1,  # Adjust as necessary
                n_changepoints=30
            )
            
            # Add custom 6-month seasonality (biannual)
            prophet_model.add_seasonality(name='biannual', period=182.5, fourier_order=5)
            
            prophet_model.fit(daily_data)

            # Create future dates and generate forecast
            future_dates = prophet_model.make_future_dataframe(periods=forecast_period)
            forecast = prophet_model.predict(future_dates)

            # Filter forecast results to the next three months only
            forecast['month'] = forecast['ds'].dt.to_period('M')
            last_date = daily_data['ds'].max()
            forecast_next_twelve_months = forecast[forecast['ds'] > last_date].groupby('month')['yhat'].sum().head(12)

            # Store forecasted monthly results for the current model
            monthly_forecasts[model_name] = forecast_next_twelve_months.values

        forecast_model_df = pd.DataFrame.from_dict(
            monthly_forecasts, 
            orient='index', 
            columns=forecast_next_twelve_months.index[:12]  # Set columns to match the months
            ).astype(int).reset_index().rename(columns={'index': 'Model'})

        return forecast_model_df
