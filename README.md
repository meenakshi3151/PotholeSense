# PotholeSense – Pothole Detection System  

**PotholeSense** is a web application built using **Streamlit** that predicts the presence of **potholes** on roads using motion sensor data from **accelerometers** and **gyroscopes**. It leverages a **Machine Learning pipeline (KNN model)** to analyze sensor readings and classify whether a road surface contains a pothole or not.

---

## Features  
- Detects potholes using a trained **KNN-based ML pipeline** (`pothole_detection_model_pipeline.joblib`)  
- Automatically applies **feature engineering** and **data scaling** through the pipeline  
- Provides an **interactive Streamlit interface** for real-time sensor data input  
- Gives **instant prediction results** with clear and intuitive feedback  

---

## Features Used in Prediction  

The model predicts potholes based on the following motion sensor readings:

- **Latitude** — GPS latitude coordinate of the vehicle.  
- **Longitude** — GPS longitude coordinate of the vehicle.  
- **Speed** — Current vehicle speed.  
- **Accelerometer X, Y, Z** — Acceleration values in three axes from the accelerometer.  
- **Gyro X, Y, Z** — Angular velocity readings in three axes from the gyroscope.  
- **Accelerometer Magnitude** — Combined acceleration magnitude.  
- **Gyro Magnitude** — Combined gyroscope magnitude.  

> These features collectively help the model analyze road surface vibrations and identify potential potholes.

---

## Technologies Used  
- **Streamlit** – Web application framework  
- **Python**  
- **Scikit-learn** – ML model and pipeline creation  
- **Pandas**, **NumPy** – Data preprocessing  
- **Joblib** – Model serialization and loading  

---

## Installation & Setup  

```bash
# 1. Clone the repository
git clone https://github.com/meenakshi3151/PotholeSense.git
cd RoadGuard

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate     # On macOS/Linux
# venv\Scripts\activate      # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run main.py
```
