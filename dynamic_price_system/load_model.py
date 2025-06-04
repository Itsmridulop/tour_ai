import joblib
from config import settings

def load():
    model = joblib.load(settings.MODEL)
    return model
