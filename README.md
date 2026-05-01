📉 Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

Hi there! 👋

This is an end-to-end Machine Learning project designed to predict customer churn. The primary focus of this project is to implement clean, production-ready code. To achieve this, I utilized `Scikit-Learn Pipelines` to eliminate data leakage and applied `GridSearchCV` to rigorously optimize a `RandomForest` classifier. The final model is deployed via an interactive `Streamlit` web application.

## 📊 Data Insights & Model Performance

Visualizing the data is a crucial step to uncover underlying patterns before model training. Below are the key insights derived from the Exploratory Data Analysis (EDA):

**1. Target Variable Distribution**
The dataset exhibits a class imbalance, which is a standard characteristic of real-world churn data.
![Churn Distribution](churn_distribution.png)

**2. Feature Correlations**
Analyzing linear correlations between numerical features and the target variable to understand predictive strength.
![Correlation Heatmap](correlation_heatmap.png)

**3. Behavioral Analysis**
Evaluating the impact of continuous variables, such as 'Tenure' and 'Monthly Charges', on the customer churn rate.
![Boxplots Analysis](features_boxplots.png)
![Tenure Density](tenure_density.png)

**4. Final Model Evaluation**
The Confusion Matrix detailing the exact true positive/negative and false positive/negative predictions of the optimized Random Forest model.
![Confusion Matrix](confusion_matrix.png)

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn (RandomForest, Pipelines, GridSearchCV)
* **Data Processing:** Pandas, NumPy
* **Web UI:** Streamlit
* **Data Visualization:** Seaborn, Matplotlib

## 🚀 How to Run Locally

To run this project on your local machine, follow these steps:

```bash
git clone https://github.com/YourUsername/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt
streamlit run app.py
📁 Repository Structure
app.py: The Streamlit web application script.

churn_prediction_pipeline.pkl: The serialized, optimized machine learning pipeline ready for inference.

model_training.ipynb: The Jupyter Notebook containing the data exploration, preprocessing, and model training workflows.

requirements.txt: The list of project dependencies.

Feel free to connect with me on LinkedIn to discuss this project or explore potential collaborations!
