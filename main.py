from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="gem.html",
        context={"models":
                     [{"id": 1, "model": "SVR"},
                      {"id": 2, "model": "Linear Regression"},
                      {"id": 3, "model": "Random Forest Classifier"}]}
    )

@app.get("/prediction", response_class=HTMLResponse)
async def predition(
        request: Request,
                    carat: float, depth: float, table: float, model: str):
    if model == "SVR":
        reg = joblib.load("./models/svr_no_cat.z")
        pred = reg.predict([[carat, depth, table]])
    elif model == "Linear Regression":
        reg = joblib.load("./models/lr_no_cat.z")
        pred = reg.predict([[carat, depth, table]])
    else: # random forest
        reg = joblib.load("./models/rf_no_cat.z")
        pred = reg.predict([[carat, depth, table]])
    return templates.TemplateResponse(
        request=request, name="prediction.html", context={"model": model, "price": pred[0]}
    )