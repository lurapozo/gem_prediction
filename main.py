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
    """
    Renders the main page, provides data needed to create all the selects in the HTML.
    :param request:
    :return: the HTML to render the main page, ML model to predict the price of the Zircon, the types of cuts colors and
    clarities the gem can have
    """
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
    """
    Renders the prediction of the price given by the model with the given parameters of the Zircon.
    :param request:
    :param carat: weight of the gem
    :param depth: height of the gem
    :param table: width of the gem
    :param model: regression model
    :param categories: if it uses categorical features for the prediction (bad name, I know)
    :param cut: Cut quality of the gem
    :param color: Color of the gem
    :param clarity: Absence of the inclusions and blemishes in the gem
    :return: the html to render the prediction, the name of the regression model and the predicted price
    """
    pred: float = utils.predict(carat, depth, table, model, categories, cut, color, clarity)
    return templates.TemplateResponse(
        request=request, name="prediction.html", context={"model": model, "price": "{:.2f}".format(pred)}
    )
