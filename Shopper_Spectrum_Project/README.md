# Shopper Spectrum Project

## 📌 Project Overview
The **Shopper Spectrum Project** is an end-to-end data science application that analyzes customer purchasing behavior using **RFM (Recency, Frequency, Monetary) analysis** and **KMeans clustering** for customer segmentation.  
Additionally, an **item-based collaborative filtering recommendation system** suggests products frequently purchased together using cosine similarity.

A **Streamlit web application** is included to demonstrate real-time customer segmentation and product recommendations.

---

## 🎯 Objectives
- Segment customers into meaningful groups using RFM analysis  
- Identify high-value and at-risk customers  
- Recommend similar products based on purchase behavior  
- Build a deployable, interactive Streamlit application  

---

## 🧠 Methodology

1. **Data Cleaning & Preprocessing**
   - Removed cancelled transactions  
   - Handled missing customer and product details  
   - Filtered invalid quantities and prices  

2. **Exploratory Data Analysis (EDA)**
   - Country-wise sales analysis  
   - Product-level sales trends  
   - Monthly revenue patterns  
   - Distribution of transaction monetary values  

3. **RFM Feature Engineering**
   - Recency: Days since last purchase  
   - Frequency: Number of purchases  
   - Monetary: Total spend per customer  

4. **Customer Segmentation**
   - Standardized RFM features  
   - Applied KMeans clustering  
   - Optimal clusters selected using Elbow and Silhouette analysis  
   - Resulting segments:
     - High-Value  
     - Regular  
     - Occasional  
     - At-Risk  

5. **Product Recommendation System**
   - Item-based collaborative filtering using cosine similarity  
   - Top-N product recommendations  

6. **Model Deployment**
   - Models saved using `joblib`  
   - Streamlit app for interactive use  

---

## 🧪 Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 📂 Project Structure
```

Shopper_Spectrum_Project/
│
├── app.py                     # Streamlit application
├── shopper_spectrum.ipynb     # Complete analysis notebook
├── models/
│   ├── kmeans_model.pkl       # Trained KMeans model
│   └── scaler.pkl             # StandardScaler object
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files

````

---

## 📊 Dataset

The project uses the **Online Retail Dataset** containing transactional purchase records.

🔗 **Direct dataset link:**  
https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view?usp=sharing

> ⚠️ Due to GitHub file size and licensing constraints, the dataset is **not included** in this repository.

### To run the project locally
1. Download the dataset from the link above  
2. Place the file inside the `data/` folder as:

```text
data/online_retail.csv
````

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Key Results

* Identified 4 distinct customer segments
* Observed that a small group of customers contributes disproportionately to total revenue
* Validated product recommendations using cosine similarity
* Streamlit app provides real-time customer segmentation and recommendations

---

## 🎥 Project Demo

An explanatory video demonstrating the complete workflow, analysis, and Streamlit application was recorded and submitted separately via Google Drive as per submission instructions.

---

## 🚀 Future Scope

* Incorporate customer demographic data
* Explore matrix factorization or deep learning-based recommendation systems
* Deploy the application on cloud platforms
* Enable personalized recommendation history
* Add business-oriented dashboards and visual analytics

---

## 👤 Author

**Sukalp Warhekar**
B.Tech – Computer Science & Engineering
Customer Analytics | Machine Learning | Data Science
