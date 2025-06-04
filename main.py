from fastapi import FastAPI, Query
from recommendation.recommender import TourRecommender
from dynamic_price_system.predict_price import predict

app = FastAPI()

@app.get("/recommend")
def recommend_tours(tour_name: str = Query(..., description="Tour name to base recommendations on")):
    recommender = TourRecommender()  
    recommended_tours = recommender.recommend(tour_name)
    result = predict(recommended_tours)
    return result