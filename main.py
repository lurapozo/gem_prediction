from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prediction import utils

app = FastAPI()

templates = Jinja2Templates(directory="templates")

cuts = ["Premium", "Ideal", "Very Good", "Good", "Fair"]
colors = ["D", "E", "F", "G", "H", "I", "J"]
clarities = ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="gem.html",
        context={"models":
                     [{"id": 1, "model": "SVR"},
                      {"id": 2, "model": "Linear Regression"},
                      {"id": 3, "model": "Random Forest Classifier"}],
                 "cuts": cuts, "colors": colors, "clarities": clarities}
    )

@app.post("/prediction", response_class=HTMLResponse)
async def prediction(
        request: Request,
        carat: Annotated[float, Form()],
        depth: Annotated[float, Form()],
        table: Annotated[float, Form()],
        model: Annotated[str, Form()],
        categories: Annotated[bool, Form()] = None,
        cut: Annotated[str, Form()] = None,
        color: Annotated[str, Form()] = None,
        clarity: Annotated[str, Form()] = None):

    pred: float = utils.predict(carat, depth, table, model, categories, cut, color, clarity)
    return templates.TemplateResponse(
        request=request, name="prediction.html", context={"model": model, "price": pred}
    )
