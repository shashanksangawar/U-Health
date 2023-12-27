# import joblib
import pickle
def model_import():
    try:

        # model = joblib.load('../Models/heart.pkl')
        # print(pickle.loads("../Models/heart.pkl"))
        # pickle.load(open("heart_disease_model.sav", "rb"))
        model = pickle.load(open("../Models/heart_disease_model.sav", "rb"))
        print(model)
        return type(model)
    except Exception as w:
        return w


def heart_prediction():
    model = model_import()
    return model