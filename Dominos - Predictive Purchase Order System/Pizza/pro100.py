import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="Dominos Sales Forecast & Purchase Order", layout="wide")
st.title("🍕 Dominos - Predictive Purchase Order System")

# File Upload Section
sales_file = st.file_uploader("Upload Pizza Sales CSV", type=["csv"])
ingredients_file = st.file_uploader("Upload Pizza Ingredients CSV", type=["csv"])

if sales_file and ingredients_file:
    sales_df = pd.read_csv(sales_file)
    ingredients_df = pd.read_csv(ingredients_file)

    # Clean Columns
    sales_df.columns = sales_df.columns.str.strip().str.lower()
    ingredients_df.columns = ingredients_df.columns.str.strip().str.lower()

    # Date Conversion
    sales_df['order_date'] = pd.to_datetime(sales_df['order_date'], format="%d-%m-%Y", errors='coerce')

    # Prepare Data
    daily_sales_df = sales_df.groupby('order_date')['quantity'].sum().reset_index()
    daily_sales_df.columns = ['ds', 'y']

    all_dates = pd.date_range(start=daily_sales_df['ds'].min(), end=daily_sales_df['ds'].max())
    daily_sales_df = daily_sales_df.set_index('ds').reindex(all_dates).fillna(0).rename_axis('ds').reset_index()

    train_df = daily_sales_df[:-7]
    test_df = daily_sales_df[-7:]

    mape_list = []
    forecast_list = []

    with st.spinner("Training Prophet model 100 times..."):
        for _ in range(100):
            model = Prophet()
            model.fit(train_df)
            future = model.make_future_dataframe(periods=7)
            forecast = model.predict(future)
            forecast_list.append(forecast['yhat'][-7:].values)
            mape = np.mean(np.abs((test_df['y'].values - forecast['yhat'][-7:].values) / np.maximum(test_df['y'].values, 1))) * 100
            mape_list.append(mape)

    avg_forecast = np.mean(forecast_list, axis=0)
    forecast_dates = pd.date_range(start=daily_sales_df['ds'].max() + pd.Timedelta(days=1), periods=7)
    forecast_df = pd.DataFrame({'date': forecast_dates, 'predicted_sales': avg_forecast.astype(int)})

    st.subheader("📈 7-Day Sales Forecast")
    st.dataframe(forecast_df)

    fig1, ax1 = plt.subplots(figsize=(10,5))
    ax1.plot(daily_sales_df['ds'], daily_sales_df['y'], label='Actual Sales', color='skyblue')
    ax1.plot(forecast_df['date'], forecast_df['predicted_sales'], label='Forecasted Sales', color='orange', marker='o')
    ax1.set_title('Actual Sales vs Forecasted Sales')
    ax1.legend()
    st.pyplot(fig1)

    # Pizza-level Forecast based on proportions
    pizza_sales = sales_df.groupby('pizza_name')['quantity'].sum()
    pizza_sales_pct = pizza_sales / pizza_sales.sum()

    pizza_forecast = pd.DataFrame({
        'pizza_name': pizza_sales_pct.index,
        'forecasted_quantity': (pizza_sales_pct * avg_forecast.sum()).astype(int)
    }).reset_index(drop=True)

    ingredients_df = ingredients_df.reset_index(drop=True)
    ingredient_forecast = pd.merge(pizza_forecast, ingredients_df, on='pizza_name', how='left')
    ingredient_forecast['total_ingredient_needed'] = ingredient_forecast['forecasted_quantity'] * ingredient_forecast['items_qty_in_grams']

    purchase_order = ingredient_forecast.groupby('pizza_ingredients')['total_ingredient_needed'].sum().reset_index()

    st.subheader("🧾 Purchase Order")
    st.dataframe(purchase_order)

    fig2, ax2 = plt.subplots(figsize=(12,6))
    sns.barplot(x='pizza_ingredients', y='total_ingredient_needed', data=purchase_order.sort_values(by='total_ingredient_needed', ascending=False), ax=ax2, palette='viridis')
    ax2.set_title('Total Ingredient Quantity Needed')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig2)

    # Download Buttons
    csv1 = forecast_df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Forecast CSV", csv1, "7_day_sales_forecast.csv", "text/csv")

    csv2 = purchase_order.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Purchase Order CSV", csv2, "purchase_order.csv", "text/csv")

else:
    st.info("📂 Please upload both sales and ingredients CSV files to begin.")
