from pymongo import MongoClient
import pandas as pd
from config import settings

def get_tour_dataframe():
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    collection = db[settings.COLLECTION_NAME]
    data = list(collection.find({}))
    df = pd.DataFrame(data)
    df.rename(columns={'startLocation.description': 'startLocation_description'}, inplace=True)
    return df