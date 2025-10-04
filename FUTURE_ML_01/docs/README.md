# FUTURE_ML_01 – AI-Powered Sales Forecasting Dashboard

## 📌 About the Task
This project is part of my *Future Interns Machine Learning Internship* (Task 1).  
The goal is to build an *AI-powered sales forecasting system* that predicts future sales trends using machine learning, and present the insights through an *interactive Power BI dashboard*.

---

## 🎯 Objectives
- Clean and structure historical retail sales data.
- Engineer features such as monthly sales and seasonal patterns.
- Train a *time series forecasting model* using *Facebook Prophet*.
- Build a Power BI dashboard for visualization.
- Provide clear *business insights* from the results.

---

## 🛠 Tools & Technologies
- *Python* (Pandas, Prophet, Matplotlib, Scikit-learn, NumPy)
- *Power BI Desktop*
- *Superstore Sales Dataset*
- *GitHub* for code hosting

---

## 📊 Key Features in Dashboard
✔ Sales trend line with *actual vs forecasted* data  
✔ *Monthly & yearly comparisons*  
✔ Filters by *Category* and *Region*  
✔ Highlighted *top-selling items* and low seasons  
✔ KPI cards for quick decision-making (Total Sales, Total Profit, Avg. Discount)

---

## 📂 Project Structure
```text
FUTURE_ML_01/
│
├── code/                 # Python forecasting scripts
│   ├── prophet_model.py
│   └── requirements.txt
│
├── data/                 # Datasets and forecast outputs
│   ├── Superstore.csv
│   └── forecast_results.csv
│
├── dashboard/            # Power BI files
│   ├── Task1_Dashboard.pbix
│   └── Dashboard_Screenshot1.png
│   └── Dashboard_Screenshot2.png
│   └── Dashboard_Screenshot3.png
│
├── docs/                 # Documentation
│   └── README.md
```

---

## 📈 Model Performance
- *MAE*  : 5665.18  
- *RMSE* : 7260.16  
- *MAPE* : 13.22%  
- *sMAPE*: 13.16%  

The model provides a reliable monthly sales forecast for decision-making.

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Raj-jad06/FUTURE_ML_01.git

2. Navigate into the project folder:
   cd FUTURE_ML_01/code


3. Install dependencies:
   pip install -r requirements.txt


4. Run the Prophet forecasting script:
   python prophet_model.py


5. The forecast results will be exported as forecast_results.csv.
   Open the Power BI file (Task1_Dashboard.pbix) to explore the dashboard.

📌 Internship Details

- *Internship Program* : Future Interns – Machine Learning Track

- *Candidate ID (CIN)* : FIT/SEP25/ML2732

- *Task* : AI-Powered Sales Forecasting Dashboard (Task 1)