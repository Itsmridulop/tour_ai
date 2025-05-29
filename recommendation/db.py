from pymongo import MongoClient
import pandas as pd
from config import settings

def get_tour_dataframe():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    collection = db[settings.COLLECTION_NAME]
    data = list(collection.find({}, {
        'name': 1,
        'summary': 1,
        'description': 1,
        'difficulty': 1,
        'duration': 1,
        'price': 1,
        'imageCover': 1,
        'startLocation.description': 1,
        'startDates': 1,
        'ratingsAverage': 1,
        'ratingsQuantity': 1,
        'maxGroupSize': 1,
    }))
    df = pd.json_normalize(data)
    df.rename(columns={'startLocation.description': 'startLocation_description'}, inplace=True)
    return df