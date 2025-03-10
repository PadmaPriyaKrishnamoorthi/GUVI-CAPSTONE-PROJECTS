# streamlit_app/app.py
import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# App Title
st.title("🍕 Dominos - Predictive Purchase Order System")
st.markdown("Forecast pizza sales and generate ingredient purchase orders.")

# Load data
sales_df = pd.read_csv(r"C:\Users\Vishwa\Desktop\GUVI captone\Dominos\Pizza_Sale - pizza_sales.csv")
ingredients_df = pd.read_csv(r"C:\Users\Vishwa\Desktop\GUVI captone\Dominos\Pizza_ingredients - Pizza_ingredients.csv")

# Preprocess
daily_sales = sales_df.copy()
daily_sales['order_date'] = pd.to_datetime(daily_sales['order_date'], errors='coerce', dayfirst=True)
daily_sales = daily_sales.groupby('order_date')['quantity'].sum().reset_index()
daily_sales.columns = ['ds', 'y']

# Select forecasting model
model_choice = st.selectbox("Choose Forecasting Model", ["Prophet", "SARIMA"])

# Train/Test Split
train = daily_sales[:-7]
test = daily_sales[-7:]

# Forecasting
if model_choice == "Prophet":
    model = Prophet()
    model.fit(train)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    forecast_data = forecast[['ds', 'yhat']].tail(7)
    avg_pred = forecast_data['yhat'].mean()
    st.subheader("📈 Prophet Forecast - Next 7 Days")
    fig = model.plot(forecast)
    st.pyplot(fig)
else:
    train_sarima = train.set_index('ds')['y']
    sarima_model = SARIMAX(train_sarima, order=(1,1,1), seasonal_order=(1,1,1,7))
    sarima_result = sarima_model.fit()
    sarima_forecast = sarima_result.forecast(steps=7)
    avg_pred = sarima_forecast.mean()
    forecast_data = pd.DataFrame({"ds": pd.date_range(start=train['ds'].iloc[-1]+pd.Timedelta(days=1), periods=7), "yhat": sarima_forecast.values})
    st.subheader("📈 SARIMA Forecast - Next 7 Days")
    st.line_chart(forecast_data.set_index('ds'))

# Purchase Order Generation
st.subheader("📦 Ingredient Purchase Order")
pizza_ratios = sales_df.groupby('pizza_name_id')['quantity'].sum() / sales_df['quantity'].sum()
pizza_forecast = (pizza_ratios * avg_pred * 7).reset_index()
pizza_forecast.columns = ['pizza_name_id', 'forecasted_quantity']
purchase_order = pd.merge(pizza_forecast, ingredients_df, on='pizza_name_id', how='left')
purchase_order['total_ingredient_qty'] = purchase_order['forecasted_quantity'] * purchase_order['Items_Qty_In_Grams']
ingredient_summary = purchase_order.groupby('pizza_ingredients')['total_ingredient_qty'].sum().reset_index()
ingredient_summary.columns = ['Ingredient', 'Total_Required_Grams']
ingredient_summary = ingredient_summary.sort_values(by='Total_Required_Grams', ascending=False)

st.dataframe(ingredient_summary)
st.download_button("📥 Download Purchase Order CSV", data=ingredient_summary.to_csv(index=False), file_name="purchase_order.csv")
