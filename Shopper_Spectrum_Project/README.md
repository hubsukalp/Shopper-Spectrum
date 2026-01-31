# 🛒 Shopper Spectrum Project

## 📌 Project Overview
The **Shopper Spectrum Project** is an end-to-end data science application that analyzes customer purchasing behavior using **RFM (Recency, Frequency, Monetary) analysis** and **KMeans clustering** for customer segmentation.  

In addition, an **item-based collaborative filtering recommendation system** is implemented to recommend products that are frequently purchased together using **cosine similarity**.

A **Streamlit-based web application** is included to demonstrate real-time customer segmentation and product recommendations.

---

## 🎯 Objectives
- Segment customers into meaningful groups using RFM analysis
- Identify high-value and at-risk customers
- Recommend similar products based on purchase behavior
- Build a deployable, interactive Streamlit application

---

## 🧠 Methodology

### 1️⃣ Data Cleaning & Preprocessing
- Removed cancelled transactions
- Handled missing customer and product descriptions
- Filtered invalid quantities and prices

### 2️⃣ Exploratory Data Analysis (EDA)
- Country-wise sales analysis
- Product-level sales trends
- Monthly revenue patterns
- Transaction monetary value distribution

### 3️⃣ RFM Feature Engineering
- **Recency**: Days since last purchase  
- **Frequency**: Number of transactions  
- **Monetary**: Total spending per customer  

### 4️⃣ Customer Segmentation
- Standardized RFM features
- Applied KMeans clustering
- Optimal number of clusters selected using Elbow Method and Silhouette Score
- Final customer segments:
  - High-Value
  - Regular
  - Occasional
  - At-Risk

### 5️⃣ Product Recommendation System
- Item-based collaborative filtering
- Cosine similarity for product-product similarity
- Top-N product recommendations

### 6️⃣ Model Deployment
- Models saved using `joblib`
- Streamlit app for real-time interaction

---

## 🧪 Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- SciPy
- Streamlit
- Joblib

---

## 📊 Dataset

The project uses the **Online Retail Dataset**, which contains transactional purchase records.

🔗 **Dataset Download Link:**  
https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view

> ⚠️ Due to GitHub file size limitations, the dataset is **not included** in this repository.

### Dataset Placement
After downloading, place the dataset at the following path:
```text
Shopper_Spectrum_Project/data/online_retail.csv
````

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/hubsukalp/Shopper-Spectrum.git
cd Shopper-Spectrum
```

### 2️⃣ Navigate to Project Folder

```bash
cd Shopper_Spectrum_Project
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```text
Shopper-Spectrum/
└── Shopper_Spectrum_Project/
    ├── app.py                  # Streamlit application
    ├── shopper_spectrum.ipynb  # Complete analysis notebook
    ├── models/
    │   ├── kmeans_model.pkl
    │   └── scaler.pkl
    ├── data/                   # Dataset folder (not included)
    ├── requirements.txt
    └── README.md
```

---

## 📈 Key Results

* Identified 4 distinct customer segments
* Found that a small group of customers contributes disproportionately to revenue
* Generated meaningful product recommendations using cosine similarity
* Built an interactive Streamlit application for real-time predictions

---

## 🎥 Project Demo

An explanatory video demonstrating the complete workflow and Streamlit application was submitted separately via Google Drive as per submission instructions.

---

## 🚀 Future Scope

* Incorporate customer demographic information
* Explore advanced recommendation techniques (matrix factorization, deep learning)
* Deploy the application on cloud platforms
* Add business-focused dashboards and analytics
* Enable personalized recommendation history

---

## 👤 Author

**Sukalp Warhekar**
B.Tech – Computer Science & Engineering
Customer Analytics | Machine Learning | Data Science

