# 🌊 Dissolved Oxygen Predictor

A web-based application that predicts Dissolved Oxygen (DO) levels in aquaculture environments using a LightGBM regression model optimized with Differential Evolution. This helps in monitoring and managing aquatic health effectively.

---

## 🚀 Features

- 🔬 Predicts DO levels based on sensor input: Depth, Temperature, pH, and Conductivity.
- ⚙️ Machine Learning model (LightGBM) optimized with Differential Evolution.
- 🎯 Achieved 97.2% prediction accuracy on real-world lake data (47,000+ samples).
- 🧠 Built with FastAPI and Tailwind CSS for a responsive, clean interface.
- 🔁 Handles invalid inputs (e.g., negative predictions) with a user-friendly error page.

---

## 📷 Preview

![Preview Screenshot](https://vitalpharma.in/wp-content/uploads/2020/12/fishs.jpg)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, Tailwind CSS, Jinja2
- **Backend:** FastAPI (Python)
- **Model:** LightGBM (trained & serialized using `joblib`)
- **Optimization:** Differential Evolution
- **Deployment-ready:** Organized with static templates and endpoints

---

## 📂 Project Structure

├── static/ # CSS and assets
├── templates/ # HTML templates (Jinja2)
│ ├── index.html
│ ├── form.html
│ └── error.html
├── optimized_lgbm_model.pkl # Trained ML model
├── main.py # FastAPI application
└── README.md

## 🔍 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/do-predictor.git
   cd do-predictor
2. **Install dependencies**
   pip install fastapi uvicorn joblib numpy scikit-learn jinja2
3. **Run the Server**
   uvicorn main:app --reload
4. **Visit in local browser**
   http://localhost:8000/
 
