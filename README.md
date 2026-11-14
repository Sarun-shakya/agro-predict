# 🌱 AgroPredict – Crop Recommendation System

AgroPredict is a machine learning-powered crop recommendation web application that helps users identify the most suitable crop to grow based on soil nutrients and environmental conditions.

By analyzing essential soil and climate parameters, AgroPredict uses a trained Random Forest classification model to provide crop recommendations through an interactive Streamlit interface.

## 🚀 Live Demo

**[🌐 Try AgroPredict](https://agro-predict.streamlit.app/)**

**[📂 GitHub Repository](https://github.com/Sarun-shakya/agro-predict)**


## 📊 Dataset Description

AgroPredict uses a crop recommendation dataset containing **2,200 records** and 8 columns, including 7 input features and 1 target variable.

The dataset contains information about soil nutrient levels and environmental conditions required for different crops.

### Dataset Features

| Feature | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Temperature in °C |
| Humidity | Relative humidity in % |
| ph | Soil pH value |
| Rainfall | Rainfall in mm |
| label | Recommended crop (target variable) |

### Dataset Overview

- **Total Records:** 2,200
- **Input Features:** 7
- **Target Variable:** 1 (`label`)
- **Number of Crop Classes:** 22
- **Class Distribution:** Balanced across crop categories
- **Missing Values:** None
- **Duplicate Records:** None

## 🧠 Machine Learning Model

Several machine learning algorithms were explored and evaluated for crop classification.

The **Random Forest Classifier** was selected as the final model based on its performance.

### Model Performance

| Rank | Algorithm | Accuracy |
|---|---|---|
| 1 | Random Forest | **99.55%** |
| 2 | Support Vector Machine (SVM) | **98.41%** |
| 3 | Logistic Regression | **97.27%** |

The model was trained to identify relationships between soil characteristics, environmental conditions, and suitable crop categories.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Streamlit** – Web application framework
- **Scikit-learn** – Machine learning model development
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Joblib / Pickle** – Model serialization

## 📂 Project Structure

```text
agro-predict/
│
├── images/
├── agro_predict.ipynb
├── app.py
├── crop_model.pkl
├── requirements.txt
└── README.md
```
## 📸 Screenshots

### 🧪 Input Parameters
<img width="1168" height="785" alt="Screenshot 2026-11-14 155603" src="https://github.com/user-attachments/assets/915432c8-1ed6-44db-86ac-858b7bb3fa11" />


### 🌱 Crop Recommendation
<img width="1017" height="727" alt="Screenshot 2026-11-14 155613" src="https://github.com/user-attachments/assets/a64f2ce7-6b78-45a2-9322-11cc05cf7fdb" />


## 💻 Run Locally

Follow these steps to run AgroPredict on your local machine.

**1. Clone the repository**

```bash
git clone https://github.com/Sarun-shakya/agro-predict.git
```

**2. Navigate to the project directory**

```bash
cd agro-predict
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🎯 Project Objective

The primary objective of AgroPredict is to demonstrate how machine learning can be applied to agriculture to support data-driven crop selection.

By analyzing soil nutrients and environmental conditions, the system provides an accessible way to identify suitable crops for cultivation.

## 🔮 Future Improvements

- Integration with real-time weather data.
- Soil data retrieval through external APIs.
- Region-specific agricultural recommendations.
- Crop yield and fertilizer recommendations.
- Multilingual support for better accessibility.

## 👨‍💻 Author
**Sarun Shakya**

- Project: [AgroPredict](https://github.com/Sarun-shakya/agro-predict)
- Live Application: [AgroPredict](https://agro-predict.streamlit.app/)

---

⭐ If you find this project interesting, consider giving the repository a star!
