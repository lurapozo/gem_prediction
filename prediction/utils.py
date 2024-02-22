import joblib
import pandas as pd

index = {"Fair": 3, "Good": 4, "Ideal": 5, "Premium": 6, "Very Good": 7,
         "D": 8, "E": 9, "F": 10, "G": 11, "H": 12, "I": 13, "J": 14,
         "I1": 15, "IF": 16, "SI1": 17, "SI2": 18, "VS1": 19, "VS2": 20,
         "VVS1": 21, "VVS2": 22}


def predict(
        carat: float,
        depth: float,
        table: float,
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
    :param model: regression model
    :param categories: if it uses categorical features for the prediction
    :param cut: Cut quality of the gem
    :param color: Color of the gem
    :param clarity: Absence of the inclusions and blemishes in the gem
    :return: the predicted price
    """
    arg = [0.0 for i in range(23)]
    arg[0] = carat
    arg[1] = depth
    arg[2] = table
    if categories:
        scaler = joblib.load("./models/scaler_with_cat.z")
        arg[index[cut]] = 1.0
        arg[index[color]] = 1.0
        arg[index[clarity]] = 1.0
        if model == "SVR":
            reg = joblib.load("./models/svr_with_cat.z")
        elif model == "Linear Regression":
            reg = joblib.load("./models/lr_with_cat.z")
        else:  # random forest
            reg = joblib.load("./models/rf_with_cat.z")

        x_norm = scaler.transform(
            pd.DataFrame([arg],
                         columns=['carat', 'depth', 'table', 'cut_Fair', 'cut_Good', 'cut_Ideal',
                                  'cut_Premium', 'cut_Very Good', 'color_D', 'color_E', 'color_F',
                                  'color_G', 'color_H', 'color_I', 'color_J', 'clarity_I1', 'clarity_IF',
                                  'clarity_SI1', 'clarity_SI2', 'clarity_VS1', 'clarity_VS2', 'clarity_VVS1',
                                  'clarity_VVS2'])
        )

    else:
        scaler = joblib.load("./models/scaler_no_cat.z")
        if model == "SVR":
            reg = joblib.ldad("./models/svr_no_cat.z")
        elif model == "Linear Regression":
            reg = joblib.load("./models/lr_no_cat.z")
        else:  # random forest
            reg = joblib.load("./models/rf_no_cat.z")
        x_norm = scaler.transform(
            pd.DataFrame([[carat, depth, table]],
                         columns=['carat', 'depth', 'table'])
        )

    pred = reg.predict(x_norm)

    return pred[0]
