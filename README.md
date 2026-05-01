# 📉 Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

Hi there! 👋

This is an end-to-end Machine Learning project I built to predict whether a customer will churn (cancel their subscription) based on their service data. 

My main focus here was to write clean, production-ready code. I used `Scikit-Learn Pipelines` to prevent data leakage and `GridSearchCV` to optimize a `RandomForest` model. Finally, I deployed the model using a simple `Streamlit` web app.

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn (RandomForest, Pipelines, GridSearchCV)
* **Data Processing:** Pandas, NumPy
* **Web UI:** Streamlit

## 🚀 How to Run Locally

```bash
git clone [https://github.com/YourUsername/Customer-Churn-Prediction.git](https://github.com/YourUsername/Customer-Churn-Prediction.git)
cd Customer-Churn-Prediction
pip install pandas numpy scikit-learn streamlit joblib
streamlit run app.py
📁 Repository Structure
app.py: The Streamlit web app script.

churn_prediction_pipeline.pkl: The trained and optimized model ready for inference.

model_training.ipynb: The notebook containing data exploration and model training steps.

Feel free to connect with me on LinkedIn!
