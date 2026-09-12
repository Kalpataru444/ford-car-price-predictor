# 🚗 Ford Car Price Predictor

A machine learning-based used-car valuation system that predicts the price of Ford cars from vehicle specifications.

## 📌 Project Overview

This project was developed as part of a hackathon based on the problem statement:

> Build a dynamic valuation model for the used car market.

The system predicts the estimated price of a Ford vehicle using features such as:

- Car model
- Manufacturing year
- Transmission
- Mileage
- Fuel type
- Tax
- MPG
- Engine size

The project covers data cleaning, exploratory data analysis, preprocessing, model comparison, hyperparameter tuning, external testing, and deployment through a Streamlit web application.

---

## 🧠 Machine Learning Models

Three regression algorithms were explored:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Random Forest performed the best during validation and was selected as the final model after hyperparameter tuning.

---

## 📊 Model Performance

### Tuned Random Forest — Validation Set

| Metric | Score |
|---|---:|
| MAE | 877.86 |
| RMSE | 1219.11 |
| R² | 0.9276 |

### External Test Dataset

| Metric | Score |
|---|---:|
| MAE | 1412.74 |
| RMSE | 1960.80 |
| R² | 0.8285 |

The external test results show how model performance can change when the model is evaluated on data that was not used during model development.

---

## 🔬 Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Data Preprocessing
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
External Testing
     ↓
Model Serialization
     ↓
Streamlit Deployment
🌐 Web Application

The trained model is integrated into a Streamlit application.
Users can enter vehicle specifications such as:

Model
Year
Transmission
Mileage
Fuel Type
Tax
MPG
Engine Size

The application then returns an estimated car price.

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Joblib
Streamlit
Jupyter Notebook

📁 Project Structure
ford-car-price-predictor/
│
├── app.py                  # Streamlit web application
├── fords.ipynb             # Data analysis and model development
├── car_price_model.pkl     # Trained machine learning model
├── train.csv               # Training dataset
├── Test_data.csv           # External test dataset
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
▶️ How to Run the Project
1. Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
2. Navigate to the project directory
cd ford-car-price-predictor
3. Install the required dependencies
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app.py

The application should then open in your browser.

🎯 Future Improvements
Improve model generalization
Experiment with additional regression algorithms
Use cross-validation for more robust model evaluation
Add more relevant vehicle features
Incorporate more recent used-car market data
Deploy the application publicly
Improve the user interface

👨‍💻 Author
Kalpataru Bhattacharyya
B.Tech CSE (AI/ML) Student
---