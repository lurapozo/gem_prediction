import joblib
import pandas as pd

index = {"Fair": 4, "Good": 5, "Ideal": 6, "Premium": 7, "Very Good": 8,
         "D": 9, "E": 10, "F": 11, "G": 12, "H": 13, "I": 14, "J": 15,
         "I1": 16, "IF": 17, "SI1": 18, "SI2": 19, "VS1": 20, "VS2": 21,
         "VVS1": 22, "VVS2": 23}


def predict(
        carat: float,
        depth: float,
        table: float,
        volume: float,
        model: str,
        categories: bool = None,
        cut: str = None,
        color: str = None,
        clarity: str = None
) -> float:
    """
    Detects the regression model that the user wants to use for prediction,
    normalizes the input data and predicts the price with the desired model.
    :param carat: weight of the gem
    :param depth: height of the gem
    :param table: width of the gem
    :param volume: volume of the gem
    :param model: regression model
    :param categories: if it uses categorical features for the prediction
    :param cut: Cut quality of the gem
    :param color: Color of the gem
    :param clarity: Absence of the inclusions and blemishes in the gem
    :return: the predicted price
    """
    arg = [0.0 for i in range(24)]
    arg[0] = carat
    arg[1] = depth
    arg[2] = table
    arg[3] = volume

    match model:
        case "SVR":
            reg_model = "svr"
        case "Linear Regression":
            reg_model = "lr"
        case "Random Forest Regressor":
            reg_model = "rf"
        case "K Nearest Regressor":
            reg_model = "knr"
        case "Gradient Boosting Regressor":
            reg_model = "gbr"
        case _:
            reg_model = "ERROR"

    print(f"./models/{reg_model}_with_cat.z")
    print(arg[:4])
    if categories:
        scaler = joblib.load("./models/scaler_with_cat.z")
        arg[index[cut]] = 1.0
        arg[index[color]] = 1.0
        arg[index[clarity]] = 1.0
        reg = joblib.load(f"./models/{reg_model}_with_cat.z")

        x_norm = scaler.transform(
            pd.DataFrame([arg],
                         columns=['carat', 'depth', 'table', 'volume', 'cut_Fair', 'cut_Good', 'cut_Ideal',
                                  'cut_Premium', 'cut_Very Good', 'color_D', 'color_E', 'color_F',
                                  'color_G', 'color_H', 'color_I', 'color_J', 'clarity_I1', 'clarity_IF',
                                  'clarity_SI1', 'clarity_SI2', 'clarity_VS1', 'clarity_VS2', 'clarity_VVS1',
                                  'clarity_VVS2'])
        )

    else:
        scaler = joblib.load("./models/scaler_no_cat.z")
        reg = joblib.load(f"./models/{reg_model}_no_cat.z")
        x_norm = scaler.transform(
            pd.DataFrame([arg[:4]],
                         columns=['carat', 'depth', 'table', 'volume'])
        )

    pred = reg.predict(x_norm)

    return pred[0]
