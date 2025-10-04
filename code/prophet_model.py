import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("Superstore.csv", encoding="latin-1")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

monthly_sales = df.groupby(pd.Grouper(key="Order Date", freq="M"))["Sales"].sum().reset_index()
prophet_df = monthly_sales.rename(columns={"Order Date": "ds", "Sales": "y"})

model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
model.fit(prophet_df)

future = model.make_future_dataframe(periods=12, freq="M")
forecast = model.predict(future)

merged = prophet_df.merge(forecast[["ds", "yhat"]], on="ds", how="left")

mae = mean_absolute_error(merged["y"], merged["yhat"])
rmse = np.sqrt(mean_squared_error(merged["y"], merged["yhat"]))
mape = np.mean(np.abs((merged["y"] - merged["yhat"]) / merged["y"].replace(0, np.nan))) * 100
smape = 100/len(merged) * np.sum(2 * np.abs(merged["yhat"] - merged["y"]) / 
                                 (np.abs(merged["y"]) + np.abs(merged["yhat"])))

print("Monthly Model Accuracy Metrics:")
print(f"MAE   : {mae:.2f}")
print(f"RMSE  : {rmse:.2f}")
print(f"MAPE  : {mape:.2f}%")
print(f"sMAPE : {smape:.2f}%")

forecast_clean = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
forecast_clean["yhat"] = forecast_clean["yhat"].clip(lower=0)

forecast_clean.to_csv("forecast_results.csv", index=False)
print("Clean monthly forecast exported to forecast_results.csv")

plt.figure(figsize=(12,6))
plt.plot(prophet_df["ds"], prophet_df["y"], label="Actual", color="black")
plt.plot(forecast["ds"], forecast["yhat"], label="Forecast", color="blue")
plt.fill_between(forecast["ds"], forecast["yhat_lower"], forecast["yhat_upper"],
                 color="lightblue", alpha=0.5, label="Confidence Interval")
plt.title("Monthly Sales Forecast with Prophet")
plt.legend()
plt.show()