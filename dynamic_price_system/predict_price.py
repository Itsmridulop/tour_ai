from .load_model import load
from .prepare_data import prepare

def predict(tours: list):
    df = prepare(tours)
    model = load()
    predictions = model.predict(df)
    tours_with_prices = []
    for tour, price in zip(tours, predictions):
        tour_with_price = tour.copy()
        tour_with_price['price'] = int(round(price))
        tours_with_prices.append(tour_with_price)
    return tours_with_prices
