import pandas as pd
from sklearn.preprocessing import LabelEncoder


def prepare(tours: list):
    data=pd.DataFrame(tours)[['duration', 'difficulty', 'ratingsAverage', 'startDates']]
    data['startMonth'] = data['startDates'].apply(
        lambda x: pd.to_datetime(x[0]) if x else None
    ).dt.month
    data.drop(columns=['startDates'], inplace=True)
    data['season'] = data['startMonth'].apply(lambda x: 'peak' if x in [6,7,8,12] else 'off')
    data['season'] = data['season'].map({'peak': 1, 'off': 0})
    le = LabelEncoder()
    data['difficulty'] = le.fit_transform(data['difficulty'])
    return data
