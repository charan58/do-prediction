from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template setup
templates = Jinja2Templates(directory="templates")

# Load the model
model = joblib.load("optimized_lgbm_model.pkl")

@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict-form")
def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict")
async def predict_do(request: Request, Depth: float = Form(...), Temp: float = Form(...),
                     pH: float = Form(...), Cond: float = Form(...)):
    features = np.array([[Depth, Temp, pH, Cond]])
    prediction = model.predict(features)[0]
    if prediction<0:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error_message": "Invalid input details"
        })
    return JSONResponse(content={"prediction": round(float(prediction), 4)})
